import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import pandas as pd
import re
# nltk.download('punkt')
from nltk.tokenize import PunktSentenceTokenizer



def preprocess(sentence, labels, experiment):
    '''
    Task: Given a sentence apply all the required preprocessing steps
    to compute train our classifier, such as sentence splitting,
    tokenization or sentence splitting.

    Input: Sentence in string format
    Output: Preprocessed sentence either as a list or a string
    '''

    stemmer = PorterStemmer()
    preprocessed_texts = []
    for text in sentence:
        if experiment == 1:
            #EXPERIMENT 1: Symbols and numbers removal & Tokenize sentence & Word Tokenize & Stemming
            # REMOVE SYMBOLS AND NUMBERS
            text = re.sub(r'[!@#$(),n"%^*?:;~`0-9]', ' ', text)
            text = re.sub(r'[[]]', ' ', text)

            # TOKENIZE
            #Tokenize into sentences
            tokenizer = PunktSentenceTokenizer()
            sentences = tokenizer.tokenize(text)
            # Tokenize each sentence into words using word_tokenize
            tokens = []
            for sentence in sentences:
                tokens = nltk.word_tokenize(sentence, preserve_line=True)

            #STEMMING
            tokens = [stemmer.stem(token) for token in tokens]

            preprocessed_text = " ".join(tokens)
            preprocessed_texts.append(preprocessed_text)

        elif experiment == 2:
            #EXPERIMENT 2: Symbols and numbers removal & Tokenize sentence & Word Tokenize
            # REMOVE SYMBOLS AND NUMBERS
            text = re.sub(r'[!@#$(),n"%^*?:;~`0-9]', ' ', text)
            text = re.sub(r'[[]]', ' ', text)

            # TOKENIZE
            # Tokenize into sentences
            tokenizer = PunktSentenceTokenizer()
            sentences = tokenizer.tokenize(text)
            # Tokenize each sentence into words using word_tokenize
            tokens = []
            for sentence in sentences:
                tokens = nltk.word_tokenize(sentence, preserve_line=True)

            preprocessed_text = " ".join(tokens)
            preprocessed_texts.append(preprocessed_text)

        elif experiment == 3:
            #EXPERIMENT 3: Symbols and numbers removal & Word Tokenize & Stemming
            # REMOVE SYMBOLS AND NUMBERS
            text = re.sub(r'[!@#$(),n"%^*?:;~`0-9]', ' ', text)
            text = re.sub(r'[[]]', ' ', text)

            # TOKENIZE
            # Tokenize into words using word_tokenize
            tokens = nltk.word_tokenize(text, preserve_line=True)

            # STEMMING
            tokens = [stemmer.stem(token) for token in tokens]

            preprocessed_text = " ".join(tokens)
            preprocessed_texts.append(preprocessed_text)

        elif experiment==4:
            #EXPERIMENT 4: Symbols and numbers removal & Word Tokenize
            # REMOVE SYMBOLS AND NUMBERS
            text = re.sub(r'[!@#$(),n"%^*?:;~`0-9]', ' ', text)
            text = re.sub(r'[[]]', ' ', text)

            # TOKENIZE
            tokens = nltk.word_tokenize(text, preserve_line=True)

            preprocessed_text = " ".join(tokens)
            preprocessed_texts.append(preprocessed_text)

        elif experiment==5:
            #EXPERIMENT 5: Tokenize sentence & Word Tokenize & Stemming
            # TOKENIZE
            # Tokenize into sentences
            tokenizer = PunktSentenceTokenizer()
            sentences = tokenizer.tokenize(text)
            # Tokenize each sentence into words using word_tokenize
            tokens = []
            for sentence in sentences:
                tokens = nltk.word_tokenize(sentence, preserve_line=True)

            # STEMMING
            tokens = [stemmer.stem(token) for token in tokens]

            preprocessed_text = " ".join(tokens)
            preprocessed_texts.append(preprocessed_text)

        elif experiment==6:
            #EXPERIMENT 6: Tokenize sentence & Word Tokenize
            # TOKENIZE
            # Tokenize into sentences
            tokenizer = PunktSentenceTokenizer()
            sentences = tokenizer.tokenize(text)
            # Tokenize each sentence into words using word_tokenize
            tokens = []
            for sentence in sentences:
                tokens = nltk.word_tokenize(sentence, preserve_line=True)

            preprocessed_text = " ".join(tokens)
            preprocessed_texts.append(preprocessed_text)

        elif experiment==7:
            #EXPERIMENT 7: Word Tokenize & Stemming
            # TOKENIZE
            tokens = nltk.word_tokenize(text, preserve_line=True)

            # STEMMING
            tokens = [stemmer.stem(token) for token in tokens]

            preprocessed_text = " ".join(tokens)
            preprocessed_texts.append(preprocessed_text)

        elif experiment==8:
            #EXPERIMENT 8: Word Tokenize
            # TOKENIZE
            tokens = nltk.word_tokenize(text, preserve_line=True)

            preprocessed_text = " ".join(tokens)
            preprocessed_texts.append(preprocessed_text)

        elif experiment==9:
            #EXPERIMENT 9: Symbols and numbers removal & Tokenize sentence
            # REMOVE SYMBOLS AND NUMBERS
            text = re.sub(r'[!@#$(),n"%^*?:;~`0-9]', ' ', text)
            text = re.sub(r'[[]]', ' ', text)

            # TOKENIZE
            # Tokenize into sentences
            tokenizer = PunktSentenceTokenizer()
            tokens = tokenizer.tokenize(text)

            preprocessed_text = " ".join(tokens)
            preprocessed_texts.append(preprocessed_text)

        elif experiment==10:
            #EXPERIMENT 10: Symbols and numbers removal
            # REMOVE SYMBOLS AND NUMBERS
            text = re.sub(r'[!@#$(),n"%^*?:;~`0-9]', ' ', text)
            text = re.sub(r'[[]]', ' ', text)

            # preprocessed_text = " ".join(text)
            preprocessed_texts.append(text)

        elif experiment==11:
            #EXPERIMENT 11: Tokenize sentence
            # TOKENIZE
            # Tokenize into sentences
            tokenizer = PunktSentenceTokenizer()
            tokens = tokenizer.tokenize(text)

            preprocessed_text = " ".join(tokens)
            preprocessed_texts.append(preprocessed_text)
        else:
            print("EXPERIMENT NUMBER IS WRONG")

    # Convert preprocessed texts list to pandas Series
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

