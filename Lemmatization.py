nouns = ["cats", "geese", "mice", "children", "feet"]
verbs = ["running", "going", "working" , "eating" , "doing" , "kicking"]
adjectives = ["better", "best", "worse", "worst", "fairer", "fairest", "easier", "easiest" , "fairly"]

from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('wordnet')
# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Apply lemmatization
print("\nLemmatized Words Nouns:")
for word in nouns:
    print(f"{word} -> {lemmatizer.lemmatize(word , pos='n')}")

print("\nLemmatized Words Verbs:")
for word in verbs:
    print(f"{word} -> {lemmatizer.lemmatize(word , pos='v')}")

print("\nLemmatized Words Adjectives:")
for word in adjectives:
    print(f"{word} -> {lemmatizer.lemmatize(word , pos='a')}")