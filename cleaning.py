import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
tokenizer = RegexpTokenizer(r'\w+')
new_words =["get","go","quot","going, got"]

def remove_mention(text):
    text_split = text.split(" ")
    new_text = ""
    for i in text_split:
        #print(i)
        if "@" not in i:
            new_text += i + " "
    #print(new_text)
    return new_text[0:len(new_text)-1]


def tokenize(text):
    text = remove_mention(text)
    words = tokenizer.tokenize(text.lower())
    filtered = []
    for i in words:
        if not i in stopwords.words():
            filtered.append(i)
    for j in range(len(filtered)):
        filtered[j] = lemmatizer.lemmatize(filtered[j])
    return filtered