# Load libraries
import nltk
from nltk import pos_tag
from nltk import word_tokenize
from sklearn.preprocessing import MultiLabelBinarizer
# Create text
text_data = "Chris loved outdoor running"
# Use pre-trained part of speech tagger
text_tagged = pos_tag(word_tokenize(text_data))
# Show parts of speech
print(text_tagged)


# Filter words
print([word for word, tag in text_tagged if tag in ['NN','NNS','NNP','NNPS'] ])


# Create text
tweets = ["I am eating a burrito for breakfast",
"Political science is an amazing field",
"San Francisco is an awesome city"]
# Create list
tagged_tweets = []
# Tag each word and each tweet
for tweet in tweets:
    tweet_tag = nltk.pos_tag(word_tokenize(tweet))
    tagged_tweets.append([tag for word, tag in tweet_tag])
# Use one-hot encoding to convert the tags into features
one_hot_multi = MultiLabelBinarizer()
print(one_hot_multi.fit_transform(tagged_tweets))


# Show feature names
print(one_hot_multi.classes_)