#Libraries
import RPi.GPIO as GPIO
import time
from time import sleep
 
def getData():
    #GPIO Mode (BOARD / BCM)
    GPIO.setmode(GPIO.BOARD)

     
    #set GPIO Pins
    triggerL = 11
    echoL = 13

    triggerR = 16
    echoR = 18

    buzzerL = 32
    buzzerR = 33


     
    #set GPIO direction (IN / OUT)
    GPIO.setup(buzzerR, GPIO.OUT)
    GPIO.setup(buzzerL, GPIO.OUT)
    GPIO.setup(triggerR, GPIO.OUT)
    GPIO.setup(echoR, GPIO.IN)
    GPIO.setup(echoL, GPIO.IN)
    GPIO.setup(triggerL, GPIO.OUT)

    pwmL = GPIO.PWM(buzzerL, 1000)
    pwmR = GPIO.PWM(buzzerR, 1000)

    pwmL.start(0)
    pwmR.start(0)

    i = 0

     
    def distance(trig, echo):
        # set Trigger to HIGH
        GPIO.output(trig, True)
        
     
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(trig, False)
        
     
        StartTime = time.time()
        StopTime = time.time()
        
     
        # save StartTime
        while GPIO.input(echo) == 0:
            StartTime = time.time()
            
        
     
        # save time of arrival
        while GPIO.input(echo) != 0:
            StopTime = time.time()
            
        
     
        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2
     
        return distance
     
    
    try:
        while True:
                
            distL = distance(triggerL, echoL)
            distR = distance(triggerR, echoR)


            if distL < 30:
                pwmL.ChangeDutyCycle(100)
                GPIO.output(buzzerL, True)
                print("Too close on the left")
            elif distL < 45:
                pwmL.ChangeDutyCycle(66)
                GPIO.output(buzzerL, True)
                print("Too close on the left")
            elif distL < 60:
                pwmL.ChangeDutyCycle(33)
                GPIO.output(buzzerL, True)
                print("Too close on the left")
            else:
                pwmL.ChangeDutyCycle(0)
                GPIO.output(buzzerL, False)
                            
            if distR < 30:
                pwmR.ChangeDutyCycle(100)
                GPIO.output(buzzerR, True)
                print("Too close on the right")
            elif distR < 45:
                pwmR.ChangeDutyCycle(66)
                GPIO.output(buzzerR, True)
                print("Too close on the right")
            elif distR < 60:
                pwmR.ChangeDutyCycle(33)
                GPIO.output(buzzerR, True)
                print("Too close on the right")
            else:
                pwmR.ChangeDutyCycle(0)
                GPIO.output(buzzerR, False)
                
                    
            print ("Measured Distance Left = %.1f cm" % distL)
            print ("Measured Distance Right = %.1f cm" % distR)
            time.sleep(1)
                
            i=i+1
     
            # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
