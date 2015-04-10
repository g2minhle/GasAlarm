# Main background task to detect sensor, get phone number from a file and make call to user
import time
import serial
import RPi.GPIO as GPIO

def checkSensor():
	if GPIO.input(40) == False:
		return True
	if GPIO.input(37) == False:
		return True
	return False
	if GPIO.input(16) == False:
		return True
	if GPIO.input(15) == False:
		return True
	return False 

def getPhoneNumber():
	try :
		f = open("currentPhoneNumber","r")
		phoneNumber = f.readline()
		f.close()
		return phoneNumber
	except :		
		return ""


def makingCall(phoneNumber):
	print "makingCall"
	try :
		serialport = serial.Serial("/dev/ttyAMA0", 115200, timeout=0.5)
		serialport.write("AT\r")
		response = serialport.readlines(None)
		print response
		serialport.write("ATE0\r")
		response = serialport.readlines(None)
		print response
		serialport.write("AT\r")
		response = serialport.readlines(None)
		print response
		# call phone
		serialport.write("ATD" + getPhoneNumber() + ';\r')
		response = serialport.readlines(None)
		print response
		time.sleep(60)
	except :
		print "makingCall error"

def gpioSetup():
	time.sleep(10)
	# init board
	GPIO.setmode(GPIO.BOARD)
	#sim 900 power button
	GPIO.setup(33, GPIO.OUT)
	# turn on sim900
	GPIO.output(33, False)
	time.sleep(2)
	GPIO.output(33, True)

	# sensor input
	GPIO.setup(40, GPIO.IN)
	GPIO.setup(37, GPIO.IN)
	GPIO.setup(16, GPIO.IN)
	GPIO.setup(15, GPIO.IN)	
	time.sleep(10)

if __name__ == "__main__":
	gpioSetup()
	while True:
		# check sensor 	
		if (checkSensor()):
			print "gasDetected"
			# gas detected
			# get phone number from file
			phoneNumber = getPhoneNumber()
			if phoneNumber == "":
				continue
			makingCall(phoneNumber)
			print "resumeChecking"
		time.sleep(1)
