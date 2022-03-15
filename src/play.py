import subprocess
import shlex
import sys
import getopt

argv = sys.argv[1:]
r = ""
# t = ""
t=""
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
        r = "160"
    elif resolution ==  "240":
        r = "133"
    elif resolution == "360":
        r = "134"
    elif resolution == "480":
        r = "135"
    elif resolution == "720":
        r = "136"
    elif resolution == "1080":
        r = "137"
    else:
        pass
except:pass

if r == "":
   r = "bestvideo"

try:
    if vt =="yes":
        subprocess.call(["./audio.sh",t, link])
except:
    subprocess.call(["./video.sh" ,r ,link])

