import requests
from bs4 import BeautifulSoup
import json,re

class Info():
    Channel= []
    Links = []
    Name = []
    

def search():
    searchh = input("what you wanna search: ")
    query = str(searchh.replace(" ","+"))

    response = requests.get(f"https://www.youtube.com/results?search_query={query}").text


    soup =BeautifulSoup(response,'lxml')
    scripts = soup.findAll("script")
    json_text=re.search("var ytInitialData = (.+)[,:]{1}",str(scripts)).group(1)
    endpoint = json_text.find(";")
    json_text = json_text[:endpoint]

    json_data = json.loads(json_text)

    content = (
        json_data
        ['contents']['twoColumnSearchResultsRenderer']
        ['primaryContents']['sectionListRenderer']
        ['contents'][0]['itemSectionRenderer']
        ['contents']
    )

    try:
        for data in content:
            for key,value in data.items():

                for k,v in value.items():
                    if k == "videoId":
                        print(v + "\n")
                    
                    if k == "title" :
                        print(v['runs' ][0]['text'] +'\n')

                    
                    if k=="thumbnail" or k=="thumbnails":
                        print(v["thumbnails"][0]["url"]+'\n')
                
    except:
        print(" ")

search()
