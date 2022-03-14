import subprocess
import shlex
import sys
import getopt

argumentList = sys.argv[1:]

options="hl:"

long_options = ["help","link"]

try:
    arguments, values = getopt.getopt(argumentList,options,long_options)

    for currentArgument,currentValue in arguments:
        if currentArgument in ("-h","--help"):
            print("play.py -l <your yt video link>")
        elif currentArgument in("-l","--link"):
            link = currentValue
            subprocess.call(shlex.split(f'/home/aadi/youtube-tui/src/play.sh {link}'))
except getopt.error as err:
    print(str(err))
