import sys
from rutube import Rutube
import pyinputplus as pyinp

print(sys.argv[1:][0])

vidlink = sys.argv[1:][0]
rt = Rutube(vidlink)

#print(rt.playlist)  # [Nature 4k (272x480), Nature 4k (408x720), Nature 4k (608x1080)]
numres = len(rt.playlist._playlist)
print(rt.playlist._playlist[0]._title)
chnum = 0
for res in rt.playlist:
    rcur = str(res._resolution[0]) + "x" + str(res._resolution[1])
    print("(" + str(chnum) + ") - " + rcur)
    chnum+=1

#resvar = input("Select resolution to download: ")
resvar = pyinp.inputInt(prompt="Select resolution to download: ", min=0, max=numres)

rt.playlist[resvar].download()
