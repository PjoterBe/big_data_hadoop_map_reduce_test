import re
#szuka chociaż 1 znaku z word character
WORD_RE = re.compile(r'[\w]+')#r to wyrazenie regularne, w to a-z,A-Z,0-1 i _,

words = WORD_RE.findall('Big data, hadoop and map reduce, (hell world!')
print(words)