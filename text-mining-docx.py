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


#lowercase
text = cleaned
lower_text = text.lower()


#Tokenize words
from nltk.tokenize import word_tokenize
tokenized_word = word_tokenize(lower_text)


tokenized_word = [word for word in tokenized_word if word.isalpha()]

#remove stop words
from nltk.corpus import stopwords
stop_words=set(stopwords.words("english"))


qep = [word for word in tokenized_word if word not in stop_words]

#identify ngrams
from nltk.util import ngrams
esBigrams = ngrams(qep, 1)
esBigramFreq = collections.Counter(esBigrams)

#results
results = esBigramFreq.most_common(100)
for y in results:
    print(y)

# Python3 Scriptname > results.csv


