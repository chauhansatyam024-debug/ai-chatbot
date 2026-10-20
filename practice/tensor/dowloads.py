# dowloads.py
import os
import sys
import urllib3
from urllib.parse import urlparse
import pandas as pd
import itertools
import shutil
from concurrent.futures import ThreadPoolExecutor, as_completed

from urllib3.util import Retry, Timeout

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

classes = ["cat", "fish"]
set_types = ["train", "test", "val"]

# one shared pool for all threads
http = urllib3.PoolManager(
    retries=Retry(connect=1, read=1, redirect=2),
    timeout=Timeout(connect=5, read=10),
)


def download_image(url, klass, data_type):
    basename = os.path.basename(urlparse(url).path)
    filename = "{}/{}/{}".format(data_type, klass, basename)
    if os.path.exists(filename):
        return True
    try:
        with http.request("GET", url, preload_content=False) as resp:
            if resp.status != 200:
                return False
            with open(filename, "wb") as out_file:
                shutil.copyfileobj(resp, out_file)
        return True
    except Exception:
        if os.path.exists(filename):
            os.remove(filename)  # don't leave half-written files
        return False


if __name__ == "__main__":
    if not os.path.exists("images.csv"):
        print("Error: can't find images.csv!")
        sys.exit(0)

    imagesDF = pd.read_csv("images.csv")
    imagesDF = imagesDF[imagesDF["class"].isin(classes)]

    for set_type, klass in itertools.product(set_types, classes):
        path = "./{}/{}".format(set_type, klass)
        if not os.path.exists(path):
            print("Creating directory {}".format(path))
            os.makedirs(path)

    total = len(imagesDF)
    print("Downloading {} images".format(total))

    done = failed = 0
    with ThreadPoolExecutor(max_workers=16) as pool:
        futures = [
            pool.submit(download_image, url, klass, data_type)
            for url, klass, data_type in zip(
                imagesDF["url"], imagesDF["class"], imagesDF["type"]
            )
        ]
        for f in as_completed(futures):
            done += 1
            if not f.result():
                failed += 1
            if done % 50 == 0 or done == total:
                print("{}/{} processed, {} failed".format(done, total, failed))
    sys.exit(0)