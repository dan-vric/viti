import os
import glob
import subprocess 

from datetime import datetime, timedelta, date
#import pysftp


#import paramiko



def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)


for i in range(9):
	skiplist = []
	for f in glob.glob("C:/Users/daniel.bath/Desktop/timelapse/viti" + str(i) + "_2022*"):
		skiplist.append(f.split('_')[-2])
	start_dt = datetime.strptime(max(skiplist),"%Y%m%d")
	copylist = []
	for dt in daterange(start_dt, datetime.now()):
	    copylist.append(dt.strftime("%Y%m%d"))
	for DATE in copylist:
		#from windows machine, call:
		print("scp pi@192.168.81.24" + str(i) + ":/home/pi/DATA/viti" + str(i) + "_" + str(DATE) + "* C:/Users/daniel.bath/Desktop/timelapse")
		subprocess.call("scp pi@192.168.81.24" + str(i) + ":/home/pi/DATA/viti" + str(i) + "_" + str(DATE) + "* C:/Users/daniel.bath/Desktop/timelapse")
		print('...')
	
	