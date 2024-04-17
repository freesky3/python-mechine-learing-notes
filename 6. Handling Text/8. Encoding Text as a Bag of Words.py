# Load library
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
# Create text
text_data = np.array(['I love Brazil. Brazil!',
'Sweden is best',
'Germany beats both'])
# Create the bag of words feature matrix
count = CountVectorizer()
bag_of_words = count.fit_transform(text_data)
# Show feature matrix
print(bag_of_words)
print(bag_of_words.toarray())
print(count.get_feature_names_out())


# Create feature matrix with arguments
count_2gram = CountVectorizer(ngram_range=(1,2),
stop_words="english",
vocabulary=['brazil'])
bag = count_2gram.fit_transform(text_data)
# View feature matrix
print(bag.toarray())
# View the 1-grams and 2-grams
print(count_2gram.vocabulary_)