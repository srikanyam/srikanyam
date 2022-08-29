import requests
from bs4 import BeautifulSoup
import csv

req = requests.get(" https://www.authenticwatches.com/rolex-specials.html")
soup = BeautifulSoup(req.content, "html.parser")

print(soup.prettify)
print(soup.text)

#images
img1=[]
image=soup.findAll('div',class_="sm-img-wrap")
for i in image:
    j=i.img['src']
    print(j)
    img1.append(j)
print(img1)

#links
links=[]
link=soup.findAll('div',class_="sm-overlay")
for i in link:
    j=i.a.text
    j=i.a['href']
    links.append(j)
    print(links)
