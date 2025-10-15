import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk import ne_chunk

sentence = "Barack Obama was born in Hawaii. He was elected president in 2008."
tokens = word_tokenize(sentence)
tagged_tokens = pos_tag(tokens)
named_entities = ne_chunk(tagged_tokens)
print(named_entities)
