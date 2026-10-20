import gensim.downloader as api

model = api.load("glove-wiki-gigaword-50")
model.save("glove_50.model")