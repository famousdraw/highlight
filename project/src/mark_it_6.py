import nltk_test

key_words=nltk_test.cal_key_words()
texts=[]
with open('e:\\nlp\\highlight\\project\\data\\1801.06146.html','r',encoding='utf-8') as f:
    line = f.readline( )
    while line:
        line=f.readline()
        texts.append(line)
        #print(line)

def replace_html_tag(text, word):
    new_word = '<font color="red">' + word + '</font>'
    len_w = len(word)
    len_t = len(text)
    for i in range(len_t - len_w, -1, -1):
        if text[i: i + len_w] == word:
            print('found',word)
            text = text[:i] + new_word + text[i + len_w:]
    return text


def save_html(ls_of_ls, prefix):
    fname = prefix + '.html'
    with open(fname, 'w', encoding='utf-8') as f:
        for ls in ls_of_ls:
            #print(ls)
            f.write(''.join(ls))
            #for i in ls:
            #    f.write('<td><font size="4">{}</font></td>'.format(i))
            #f.write('</tr>\n')
        #f.write('</table></body></html>')


word = 'Fine'
word2 = 'tuning'
result_title= word
ls_of_ls = []
for text in texts:
    print(text)
    text=replace_html_tag(text, word)
    text = replace_html_tag(text, word2)
    ls_of_ls.append(text)
save_html(ls_of_ls, result_title)
