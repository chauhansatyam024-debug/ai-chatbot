import torch
import numpy as np
import json
import torch.nn as nn
from gensim.models import KeyedVectors
model = KeyedVectors.load("glove_50.model") # gensim vector
with open("intents.json" ,"r") as f:
    data  = json.load(f)



def sentence_to_vector(sentence,model):
    sentence = sentence.lower().split()
    vectors = [model[w] for w in sentence if w in model]


    """ it will return vector of word in sentence , e.g : hello there ,
    so it will give vector of hello and there , two vector from model taken from gensim"""

    if not vectors:
        return np.zeros(50)

    #this is if user enter something gibberish or nothing , so our model doesn't crash

    return np.mean(vectors,axis=0)


    """ this will return one list of 50-dim from Nth vector , we hv taken axis = 0 'row ',
    coz only mean of rows can give single list of 50-dim vector ,if we use axis = 1 , then we will get 
    multiple nth- dim vector in single row, here n mean word used after vectorization after removing , waste words"""


#vec = sentence_to_vector("hello there my name is satyam " , model) # getting vector in numpy
#tensor = torch.tensor(vec,dtype = torch.float32) # numpy as default float64 , but torch use float32, we are just converting from numpy dtype to torch.tensor

#print(tensor)
#print(vec)
#print(tensor.shape)

x =[]
y =[]
for intent in data["intents"]:
    tag = intent["tag"]
    for pattern in intent["patterns"]:
        vec = sentence_to_vector(pattern,model)
        x.append(vec)
        y.append(tag)

print(len(x) , len(y))
print(x[1].shape)
print(y[0])

tags = sorted(set(y))
tag_to_index = {tag:i for i,tag in enumerate(tags)} # used numbers to feed pytorch
index_to_tag = {i:tag for tag , i in tag_to_index.items()}

y_indices = [tag_to_index[tag] for tag in y]
print(len(tags))
print(tag_to_index)
print(y_indices[:5])