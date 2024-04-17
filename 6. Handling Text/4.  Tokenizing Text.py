# Load library
from nltk.tokenize import word_tokenize
# Create text
string = "The science of today is the technology of tomorrow"
# Tokenize words
print(word_tokenize(string))


# Load library
from nltk.tokenize import sent_tokenize
# Create text
string = "The science of today is the technology of tomorrow. Tomorrow is today."
# Tokenize sentences
print(sent_tokenize(string))