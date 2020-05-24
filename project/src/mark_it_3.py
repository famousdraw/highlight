#mysql高亮查询
def highlight(self, field, table, keyword, n=99):
    sql = "SELECT %s FROM %s WHERE INSTR(%s,'%s')>0;" % (field, table, field, keyword)
    for i in self.fetchone(sql, n):
        text = i[0]
        highlight_word = '\033[031m' + keyword + '\033[0m'  # red
        len_w = len(keyword)
        len_t = len(text)
        for i in range(len_t - len_w, -1, -1):
            if text[i: i + len_w] == keyword:
                text = text[:i] + highlight_word + text[i + len_w:]
        print(text)


highlight()