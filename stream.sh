#!/bin/bash

echo "Starting Stream"

cd /home/pi/mjpg-streamer/mjpg-streamer-experimental

./mjpg_streamer -o "output_http.so -w ./www" -i "input_raspicam.so"

echo "Streaming at"
