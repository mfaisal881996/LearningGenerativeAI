import nltk
nltk.download('averaged_perceptron_tagger_eng')
from nltk.tokenize import word_tokenize
from nltk import pos_tag


def converting_sentence_to_words(sentence):
    # Tokenize the text into words
    words = word_tokenize(sentence)
    return words

def pos_tagging(words):
    # Perform POS tagging
    tagged_words = pos_tag(words)
    return tagged_words

def count_nouns(tagged_words):
    # Count the number of nouns in the tagged words
    noun_count = sum(1 for word, tag in tagged_words if tag.startswith('NN'))
    return noun_count

def count_verbs(tagged_words):
    # Count the number of verbs in the tagged words
    verb_count = sum(1 for word, tag in tagged_words if tag.startswith('VB'))
    return verb_count

def count_adjectives(tagged_words):
    # Count the number of adjectives in the tagged words
    adjective_count = sum(1 for word, tag in tagged_words if tag.startswith('JJ'))
    return adjective_count

def count_adverbs(tagged_words):
    # Count the number of adverbs in the tagged words
    adverb_count = sum(1 for word, tag in tagged_words if tag.startswith('RB'))
    return adverb_count

# Example usage
if __name__ == "__main__":
    text = "The quick brown fox jumps over the lazy dog."
    words = converting_sentence_to_words(text)
    tagged_words = pos_tagging(words)
    noun_count = count_nouns(tagged_words)
    verb_count = count_verbs(tagged_words)  
    adjective_count = count_adjectives(tagged_words)
    adverb_count = count_adverbs(tagged_words)

    print(f"Text: {text}")
    print(f"Noun Count: {noun_count}")
    print(f"Verb Count: {verb_count}")
    print(f"Adjective Count: {adjective_count}")
    print(f"Adverb Count: {adverb_count}")