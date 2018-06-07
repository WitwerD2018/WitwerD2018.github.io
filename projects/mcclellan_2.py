import nltk

our_file = "mcclellan.txt"

def open_file_and_get_text(our_file):
# given a filenam, open it.
    with open(our_file, 'r') as fn:
    # takes the file and reads the text.  Stores it.
        text = fn.read()
    return text

def clean_tokens(words):
    clean_words = []
    for word in words:
    # given some tokens lower case them
# set a variable our_file for where our file is.
        clean_words.append(word.lower())
    return clean_words
#print out first 30 words of clean list

text = open_file_and_get_text(our_file)
# take a long string and break it into words.
words = nltk.word_tokenize(text)
clean_words = clean_tokens(words)
# loop over every word in the word list

# make each word lower case and appends it in a new list

#word_counts = nltk.FreqDist(clean_words)
#print(word_counts['racketeer*'])
nltk.Text(clean_words).dispersion_plot(['beck', 'portland', 'labor', 'brewster'])
