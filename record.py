from picamera import PiCamera
from time import sleep

camera = PiCamera()

camera.start_preview(alpha=160)
camera.exposure_mode='auto'
camera.awb_mode='auto'
#camera.annotate_text = "Hello world!"
sleep(5)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()