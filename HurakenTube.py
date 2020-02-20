import sys
import youtube_dl
import os 
import subprocess

#def dl ():
p=sys.stdin.readline()
p=p.strip('\n')
print (p)
subprocess.call(["youtube-dl -o cache/p --merge-output-format mkv "+p],shell=True)
