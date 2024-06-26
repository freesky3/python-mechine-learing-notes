# Load libraries
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
# Create text
text_data = np.array(['I love Brazil. Brazil!',
'Sweden is best',
'Germany beats both'])
# Create the tf-idf feature matrix
tfidf = TfidfVectorizer()
feature_matrix = tfidf.fit_transform(text_data)
# Show tf-idf feature matrix
print(feature_matrix)
# Show tf-idf feature matrix as dense matrix
print(feature_matrix.toarray())
# Show feature names
print(tfidf.vocabulary_)