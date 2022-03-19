import shlex
import sys
import getopt
import scrape, play

search = input("Search: ")
scrape.search(search)
for i in range(len(scrape.Info.Links)):
    print(i+1, scrape.Info.Name[i])
    i=i

select = input("Select: ")
try:
    if int(select) > len(scrape.Info.Links)+1:
        print("WTH BRO!!!"+'\n')
        sys.exit()
    temp = 'https://www.youtube.com/watch?v='
    link = temp+scrape.Info.Links[int(select)-1]
    quality = input("choose the resolution (144/240/360/480/720/1080)[press enter for best quality]:")
    mp3 = input("Do you wanna run mp3 format(yes/no): ")
    play.Get(link,quality,mp3)
except:
    pass