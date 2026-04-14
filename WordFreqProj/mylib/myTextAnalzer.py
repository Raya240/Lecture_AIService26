import pandas as pd

def load_corpus_from_csv(data_filename, column):
    data_df = pd.read_csv(data_filename)
    corpus = list(data_df[column])    
    if data_df[column].isnull().sum():
        data_df.dropna(subset=[column], inplace=True)

    return corpus


def tokenize_korean_corpus(corpus, tokenizer, my_tags=None, my_stopwords=None):
    all_tokens = []
    if my_tags:
        #print('enter my_tags')
        for text in corpus:
            tokens = [word for word, tag in tokenizer(text) if tag in my_tags and word not in my_stopwords]
            all_tokens += tokens
    else: 
        #print('enter no my_tags')
        for text in corpus:
            tokens = [word for word, tag in tokenizer(text) if word not in my_stopwords]
            all_tokens += tokens
            _
    return all_tokens

from collections import Counter

def analyze_word_freq(tokens):
    return Counter(tokens)

def visualize_barhgraph(counter, num_words, title, xlabel, ylabel, font_path=None):
    # 고빈도 단어 num_words만큼 추출

    # x 데이터와 y 데이터 분리
    print('test')
    #
