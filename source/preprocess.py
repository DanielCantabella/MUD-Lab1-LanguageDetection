import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pandas as pd


#Tokenizer function. You can add here different preprocesses.
def preprocess(sentence, labels):
    '''
    Task: Given a sentence apply all the required preprocessing steps
    to compute train our classifier, such as sentence splitting, 
    tokenization or sentence splitting.

    Input: Sentence in string format
    Output: Preprocessed sentence either as a list or a string
    '''
    # Place your code here
    # Keep in mind that sentence splitting affectes the number of sentences
    # and therefore, you should replicate labels to match.

    # Tokenization, lowercasing, removing punctuation, stop words, and stemming
    stemmer = PorterStemmer()
    preprocessed_texts = []
    for text in sentence:
        tokens = nltk.word_tokenize(text.lower())
        # tokens = [token for token in tokens if token.isalpha()]
        # stop_words = set(stopwords.words('english'))
        # tokens = [token for token in tokens if token not in stop_words]
        # tokens = [stemmer.stem(token) for token in tokens]
        # tokens = [token for token in tokens if token.isalpha()]
        preprocessed_text = " ".join(tokens)
        preprocessed_texts.append(preprocessed_text)

    # Convert preprocessed texts list to pandas Series
    sentence = pd.Series(preprocessed_texts)

    return sentence, labels



