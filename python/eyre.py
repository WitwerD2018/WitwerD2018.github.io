# there is a package called nltk. load it for this file.
import nltk

def open_file_and_get_text(filename):
# given a filenam, open it.
    with open(filename, 'r') as our_file:
    # takes the file and reads the text.  Stores it.
        text = our_file.read()
    return text

def clean_tokens(words):
    clean_words = []
    for word in words:
    # given some tokens lower case them
# set a variable filename for where our file is.
        clean_words.append(word.lower())
    return clean_words
#print out first 30 words of clean list

filename = "eyre.txt"


text = open_file_and_get_text(filename)

# take a long string and break it into words.
words = nltk.word_tokenize(text)


clean_words = clean_tokens(words)
# loop over every word in the word list

    # make each word lower case and appends it in a new list

    #print out first 30 words of clean list
print(clean_words[0:30])
word_counts = nltk.FreqDist(clean_words)
print(word_counts['Jane'])
nltk.Text(clean_words).dispersion_plot(['he', 'she', 'jane', 'tony'])
