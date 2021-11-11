import sys, os
from picamera import PiCamera
from time import sleep
import datetime
import socket

TIMESTAMP = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S")
HOST = socket.gethostname()

camera = PiCamera()
camera.start_preview(alpha=0)
camera.exposure_mode='auto'
camera.awb_mode='auto'
#camera.annotate_text = "Hello world!"
sleep(5)
camera.capture('/home/pi/DATA/' + HOST + '_' + TIMESTAMP + '.jpg')
camera.stop_preview()
print("job done")