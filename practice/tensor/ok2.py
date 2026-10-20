import torch as tt
import torchvision as tv
from torchvision import transforms as trf


train_data_path = "./train"
val_data_path = "./val"
test_data_path = "./test"
transforms  = trf.Compose([trf.Resize(64),
                           trf.ToTensor(),
                           trf.Normalize(mean=[0.485,0.456,0.406],
                                         std = [0.229,0.224,0.225])])
train_data = tv.datasets.ImageFolder(root=train_data_path,transform=transforms)
val_data = tv.datasets.ImageFolder(root = val_data_path,transform = transforms)
test_data = tv.datasets.ImageFolder(root = test_data_path , transform = transforms)

