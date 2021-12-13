#!/usr/bin/env python
# coding: utf-8

# # Sentiment Analysis Application

# ## importation
get_ipython().system("pip install nltk")
get_ipython().system('pip install vaderSentiment')

import nltk

from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

from nltk.stem import WordNetLemmatizer 
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from collections import defaultdict


# Here you have to collect the sentence entered by the user
#for exemple
input = "I'm angry!"


#tokenize sentences : split input sentence into words
def sent_tokenized (stc):
    data_clean_sent_tokenized = sent_tokenize(stc)
    data_clean_word_sent_tokenized = [word_tokenize(sentence) for sentence in data_clean_sent_tokenized]
    return data_clean_word_sent_tokenized

stc_token = sent_tokenized(input)
print(stc_token)

#lower text
stc_token_lower=[]
for i in range(len(stc_token)):
    stc_token_lower.append([word.lower() for word in stc_token[i]])
print(stc_token_lower)

#remove stopwords + Lemmatize : etablish relationships between words
#POS : give pos tag for each word
tag_map = defaultdict(lambda: wn.NOUN)
tag_map['J'] = wn.ADJ
tag_map['V'] = wn.VERB
tag_map['R'] = wn.ADV

stopWords = stopwords.words('english')
word_lemmatizer = WordNetLemmatizer()

def lemmatize(token):
    final_sent = []
    for sent in token:
        for word in sent:
            if word not in stopWords:
                final_sent.append(word_lemmatizer.lemmatize(word))


final_sent


# In[97]:


final_input = ' '.join(final_sent)
final_input


# ## using Vader library

# In[98]:


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()


# In[99]:


def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    print("{:-<40} {}".format(sentence, str(score)))
    return score['compound']

#we return only the compound score but we 


# In[100]:


sentiment_analyzer_scores(final_input)
#the compound is the positive metrics


# In[101]:


def sentiment():
    if sentiment_analyzer_scores(final_input) > 0 :
        return "positive"
    if sentiment_analyzer_scores(final_input) < 0 :
        return "negative"
    if sentiment_analyzer_scores(final_input) == 0 :
        return "neutral"


# In[103]:


print(sentiment())


# In[ ]:




