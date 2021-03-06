import urllib
from bs4 import BeautifulSoup
from pandas import json
import requests


def get_concepts(article):
    abstract_entity=[]
    name_entity=[]
    name_entity_string=[]
    abstract_entity_string=[]

    for i in range(0,len(article)):
        text= ' '.join(article[i])
        url = 'http://model.dbpedia-spotlight.org/en/annotate'
        #url = "http://localhost:2222/rest/annotate" #I hoped to this, but with few memory i cannot launch jar file
        data = {"text": text,"confidence":"0.5"}
        headers = {"Accept" : "application/json"}
        res = requests.get(url, params=data, headers=headers)
        j = json.loads((res.content).decode('utf-8'))
        if 'Resources' in j.keys():

            for i in range(0,len(j['Resources'])):
                try:
                    page = urllib.request.urlopen(j['Resources'][i]['@URI'])
                    soup = BeautifulSoup(page,"html5lib")
                    if j['Resources'][i]['@surfaceForm'] not in name_entity_string: #not consider duplicates
                        name_entity_string.append(j['Resources'][i]['@surfaceForm'])
                        abstract_entity_string.append(soup.find('p',{"class": "lead"}).string)
                except Exception as e:
                    print("Error: ", e.args)#i've a problem with some word (decoding problem) I'll see later
                    exit()
            name_entity.append(name_entity_string.copy())
            abstract_entity.append(abstract_entity_string.copy())
            abstract_entity_string.clear()
            name_entity_string.clear()
        else:
            name_entity.append([])
            abstract_entity.append([])
    return name_entity,abstract_entity