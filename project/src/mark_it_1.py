w = '比赛'
t = '比赛开始没多久就结束了比赛，现在没有比赛'

def replace_color(text, word):
    new_word = '\033[031m' + word + '\033[0m'  # red
    len_w = len(word)
    len_t = len(text)
    for i in range(len_t - len_w, -1, -1):
        if text[i: i + len_w] == word:
            text = text[:i] + new_word + text[i + len_w:]
    return text

print(t)
print(replace_color(t, w))

