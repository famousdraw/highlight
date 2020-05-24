
#单个高亮
from jieba import tokenize

text = '我用小米手机订购了一袋小米'
entity = '小米'

replace_color = lambda word: '\033[033m' + word + '\033[0m'
replace_word = lambda sentence, word, head, tail: sentence[:head] + word + sentence[tail:]

for word, head, tail in tokenize(text):
    if word == entity:
        word = replace_color(word)
        print(replace_word(text, word, head, tail))
