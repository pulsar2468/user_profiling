####################################
#file_name: similarity.py          #
#author: Riccardo La Grassa        #
#data created: 16/11/2016          #
#data last modified:               #
#Python interpreter: 3.5.2         #
#mail: riccardo2468@gmail.com      #
####################################

import math

# it computes the similarity with vector model
#input: doc weighted 1 doc weighted 2 and the doc 2 aligned(for compute the scalar product)
#output:similarity of the vector model
def sim_vectorial(doc_w1,doc_align_2,doc_w2):
    scalar_product=0.0
    lenght_norm2=0.0
    lenght_norm1=0.0
    for i in zip(doc_w1,doc_align_2):
        scalar_product= scalar_product + i[0]*i[1]

    for i in doc_w1:
        lenght_norm1=lenght_norm1 + math.pow(i,2)

    for a in doc_w2:
        lenght_norm2 = lenght_norm2 + math.pow(a,2)


    if scalar_product == 0: return 0 #totally different
    else:
        return (scalar_product/((math.sqrt(lenght_norm1)) * (math.sqrt(lenght_norm2))))

#it computes the weighting scheme (tf-idf) of all list
# and it aligns the terms of the second list with the first list ( if it exist, otherwise it puts 0)
# in this way, i don't consider another structure for the words set
#input:list target X and Y
#output: doc weighted 1, doc weighted 2, doc aligned 2 seeing the first
def tf_idf(list1,list2):
    doc_mix_=[]
    gold=[]
    temp=[]
    temp_repl=[]
    not_replicated=[]
    fusion_list=[]
    fusion_list.append(list1)
    fusion_list.append(list2) #lista1 U lista2
    #frequency for each term  in doc j
    for i in range(0,len(fusion_list)):
        #set_clean_list=set(fusion_list[i]) #i create a set for each account twitter
        for j in (fusion_list[i]): # for each word of doc(set) count the occurrences inside the doc
            if not j in temp_repl: #i don't consider the same words
                temp_repl.append(j)
                #tf
                n_i=1 #of course
                fr_i=fusion_list[i].count(j)


                #idf
                if any(j in item for item in fusion_list[1-i]):
                    n_i=n_i + 1

                w= ((1 + math.log10(fr_i))) * (math.log10((1+2 / n_i))) #tf-idf
                temp.append(w)

        doc_mix_.append([w for w in temp]) #first list -> doc weight 1 second list -> doc weight 2
        temp.clear()
        not_replicated.append([w for w in temp_repl])
        temp_repl.clear()



    #Finally, i won.. Fortunately i come from C
    for item in not_replicated[0]:
        if item in not_replicated[1]:
            gold.append(doc_mix_[1][not_replicated[1].index(item)])
        else:
            gold.append(0)
    return doc_mix_[0],gold,doc_mix_[1] #this is too importat, see an explanation!




