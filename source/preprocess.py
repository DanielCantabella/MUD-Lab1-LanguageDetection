import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pandas as pd
import re
# nltk.download('punkt')
from nltk.tokenize import PunktSentenceTokenizer

def remove_symbols_and_numbers(text):
    text = re.sub(r'[!@#$(),n"%^*?:;~`0-9]', ' ', text)
    text = re.sub(r'[[]]', ' ', text)
    return text

def tokenization(text):
    output = nltk.word_tokenize(text, preserve_line=True)
    return output

def stemming( tokens):
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(token) for token in tokens]
    return tokens

def split_sentences(sentences, labels):

    tokenized_list = [nltk.sent_tokenize(text) for text in sentences]
    post_sentences = []
    post_labels = []
    for sent_list, label in zip(tokenized_list, labels):
        for sentence in sent_list:
            post_sentences.append(sentence)
            post_labels.append(label)
    post_labels = pd.Series(post_labels)

    return post_sentences, post_labels

def preprocess(sentence, labels, exp_param):
    '''
    Task: Given a sentence apply all the required preprocessing steps
    to compute train our classifier, such as sentence splitting,
    tokenization or sentence splitting.

    Input: Sentence in string format
    Output: Preprocessed sentence either as a list or a string
    '''

    if exp_param["split_sentences"]:
        sentence, labels = split_sentences(sentence, labels)

    preprocessed_texts = []
    for text in sentence:
        text = text.lower()
        if exp_param["remove_symbols_and_numbers"]:
            text = remove_symbols_and_numbers(text)

        if exp_param["tokenization"]:
            text = tokenization(text)
            if exp_param["stemming"]:
                text = stemming(text)
            text = " ".join(text)
        preprocessed_texts.append(text)

    sentence = pd.Series(preprocessed_texts)

    return sentence, labels



# # import MeCab
# import jieba
# from indicnlp.tokenize import indic_tokenize
# from indicnlp.tokenize import sentence_tokenize

# EXTRA TOKENIZATIONS:
        # tokens = jieba.lcut(text)  # Jieba: Chinese
        # tokens = indic_tokenize.trivial_tokenize(text) #Indic: Hindi, Tamil, Urdu
        # tokens = sentence_tokenize.sentence_split(text, lang='hi')  # Indic: Hindi, Tamil, Urdu
        ## tokens = MeCab.Tagger("-Owakati").parse(text).split()# MeCab: Japanese and Korean.

