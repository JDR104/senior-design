import cameras as cam
import usTest as sensors
import cv2
import numpy
from time import sleep
import triangulation as tri
import threading

t1 = threading.Thread(target=cam.stereoVision)
t2 = threading.Thread(target=sensors.getData)

t1.start()
t2.start()
      
