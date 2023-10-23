import requests
from bs4 import BeautifulSoup
import pprint
import re
import yaml

URL = "https://www.cs.ubc.ca/group/infovis/publications.shtml"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

pubs = soup.find_all(class_="pub-one-column")

print(len(pubs))

pubObjs = []

for pub in pubs:
    pubObj = {}
    if pub.find(class_="title") and pub.find(class_="title").find("a") and pub.find(class_="title").find("a")["href"]:
        pubObj["link"] = pub.find(class_="title").find("a")["href"]
        if pubObj["link"].startswith("http://www.cs.ubc.ca/group/infovis/"):
            pubObj["link"] = pubObj["link"][len("http://www.cs.ubc.ca/group/infovis/"):]
        elif pubObj["link"].startswith("https://www.cs.ubc.ca/group/infovis/"):
            pubObj["link"] = pubObj["link"][len("https://www.cs.ubc.ca/group/infovis/"):]
        elif pubObj["link"].startswith("/~") or pubObj["link"].startswith("/labs/"):
            pubObj["link"] = "http://www.cs.ubc.ca" + pubObj["link"]

    if pub.find(class_="thumb") and pub.find(class_="thumb").find("img") and pub.find(class_="thumb").find("img")["src"]:
        pubObj["image"] = pub.find(class_="thumb").find("img")["src"]
        if pubObj["image"].startswith("http://www.cs.ubc.ca/group/infovis/"):
            pubObj["image"] =  pubObj["image"][len("http://www.cs.ubc.ca/group/infovis/"):]
        elif pubObj["image"].startswith("https://www.cs.ubc.ca/group/infovis/"):
            pubObj["image"] = pubObj["image"][len("https://www.cs.ubc.ca/group/infovis/"):]
        elif pubObj["image"].startswith("/~") or pubObj["image"].startswith("/labs/"):
            pubObj["image"] = "http://www.cs.ubc.ca" + pubObj["image"]
        elif pubObj["image"].startswith("/images/") or pubObj["image"].startswith("images/"):
            pubObj["image"] = "/assets/" + pubObj["image"]
        
    if pub.find(class_="title") and pub.find(class_="title").find("a") and pub.find(class_="title").find("a").text:
        pubObj["title"] = pub.find(class_="title").find("a").text
        pubObj["title"] = pubObj["title"].replace("\n", "")
        pubObj["title"] = ' '.join(pubObj["title"].split())
    
    if pub.find(class_="authors") and pub.find(class_="authors").find_all("a"):
        authors = pub.find(class_="authors").text.replace("\n", "")
        authors = ' '.join(authors.split())
        authors = authors.split(".")[0]
        authorsObj = []
        for author in re.split(',| and ', authors):
            author = author.strip()
            if author == "":
                continue
            authorObj = { "name": author }
            for authorLink in pub.find(class_="authors").find_all("a"):
                if authorLink.text == author:
                    authorObj["link"] = authorLink["href"]
                    if authorObj["link"].startswith("/~") or authorObj["link"].startswith("/labs/"):
                        authorObj["link"] = "http://www.cs.ubc.ca" + authorObj["link"]
            authorsObj += [authorObj]
        pubObj["authors"] = authorsObj

    if pub.find(class_="venue"):
        if pub.find(class_="venue").find(class_="name"):
            pubObj["venue"] = pub.find(class_="venue").find(class_="name").text
        else: 
            pubObj["venue"] = pub.find(class_="venue").text
        pubObj["venue"] = pubObj["venue"].replace("\n", "")
        pubObj["venue"] = ' '.join(pubObj["venue"].split())

    if pub.find(class_="abstract"):
        pubObj["abstract"] = pub.find(class_="abstract").text
        pubObj["abstract"] = pubObj["abstract"].replace("\n", "")
        pubObj["abstract"] = ' '.join(pubObj["abstract"].split())
    
    if pub.find(class_="links") and pub.find(class_="links").find_all("a"):
        linksObj = []
        for link in pub.find(class_="links") and pub.find(class_="links").find_all("a"):
            linkObj = {
                "name": link.text,
                "link": link["href"]
            }
            linksObj += [linkObj]
        pubObj["links"] = linksObj

    pubObjs += [pubObj]

pprint.pprint(pubObjs)

with open('publications.yml', 'w') as outfile:
    yaml.dump(pubObjs, outfile, default_flow_style=False)