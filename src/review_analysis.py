# %%
import pandas as pd
import nltk
from nltk.corpus import stopwords
import string
import numpy as np    
from nltk.tokenize import word_tokenize 
import nltk

# download punctuation related NLTK functions
# (needed for sent_tokenize())
nltk.download('punkt')

nltk.download('averaged_perceptron_tagger')
# download wordnet
# (needed for lemmatization)
nltk.download('wordnet')
# download stopword lists
# (needed for stopword removal)
nltk.download('stopwords')
# dictionary of English words
nltk.download('words')
nltk.download('omw-1.4')
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

import matplotlib.pyplot as plt
import urllib.request

!pip install wordcloud
from wordcloud import WordCloud

import warnings
warnings.filterwarnings("ignore")

# %%
df=pd.read_csv("K8 Reviews.csv")
df

# %%
df=df[['review']]

df

# %%
# converting to lowercase
df['review'] = df['review'].str.lower()

# %%
df[['review']]

# %%


# %%

translator = str.maketrans('', '', string.punctuation)

# Apply translation to remove punctuation from each row in the 'review' column
df['review'] = df['review'].apply(lambda x: x.translate(translator))

# %%
df[['review']]

# %%

stop_words = set(stopwords.words('english'))
def remove_stopwords(text):
    return ' '.join([word for word in text.split() if word.lower() not in stop_words])

# Apply the function to the 'review' column
df['review'] = df['review'].apply(remove_stopwords)
df[['review']]

# %%
# Define a function to map POS tags to WordNet POS tags
def get_wordnet_pos(tag):
    if tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  # default to noun if the tag is not recognized

# Function to perform lemmatization
def lemmatize_text(text):
    tokens = word_tokenize(text)  # Tokenize the text
    pos_tags = nltk.pos_tag(tokens)  # Perform POS tagging
    
    lemmatizer = nltk.stem.WordNetLemmatizer()
    lemmatized_text = []
    for token, pos_tag in pos_tags:
        wordnet_pos = get_wordnet_pos(pos_tag)  # Map POS tag to WordNet POS
        lemmatized_token = lemmatizer.lemmatize(token, pos=wordnet_pos)  # Lemmatize the token
        lemmatized_text.append(lemmatized_token)
    
    return ' '.join(lemmatized_text)  # Join lemmatized tokens into a single string

# Apply lemmatization to the 'review' column
df['review'] = df['review'].apply(lemmatize_text)
df[['review']]

# %%
reviews = ' '.join(df['review'])
review_list = reviews.split()

# %%
frequencies = nltk.probability.FreqDist(review_list)


# %%
frequencies

# %%
# Plot the frequencies
frequencies.plot(15,cumulative=False)
plt.show()

# %%
#@title Run this code first: Wordcloud function and loading the document (double-click to view) {display-mode: "form"}


# Draw a wordcloud!
# Inputs:
#   word_counts: a dictionary mapping strings to their counts
def draw_wordcloud(freq_dist, colormap):
    
    #TODO add a few corpus specific checks here to make sure people have done casing, lemmatization, punct removal
    uniq_count = len(freq_dist.keys())
    print("Building a word cloud with",uniq_count,"unique words...")
    wc = WordCloud(colormap=colormap, width=1500, 
                   height=1000).generate_from_frequencies(freq_dist)
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    



# %%
colormap = None
# Call the function to draw the word cloud
draw_wordcloud(frequencies, colormap)




