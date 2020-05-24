import nltk_test

key_words = nltk_test.cal_key_words()
texts=[]
with open('e:\\nlp\\highlight\\project\\data\\word2vec.html','r',encoding='utf-8') as f:
    line = f.readline( )
    while line:
        line=f.readline()
        texts.append(line)
        #print(line)

def replace_html_tag(text, word):
    print('begin replace:',text,word)
    #new_word = '<font color="red">' + word + '</font>'
    new_word = "<ba style = 'background:yellow'>" + word + "</ba>"
    len_w = len(word)
    len_t = len(text)

    for i in range(len_t - len_w, -1, -1):
        replace_it = False  # if the word is not inside the tag
        if text[i: i + len_w].lower() == word:
            print(text)
            print('found',word)
            for j in range(50):
                if text[i + j:i + j + 1] == '>':
                    replace_it = False
                    break
                if text[i+j:i+j+1] == '<':
                    # inside the tag, don't replace
                    replace_it = True
                    break
            if replace_it == True:
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
div_id = 'div id'
starter = 'page-container'
filter = False
result_title= 'result'
ls_of_ls = []
index = 0
for text in texts:
    if starter in text and div_id in text:
        print('start now:',text)
        filter = True
    if filter:
        for key_word in key_words:
            print(index,key_word,text)
            text = replace_html_tag(text, key_word)
    ls_of_ls.append(text)
save_html(ls_of_ls, result_title)
