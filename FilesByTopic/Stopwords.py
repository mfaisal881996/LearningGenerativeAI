paragraph = """Natural language processing (NLP) is a field of artificial intelligence that focuses on the interaction between computers and humans through natural language. The ultimate objective of NLP is to enable computers to understand, interpret, and generate human language in a way that is valuable."""

from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
from nltk.tokenize import word_tokenize , sent_tokenize

# Get the list of English stopwords
stop_words = set(stopwords.words('english'))
print("Original Paragraph:")
print(paragraph)

# Tokenize the paragraph into words
print("\nTokenized Words:")
words = word_tokenize(paragraph)
print(words)

# Tokenize the paragraph into sentences
print("\nTokenized Sentences:")
sentences = sent_tokenize(paragraph)
print(sentences)

# Remove stopwords from the tokenized sentences
print("\nSentences after Stopword Removal:")
filtered_sentences = []
for sentence in sentences:
    word_tokens = word_tokenize(sentence)
    filtered_sentence = [word for word in word_tokens if word.lower() not in stop_words]
    filtered_sentences.append(" ".join(filtered_sentence))
    print(filtered_sentence)