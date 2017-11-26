import urllib.request
from bs4 import BeautifulSoup
import re

list_titles=[]

#specify the url
wiki = "http://feeds.bbci.co.uk/news/world/rss.xml"
page = urllib.request.urlopen(wiki)
soup = BeautifulSoup(page,"html5lib")
for item in soup.find_all("item"):
    head=re.sub("<!\[CDATA\[",'',item.title.string)
    queue=re.sub("]]>$",'',head)
    #stop word!
    print(queue)
    #list_titles.append(item.title.string)

