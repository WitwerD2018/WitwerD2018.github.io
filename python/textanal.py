from bs4 import BeautifulSoup
from urllib import request

url = "https://raw.githubusercontent.com/humanitiesprogramming/scraping-corpus/master/full-text.txt"
html = request.urlopen(url).read()
soup = BeautifulSoup(html, 'lxml')
raw_text = soup.text
texts = eval(soup.text)
print(len(raw_text))
print(len(texts))
import nltk
from nltk import word_tokenize
nltk.download()
tokenized_texts = []
for text in texts:
    tokenized_texts.append(word_tokenize(text))

for tokenized_text in tokenized_texts:
    print('=====')
    print(len(tokenized_text))
    print(tokenized_text[0:20])
doyle = tokenized_texts[:5]
bronte = tokenized_texts[5:]

print(len(doyle))
print(len(bronte))
def normalize(tokens):
    """Takes a list of tokens and returns a list of tokens
    that has been normalized by lowercasing all tokens and
    removing Project Gutenberg frontmatter."""

#     lowercase all words
    normalized = [token.lower() for token in tokens]

#     very rough end of front matter.
    end_of_front_matter = 90
#     very rough beginning of end matter.
    start_of_end_matter = -2973
#     get only the text between the end matter and front matter
    normalized = normalized[end_of_front_matter:start_of_end_matter]

    return normalized

print(normalize(bronte[0])[:200])
print(normalize(bronte[0])[-200:])
doyle = [normalize(text) for text in doyle]
bronte = [normalize(text) for text in bronte]

print(doyle[0][:30])
from nltk.corpus import stopwords

print(stopwords.words('english')[0:30])
