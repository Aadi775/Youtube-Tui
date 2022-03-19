import requests
from bs4 import BeautifulSoup
import json,re

class Info():
    Channel= []
    Links = []
    Name = []
    thumbnail= []
    Channel_name =[]


def search(searchh):
    # searchh = input("what you wanna search: ")
    query = str(searchh.replace(" ","+"))

    response = requests.get(f"https://www.youtube.com/results?search_query={query}").text


    soup =BeautifulSoup(response,'lxml')
    scripts = soup.findAll("script")
    json_text=re.search("var ytInitialData = (.+)[,:]{1}",str(scripts)).group(1)
    endpoint = json_text.rindex("};")+1
    json_text = json_text[:endpoint]
    # print(json_text)
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

                    if k == "title" :
                        Info.Name.append(v['runs' ][0]['text'])
                        #print(v['runs' ][0]['text'] +'\n')

                    if k == "videoId":
                     #   print (" ")
                        #print(v + "\n")
                        Info.Links.append(v)
                        
                    if k=="thumbnail" or k=="thumbnails":
                        #print(v["thumbnails"][0]["url"]+'\n')
                        Info.thumbnail.append(v["thumbnails"][0]["url"])
                    if k=='longBylineText':
                        Info.Channel_name.append(v['runs'][0]['text'])
                        Info.Channel.append(v['runs'][0]['navigationEndpoint']['browseEndpoint']['browseId'])

    except: 
        print(" ")
# search("lovely)
# print(Info.Name)