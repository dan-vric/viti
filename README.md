# viti
Vineland Timelapse



instructions for streaming:

1. establish a connection via ssh:

        ssh pi@192.168.81.24X (where X is the number of the unit you want to access)
        
        enter password: vric
       

2. start streaming:

        sh viti/stream.sh
        

3. Go to the following URL in a browser (subbing "X" for the number of your unit):
        
        http://192.168.81.24X:8080/stream.html
        

instructions for accessing data:


1. establish a connection via ssh:

        ssh pi@192.168.81.24X (where X is the number of the unit you want to access)
        
        enter password: vric


2.  Find images located in the directory 
        
        /home/pi/DATA
