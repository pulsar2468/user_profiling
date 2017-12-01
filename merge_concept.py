def to_singular_concept(entity_list,lemmatizer_mashup):
    for i in range(0,len(entity_list)):
        for term in entity_list[i]:
                if ' ' in term:
                    first_term,second_term=term.split(' ')
                    lemmatizer_mashup[i].remove(first_term)
                    lemmatizer_mashup[i].remove(second_term)
                    lemmatizer_mashup[i].append(term)
    return lemmatizer_mashup

