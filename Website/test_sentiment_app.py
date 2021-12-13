
import pytest
import sentiment_app

#to run tests
# go to the folder DE_Project\Website path on a terminal
# type this command : python -m pytest

# test sent_tokenized()
def test_sent_tokenized():
    actual = sentiment_app.sent_tokenized("I'm angry!")
    expected = [['I', "'m", 'angry', '!']]
    assert actual == expected

def test_sent_tokenized_two():
    actual = sentiment_app.sent_tokenized("The sky is blue. I love it !")
    expected = [['The', 'sky', 'is', 'blue', '.'], ['I', 'love', 'it', '!']]
    assert actual == expected

def test_sent_tokenized_empty_string():
    actual = sentiment_app.sent_tokenized("")
    expected = []
    assert actual == expected


# test lower_sent() 
def test_lower():
    actual = sentiment_app.lower_sent([['I', "'m", 'angry', '!']])
    expected = [['i', "'m", 'angry', '!']]
    assert actual == expected

def test_lower_two():
    actual = sentiment_app.lower_sent([['the', 'sky', 'is', 'blue', '.'], ['I', 'love', 'it', '!']])
    expected = [['the', 'sky', 'is', 'blue', '.'], ['i', 'love', 'it', '!']]
    assert actual == expected

def test_lower_empty_list():
    actual = sentiment_app.lower_sent([])
    expected = []
    assert actual == expected

# test lemmatize()
def test_lemmatize():
    actual = sentiment_app.lemmatize([['i', "'m", 'angry', '!']])
    expected = "'m angry !"
    assert actual == expected

def test_lemmatize_two():
    actual = sentiment_app.lemmatize([['the', 'sky', 'is', 'blue', '.'], ['i', 'love', 'it', '!']])
    expected = "sky blue . love !"
    assert actual == expected

def test_lemmatize_empty_list():
    actual = sentiment_app.lemmatize([])
    expected = ''
    assert actual == expected

# test analysis()
def test_analysis_type():
    actual = type(sentiment_app.analysis("'m angry !"))
    expected = float
    assert actual == expected

def test_analysis_two_type():
    actual = type(sentiment_app.analysis("sky blue . love !"))
    expected = float
    assert actual == expected

def test_analysis_empty_type():
    actual = type(sentiment_app.analysis(''))
    expected = float
    assert actual == expected

def test_analysis_range_two():
    actual = (sentiment_app.analysis("sky blue . love !") >= -1 and sentiment_app.analysis("sky blue . love !") <= 1)
    expected = True
    assert actual == expected

def test_analysis_range():
    actual = (sentiment_app.analysis("'m angry !") >= -1 and sentiment_app.analysis("sky blue . love !") <= 1)
    expected = True
    assert actual == expected

def test_analysis_empty_string():
    actual = (sentiment_app.analysis("") == 0)
    expected = True
    assert actual == expected

#test result()
def test_result_zero():
    actual = sentiment_app.result(0)
    expected = "neutral"
    assert actual == expected

def test_result_negative():
    actual = sentiment_app.result(-1)
    expected = "negative"
    assert actual == expected

def test_result_negative():
    actual = sentiment_app.result(0.1)
    expected = "positive"
    assert actual == expected







