from gensim.models import KeyedVectors
model = KeyedVectors.load("glove_50.model")
"""So what do the numbers actually represent, then?
They represent position in a geometric space, 
learned entirely from patterns of word co-occurrence in huge amounts of text. 
Here's the training intuition: The model was trained by looking at billions of
 sentences and repeatedly asking: "which words tend to appear near which other words?"
  Words that show up in similar contexts 
  (e.g., "hello" and "hi" both often precede greetings, appear near "goodbye",
   follow punctuation similarly) get pushed toward similar vectors during training. 
   Words that never appear in similar contexts (e.g., "hello" and "spreadsheet") get pushed apart."""
vec = model["hello"]
print(vec[:5])
print('find word most similar to {} '.format(model.most_similar("hello")))
print(model.most_similar(positive=["king","woman"],negative=["man"]))# king - man + woman = queen

print(model.similarity("good","great")) # 0.79
print(model.similarity("good","turtle")) # 0.13

