import nltk
nltk.download('averaged_perceptron_tagger_eng')
from nltk.tokenize import word_tokenize
from nltk import pos_tag

def convert_sentence_to_words(sentence):
    return word_tokenize(sentence)

def convert_words_to_pos_tags(words):
    return pos_tag(words)

def extract_nouns_and_verbs(pos_tags):
    nouns = [word for word, tag in pos_tags if tag.startswith('NN')]
    verbs = [word for word, tag in pos_tags if tag.startswith('VB')]
    return nouns, verbs

# Example usage
sentence = "The quick brown fox jumps over the lazy dog."
words = convert_sentence_to_words(sentence)
pos_tags = convert_words_to_pos_tags(words)
nouns, verbs = extract_nouns_and_verbs(pos_tags)
print("Nouns:", nouns)
print("Verbs:", verbs)