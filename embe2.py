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

class OK(nn.Module):
    def __init__(self   , input_size,hidden_size,num_classes):
        super().__init__() # required to call nn.module , that is important for neural network
        
