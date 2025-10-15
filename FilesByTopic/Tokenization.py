corpus = "This is a sample corpus for tokenization. It includes punctuation, numbers like 123, and special characters like #, $, and %."
print("Original Corpus:")
print(corpus)

# Tokenization using NLTK
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize, sent_tokenize , TreebankWordTokenizer

# Tokenization using sentence-based method
print("Sentence Tokenization:")
print(sent_tokenize(corpus))

# Tokenization using word-based method
print("Word Tokenization:")
print(word_tokenize(corpus))

# Tokenization using TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()
print("Treebank Word Tokenization:")
print(tokenizer.tokenize(corpus))

#Counting Words for differences in tokenization methods
print(len(word_tokenize(corpus)))
print(len(tokenizer.tokenize(corpus)))

