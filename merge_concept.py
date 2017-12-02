def to_singular_concept(entity_list,lemmatizer_mashup):
    for i in range(0,len(entity_list)):
        for term in entity_list[i]:
            try:
                if term.count(' ')==1:
                    first_term,second_term=term.split(' ')
                    lemmatizer_mashup[i].remove(first_term)
                    lemmatizer_mashup[i].remove(second_term)

                    n_first_term=lemmatizer_mashup[i].count(first_term)
                    n_second_term=lemmatizer_mashup[i].count(second_term)
                    if (n_first_term == n_second_term) and n_first_term > 0:
                        for q in range(0,n_first_term):
                            lemmatizer_mashup[i].remove(first_term)
                            lemmatizer_mashup[i].remove(second_term)
                    for w in range(0,n_first_term+1):
                        lemmatizer_mashup[i].append(term)
                if term.count(' ')==2:
                    first_term,second_term,third_term=term.split(' ')
                    lemmatizer_mashup[i].remove(first_term)
                    lemmatizer_mashup[i].remove(second_term)
                    lemmatizer_mashup[i].remove(third_term)

                    n_first_term=lemmatizer_mashup[i].count(first_term)
                    n_second_term=lemmatizer_mashup[i].count(second_term)
                    n_third_term=lemmatizer_mashup[i].count(third_term)
                    if (n_first_term == n_second_term == n_third_term) and n_first_term > 0:
                        for q in range(0,n_first_term):
                            lemmatizer_mashup[i].remove(first_term)
                            lemmatizer_mashup[i].remove(second_term)
                            lemmatizer_mashup[i].remove(third_term)
                    for w in range(0,n_first_term+1):
                        lemmatizer_mashup[i].append(term)
            except:
                pass
    return lemmatizer_mashup

