from nltk.stem import WordNetLemmatizer

def lemmatizer_words(clean_mashup):
    wordnet_lemmatizer = WordNetLemmatizer()
    list_lemmatizer=[]
    tmp=[]
    for article in clean_mashup:
        for term in article:
            tmp.append(wordnet_lemmatizer.lemmatize(term,'v'))
        list_lemmatizer.append(tmp.copy())
        tmp.clear()
    return list_lemmatizer
