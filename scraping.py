import urllib.request
from bs4 import BeautifulSoup
import re,time
import word_netV2
import lemmatizer_content
import vector_model

def clean_text(original_list):
    list_splitted=[]
    list_clean=[]
    for i in original_list:
        list_splitted.append(i.split())

    #grammar file. i will erase all the useless words
    grammarlist=[]
    clean_title=[]
    try:
        with open('grammarList', 'r') as f:
            grammarlist.append(f.read().splitlines())

    except IOError:
        print('file not found!')
        exit()

    for i in range(0, len(list_splitted)):
        for j in range(0, len(list_splitted[i])):
            if not re.search('https?|RT|href=|class=|src=|align=|border=|height=|width=|alt=|<p>|reading', list_splitted[i][j]):
                list_splitted[i][j]=re.sub('<!\[CDATA\[|]]>|\[CDATA\[|]|•|‘|\'|"|”|!|“|,|:|&|;|/|\+|\?|…|[.]+|-|–|—|→|\(|\)|<p>|<a>|<a|<div', '', list_splitted[i][j]) #i clean the text from link replytweet and @tag
                if not (len(list_splitted[i][j]) < 3 ):
                    if not (any(list_splitted[i][j].lower() in s for s in grammarlist)):
                        clean_title.append(list_splitted[i][j].lower())
        list_clean.append([i for i in clean_title])
        clean_title.clear()
    f.close()
    return list_clean



fake_title=[]
list_mashup=[]
fake_title.append(input("Please insert title+content Fake news"))

list_titles=[]
list_url=[]
list_description=[]
similarity_vectorialList=[]
lemmatizer_mashup=[]
#specify the url
count=0
#bbc,#other famous #the guardian #the wall street journal #new york times
url=["http://feeds.bbci.co.uk/news/world/rss.xml", \
     "http://feeds.reuters.com/Reuters/worldNews", \
     "https://www.theguardian.com/international/rss", \
     "http://www.wsj.com/xml/rss/3_7085.xml",\
     "http://rss.nytimes.com/services/xml/rss/nyt/World.xml"]
for i in url:
    try:
        page = urllib.request.urlopen(i)
    except Exception as e:
        print("Error: ",e)
        exit()

    soup = BeautifulSoup(page,"html5lib")
    for item in soup.find_all("item"):
        list_titles.append(item.title.string)
        list_description.append(item.description.string)
        list_mashup.append(item.title.string+item.description.string)
        list_url.append(item.link.next_sibling)

    #stop word!
    #clean_list_safe=clean_text(list_titles)
    #clean_description=clean_text(list_description)
    clean_title_fake=clean_text(fake_title)
    clean_mashup=clean_text(list_mashup)
    #lemmatizator of data-clean
    lemmatizer_mashup=lemmatizer_content.lemmatizer_words(clean_mashup)
    lemmatizer_fake=lemmatizer_content.lemmatizer_fake_news(clean_title_fake[0])

    #tf-idf with only title (fake news,title safe page)...
    for item in lemmatizer_mashup:
        start = time.time()
        doc_weight1,doc_align_2,doc_weight2=word_netV2.tf_idf(item,lemmatizer_fake)
        similarity_vectorialList.append(word_netV2.sim_vectorial(doc_weight1,doc_align_2,doc_weight2))
        time_vector_model=time.time()-start

    winner_take_all=max(similarity_vectorialList)

    if (winner_take_all>0.1):
        index_winner=similarity_vectorialList.index(max(similarity_vectorialList))
        print("Best similarity into: ",i,"\nSim= ",winner_take_all,"\nSafe news: ",lemmatizer_mashup[index_winner],"\nTitle fake news: ",lemmatizer_fake,"\nUrl: ",list_url[index_winner])
        count=count+1
    #Clear all lists
    similarity_vectorialList.clear()
    list_mashup.clear()
    list_description.clear()
    list_titles.clear()
    list_url.clear()
print("Set safe page:",len(url),"\nStronger similarity to",count,"safe page")