# -*- encoding: utf-8 -*-
"""
test open idf file
"""
file_path='e:\\nlp\\highlight\\project\\data\\'
idf_file='idf_sample.txt'
new_idf_path=file_path+idf_file
print(new_idf_path)
content = open(new_idf_path, 'rb').read().decode('utf-8')
idf_freq = {}
for line in content.splitlines():
    word, freq = line.strip().split(' ')
    idf_freq[word] = float(freq)

for key,values in idf_freq.items():
    print(key,values)

median_idf = sorted(
    idf_freq.values( ))[len(idf_freq) // 2]

print('idf_freq.values()',idf_freq.values())
print('median_idf',median_idf)

#close(new_idf_path)