import argparse
import pandas as pd
from sklearn.model_selection import train_test_split
import random
from utils import *
from classifiers import *
from preprocess import preprocess

seed = 42
random.seed(seed)
# experiment=1
preProcessedDataset = pd.DataFrame(columns=['Experiment', 'Coverage', 'F1_micro', 'F1_macro', 'F1_weighted', 'PCA'])


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input",
                        help="Input data in csv format", type=str)
    parser.add_argument("-v", "--voc_size",
                        help="Vocabulary size", type=int)
    parser.add_argument("-a", "--analyzer",
                        help="Tokenization level: {word, char}",
                        type=str, choices=['word', 'char'])
    return parser


if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()
    raw = pd.read_csv(args.input)

    # experiments = [
    #     {"remove_symbols_and_numbers": True, "tokenization": True, "stemming": True, "split_sentences": True},
    #     {"remove_symbols_and_numbers": True, "tokenization": True, "stemming": False, "split_sentences": True},
    #     {"remove_symbols_and_numbers": True, "tokenization": True, "stemming": True, "split_sentences": False},
    #     {"remove_symbols_and_numbers": True, "tokenization": True, "stemming": False, "split_sentences": False},
    #     {"remove_symbols_and_numbers": False, "tokenization": True, "stemming": True, "split_sentences": True},
    #     {"remove_symbols_and_numbers": False, "tokenization": True, "stemming": False, "split_sentences": True},
    #     {"remove_symbols_and_numbers": False, "tokenization": True, "stemming": True, "split_sentences": False},
    #     {"remove_symbols_and_numbers": False, "tokenization": True, "stemming": False, "split_sentences": False},
    #     {"remove_symbols_and_numbers": True, "tokenization": False, "stemming": False, "split_sentences": True},
    #     {"remove_symbols_and_numbers": True, "tokenization": False, "stemming": False, "split_sentences": False},
    #     {"remove_symbols_and_numbers": False, "tokenization": False, "stemming": False, "split_sentences": True}
    #
    # ]

    experiments = [{"remove_symbols_and_numbers": True, "tokenization": True, "stemming": True, "split_sentences": True}]

    for i, exp_param in enumerate(experiments):
        experiment = i + 1
        print("EXPERIMENT: " + str(experiment))

        # Languages
        languages = set(raw['language'])
        print('========')
        print('Languages', languages)
        print('========')

        # Split Train and Test sets
        X = raw['Text']
        y = raw['language']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=seed)

        print('========')
        print('Split sizes:')
        print('Train:', len(X_train))
        print('Test:', len(X_test))
        print('========')

        # Preprocess text (Word granularity only)
        if args.analyzer == 'word':
            X_train, y_train = preprocess(X_train, y_train, exp_param)
            X_test, y_test = preprocess(X_test, y_test, exp_param)

        # Compute text features
        features, X_train_raw, X_test_raw = compute_features(X_train,
                                                             X_test,
                                                             analyzer=args.analyzer,
                                                             max_features=args.voc_size)

        print('========')
        print('Number of tokens in the vocabulary:', len(features))
        coverage = compute_coverage(features, X_test.values, analyzer=args.analyzer)
        print('Coverage: ', str(coverage))
        print('========')

        # Apply Classifier
        X_train, X_test = normalizeData(X_train_raw, X_test_raw)
        y_predict = applyNaiveBayes(X_train, y_train, X_test)
        # y_predict = applySVC(X_train, y_train, X_test)

        print('========')
        print('Prediction Results:')
        f1_micro, f1_macro, f1_weighted = plot_F_Scores(y_test, y_predict)
        print('========')

        plot_Confusion_Matrix(y_test, y_predict, experiment, "Greens")

        # Plot PCA
        print('========')
        print('PCA and Explained Variance:')
        explainedVariance = plotPCA(X_train, X_test, y_test, languages, experiment)
        print('========')

        row_data = {'Experiment': str(experiment), 'Coverage': str(coverage), 'F1_micro': f1_micro,
                    'F1_macro': f1_macro, 'F1_weighted': f1_weighted, 'PCA': str(explainedVariance)}
        preProcessedDataset = pd.concat([preProcessedDataset, pd.DataFrame([row_data])], ignore_index=True)

    preProcessedDataset.to_csv(OUTPUT_ROUTE + 'preprocessedDataset.csv', encoding='utf-8', index=False)
