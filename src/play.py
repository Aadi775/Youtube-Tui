import subprocess
import shlex
import sys
import getopt

argv = sys.argv[1:]
class Storage:
    r = ""
    # t = ""
    t=""

class Get:
    
    try:
        opts,args = getopt.getopt(argv,"r:l:p:")
    except Exception as e:
        print(e)

    for opt,arg in opts:
        if opt in ["-l","-link"]:
            link = arg

        elif opt in ["-r","-resolution"]:
            resolution = arg 

        elif opt in ["-p","-player"]:
            vt = arg

    # print(resolution)

    try:
        if resolution == "140":
            Storage.r = "160"
        elif resolution ==  "240":
            Storage.r = "133"
        elif resolution == "360":
            Storage.r = "134"
        elif resolution == "480":
            Storage.r = "135"
        elif resolution == "720":
            Storage.r = "136"
        elif resolution == "1080":
            Storage.r = "137"
        else:
            pass
    except:pass

    if Storage.r == "":
        Storage.r = "bestvideo"

    try:
        if vt =="yes":
            subprocess.call(["./audio.sh",Storage.t, link])
    except:
        subprocess.call(["./video.sh" ,Storage.r ,link])


