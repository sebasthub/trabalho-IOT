from time import sleep
import RPi.GPIO as GPIO
import asyncio
from camera import camera
from threading import Thread

GPIO.cleanup()

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(2,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)


def acenderVerde(tempo):
    print(tempo)
    GPIO.output(2,True)
    sleep(tempo)
    GPIO.output(2,False)

def piscarLed():
     for i in range(2):
       GPIO.output(2,True)
       sleep(1)
       GPIO.output(2,False)
       sleep(1)

def piscarLedFundo():
	th0 = Thread(target=piscarLed)
	th0.start()

def botao():
    contador = 0
    trava = True
    while trava: # Run forever
        if GPIO.input(21) == False:
            print("Button was pushed!", contador)
            contador += 1
            trava = True
        else:
            trava = False
    return contador

			
pins = [18,23,24,25]
WaitTime = 0.005
StepCount2 = 8
Seq2 = []
Seq2 = [i for i in range(0, StepCount2)]
Seq2[0] = [1,0,0,0]
Seq2[1] = [1,1,0,0]
Seq2[2] = [0,1,0,0]
Seq2[3] = [0,1,1,0]
Seq2[4] = [0,0,1,0]
Seq2[5] = [0,0,1,1]
Seq2[6] = [0,0,0,1]
Seq2[7] = [1,0,0,1]
StepCount = StepCount2
Seq1 = Seq2
def steps(nb):
        tr1 = Thread(target=acenderVerde,args=(10,))
        tr1.start()
        StepCounter = 0
        if nb<0: sign=-1
        else: sign=1
        nb=sign*nb*2 #times 2 because half-step
        print("nbsteps {} and sign {}".format(nb,sign))
        for i in range(nb):
                for pin in range(4):
                        xpin = pins[pin]
                        if Seq1[StepCounter][pin]!=0:
                                GPIO.output(xpin, True)
                        else:
                                GPIO.output(xpin, False)
                StepCounter += sign
        # If we reach the end of the sequence
        # start again
                if (StepCounter==StepCount):
                        StepCounter = 0
                if (StepCounter<0):
                        StepCounter = StepCount-1
                # Wait before moving on
                sleep(WaitTime)
        for pin in range(4):
		        GPIO.output(pins[pin],False)

#GPIO.cleanup()
