import sys, os
print(os.path.dirname(sys.executable))
from picamera import PiCamera
from time import sleep
import datetime

camera = PiCamera()
TIMESTAMP = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d_%H%M%S")
camera.start_preview(alpha=0)
camera.exposure_mode='auto'
camera.awb_mode='auto'
#camera.annotate_text = "Hello world!"
sleep(5)
camera.capture('/home/pi/Desktop/' + TIMESTAMP + '.jpg')
camera.stop_preview()
print("job done")