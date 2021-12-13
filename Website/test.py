
import pytest
import sentiment_app

def test_sent_tokenized():
    assert sentiment_app.sent_tokenized("I'm angry!") == [['I', "'m", 'angry', '!']]

def test_sent_tokenized():
    actual = sentiment_app.sent_tokenized("I'm angry!")
    expected = [['I', "'m", 'angry', '!']]
    assert actual == expected

def test_sent_tokenized_empty_string():
    actual = sentiment_app.sent_tokenized("")
    expected = []
    assert actual == expected

def test_all():
    test_sent_tokenized()




