from flask import Flask, request, render_template

import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from collections import defaultdict
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('Website.html')

# Here we collect the sentence entered by the user on the web interface
def input_sent():
    input = request.form['sentence']
    return input

#tokenize sentences : split input sentence into words
def sent_tokenized(input):
    data_clean_sent_tokenized = sent_tokenize(input)
    data_clean_word_sent_tokenized = [word_tokenize(sentence) for sentence in data_clean_sent_tokenized]
    return data_clean_word_sent_tokenized

#lower text
def lower_sent(token):
    stc_token_lower=[]
    for i in range(len(token)):
        stc_token_lower.append([word.lower() for word in token[i]])
    return stc_token_lower

#Lemmatize : etablish relationships between words and remove stopwords
def lemmatize(lower_sent):
    stopWords = stopwords.words('english')
    word_lemmatizer = WordNetLemmatizer()
    final_sent = []
    for sent in lower_sent:
        for word in sent:
            if word not in stopWords:
                final_sent.append(word_lemmatizer.lemmatize(word))
    final_input = ' '.join(final_sent)
    return final_input

#We use Vader library to analyse the sentiment of the text
#the compound is the positive metrics
def analysis(lemmatize_token):
    analyser = SentimentIntensityAnalyzer()
    score = analyser.polarity_scores(lemmatize_token)
    res = "{:-<40} {}".format(lemmatize_token, str(score))
    return score['compound']

def result(score):
    print(score)
    res= ""
    if score > 0 :
        res="positive"
    elif score < 0 :
        res="negative"
    elif score == 0 :
        res="neutral"
    else:
        res="error"
    return res

@app.route('/', methods=['POST'])

def final_function():
    input = input_sent()
    data_clean_word_sent_tokenized = sent_tokenized(input)
    stc_token_lower= lower_sent(data_clean_word_sent_tokenized)
    final_input = lemmatize(stc_token_lower)
    score = analysis(final_input)
    res=result(score)
    return render_template('Website.html', final=res)



#def final_function():
    input = request.form['sentence']
    data_clean_sent_tokenized = sent_tokenize(input)
    data_clean_word_sent_tokenized = [word_tokenize(sentence) for sentence in data_clean_sent_tokenized]

    stc_token_lower=[]
    for i in range(len(data_clean_word_sent_tokenized)):
        stc_token_lower.append([word.lower() for word in data_clean_word_sent_tokenized[i]])

    tag_map = defaultdict(lambda: wn.NOUN)
    tag_map['J'] = wn.ADJ
    tag_map['V'] = wn.VERB
    tag_map['R'] = wn.ADV
    stopWords = stopwords.words('english')
    word_lemmatizer = WordNetLemmatizer()

    final_sent = []
    for sent in stc_token_lower:
        for word in sent:
            if word not in stopWords:
                final_sent.append(word_lemmatizer.lemmatize(word))


    final_input = ' '.join(final_sent)

    analyser = SentimentIntensityAnalyzer()

    score = analyser.polarity_scores(final_input)
    res = "{:-<40} {}".format(final_input, str(score))
    return render_template('Website.html', final=res)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

