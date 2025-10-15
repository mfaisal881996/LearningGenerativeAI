
import nltk 
nltk.download('averaged_perceptron_tagger_eng')
from nltk.tokenize import word_tokenize
from nltk import pos_tag
text = "The quick brown fox jumps over the lazy dog."

# Tokenize the text into words
words = word_tokenize(text)
print("Tokenized Words:")
print(words)

# Perform POS tagging
tagged_words = pos_tag(words)
print("\nPOS Tagged Words:")
print(tagged_words)