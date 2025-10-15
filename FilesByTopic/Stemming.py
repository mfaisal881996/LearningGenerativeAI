words = ["running", "runner", "ran", "easily", "fairly" , "fairness" , "cats", "catlike", "catty" , "cat"]

from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer , RegexpStemmer

# Initialize the stemmers
porter = PorterStemmer()
lancaster = LancasterStemmer()
regex = RegexpStemmer('ing$|s$|e$|able$', min=4)
snowball = SnowballStemmer("english")

print("Original Words:")
print(words)

# Apply stemming using different algorithms
print("\nPorter Stemmer:") 
for word in words:
    print(f"{word} -> {porter.stem(word)}")


print(regex.stem("eating"))

# Apply Snowball stemming
print("\nSnowball Stemmer:")
for word in words:
    print(f"{word} -> {snowball.stem(word)}")


# Apply Lancaster stemming
print("\nLancaster Stemmer:")
for word in words:
    print(f"{word} -> {lancaster.stem(word)}")


# Creating a table for comparison
print("\nComparison Table:")
print(f"{'Word':<12} {'Porter':<12} {'Snowball':<12} {'Lancaster':<12} {'Regexp':<12}")
for word in words:
    print(f"{word:<12} {porter.stem(word):<12} {snowball.stem(word):<12} {lancaster.stem(word):<12} {regex.stem(word):<12}")