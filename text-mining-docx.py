import os
import zipfile
import re
import xml.dom.minidom
import nltk
import string
import collections



#cleaned up doc file
docx = zipfile.ZipFile('Focus Group II.docx')
content = docx.read('word/document.xml').decode('utf-8')
cleaned = re.sub('<(.|\n)*?>','',content)
print(cleaned)

#lowercase
text = cleaned
lower_text = text.lower()
print(lower_text)

#Tokenize words
from nltk.tokenize import word_tokenize
tokenized_word = word_tokenize(lower_text)
print(tokenized_word)

#remove stop words
from nltk.corpus import stopwords
stop_words=set(stopwords.words("english"))
print(stop_words)

qep = [word for word in tokenized_word if word not in stop_words]

#identify ngrams
from nltk.util import ngrams
esBigrams = ngrams(qep, 1)
esBigramFreq = collections.Counter(esBigrams)

#results
results = esBigramFreq.most_common(100)
print(results)

