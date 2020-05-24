texts=[]
with open('e:\\nlp\\highlight\\project\\data\\1801.06146.html','r',encoding='utf-8') as f:
    line = f.readline( )
    while line:
        line=f.readline()
        texts.append(line)
        print(line)

def replace_html_tag(text, word):
    new_word = '<font color="red">' + word + '</font>'
    len_w = len(word)
    len_t = len(text)
    for i in range(len_t - len_w, -1, -1):
        if text[i: i + len_w] == word:
            text = text[:i] + new_word + text[i + len_w:]
    return text


def save_html(ls_of_ls, prefix):
    fname = prefix + '.html'
    with open(fname, 'w', encoding='utf-8') as f:
        f.write('<html><head><meta charset="UTF-8"></head><body><table border="1">\n')
        for ls in ls_of_ls:
            f.write('<tr>')
            for i in ls:
                f.write('<td><font size="4">{}</font></td>'.format(i))
            f.write('</tr>\n')
        f.write('</table></body></html>')


#texts = ['比赛开始没多久就结束了比赛', '，现在没有比赛', '到底什么时候会有比赛', '这个比赛对于运动员来说很重要']
word = 'tuning'

ls_of_ls = []
for text in texts:
    ls_of_ls.append([word, replace_html_tag(text, word)])
save_html(ls_of_ls, word)
