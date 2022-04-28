import RPi.GPIO as GPIO
import time

sensorR = 16
buzzerR = 18
sensorL = 36
buzzerL = 38

i=0

GPIO.setmode(GPIO.BOARD)

GPIO.setup(sensorL, GPIO.IN)
GPIO.setup(buzzerL, GPIO.OUT)
GPIO.setup(sensorR, GPIO.IN)
GPIO.setup(buzzerR, GPIO.OUT)

GPIO.output(buzzerL, False)
GPIO.output(buzzerR, False)

print ("IR Sensor Ready.....")
print (" ")

try:
    while i < 10:
   
        if (GPIO.input(sensorL) == False):
            GPIO.output(buzzerL, True)
            print ("Object Detected Left")
        else:
            GPIO.output(buzzerL, False)
        if (GPIO.input(sensorR) == False):
            GPIO.output(buzzerR, True)
            print ("Object Detected Right")
        else:
            GPIO.output(buzzerR, False)
        time.sleep(0.2)
        i=i+1
        
except KeyboardInterrupt:
    GPIO.cleanup()
