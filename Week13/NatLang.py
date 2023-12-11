from nltk.tokenize import sent_tokenize, word_tokenize
about = "the quick brown fox jumps over the lazy dog. This is the next sentence, which is fairly cool, right?"
tokenized = word_tokenize(about)

stop_words = set(stopwords.words("english"))
filteredList = []

for word in tokenized:
    if word.casefold() not in stop_words:
        filteredList.append(word)

filteredList = [word for word in tokenized if word.casefold()]

print(filteredList)