#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import nltk
import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


# 导入文章到list
def Insert_text():
    L = []
    with open('e:\\nlp\\highlight\\project\\data\\word2vec.html.txt', 'r',encoding='utf-8') as f:
        L.append(f.read())
    return L


# 将text中的标点符号和数字过滤
# 第二次过滤合并多个空格
def Filter_text(text):
    str = re.sub('[^a-zA-Z]', ' ', text)
    return re.sub(r'\s+', ' ', str)


# 将大写转化为小写
def Lower_text(text):
    return text.lower()


# 使用WordNetLemmatizer类，即wordnet词形还原方法
def Lemmatization_text(text_cut_list):
    wnl = WordNetLemmatizer()
    return [wnl.lemmatize(n) for n in text_cut_list]


# 将article中的文章转化成由单词构成的list
def text_cut(text):
    return re.findall('[a-zA-z]+', text)


# 过滤停用词以及长度小于3的词
def Stopwords_text(text_cut_list):
    Stop_Word_list = stopwords.words("english")
    return [n for n in text_cut_list if n not in Stop_Word_list and len(n) >= 3]


# 计算TF-IDF
def TF_IDF_count(text):
    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(vectorizer.fit_transform(text))
    word = vectorizer.get_feature_names()  # 所有文本的关键字
    weight = tfidf.toarray()  # 对应的tfidf矩阵
    return [(word[j], float(weight[0][j])) for j in range(len(word))]


def cal_key_words():
    article = Insert_text()
    article[0] = Filter_text(article[0])
    article[0] = Lower_text(article[0])
    word_cut = Lemmatization_text(text_cut(article[0]))
    word_cut = Stopwords_text(word_cut)
    # print(Stopwords_text(word_cut))
    article[0] = ''
    for w in word_cut:
        article[0] = article[0] + w + ' '
    L = TF_IDF_count(article)
    print(sorted(L, key=lambda x: (x[1]), reverse=True))
    sorted_L=sorted(L, key=lambda x: (x[1]), reverse=True)
    i=0
    key_words=[]
    for word,index in sorted_L:
        i+=1
        if i<20:
            key_words.append(word)
            #print(word,index)
            print(word)
    return key_words

if __name__== "__main__":
    print('test')
    cal_key_words()