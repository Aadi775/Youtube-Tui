import subprocess
from webbrowser import get

def Get(link,r="",t=""):
    # print(resolution)

    try:
        if r == "140":
            r = "160"
        elif r ==  "240":
            r = "133"
        elif r == "360":
            r = "134"
        elif r == "480":
            r = "135"
        elif r== "720":
            r = "136"
        elif r == "1080":
            r = "137"
        else:
            pass
    except:pass

    if r == "":
        r = "bestvideo"

    try:
        if t =="yes":
            subprocess.call(["./audio.sh", f"{link}"])
        else:
            subprocess.call(["./video.sh" ,r ,f"{link}"])
    except: pass
