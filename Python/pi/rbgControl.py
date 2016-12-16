import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)
GPIO.output(11,1)

GPIO.setup(13,GPIO.OUT)
GPIO.output(13,1)

GPIO.setup(15,GPIO.OUT)
GPIO.output(15,1)


try:
	while(True):
		request=raw_input("RGB-->")
		if (len(request) == 3):
			GPIO.output(11, int(request[0]))
			GPIO.output(13, int(request[1]))
			GPIO.output(15, int(request[2]))
except KeyboardInterupt:
	GPIO.cleanup()

