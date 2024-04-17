# Load libraries
import nltk
nltk.download('averaged_perceptron_tagger')
from nltk import pos_tag
from nltk import word_tokenize
# Create text
text_data = "Chris loved outdoor running"
# Use pre-trained part of speech tagger
text_tagged = pos_tag(word_tokenize(text_data))
# Show parts of speech
print(text_tagged)