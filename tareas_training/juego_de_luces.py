import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pins = [17,27,22,18,23,24,12,16]
print "\n*********************************************"
print "* This are the ports I will using"
print "***********************************************\n"
print pins

def set_all_pins_to_out_type():
	for pin in pins:
		GPIO.setup(pin,GPIO.OUT)

def chance_all_pins_to_status(status, sleep_time=0, reverse=False):
	state = None
	tmp_pins = pins
	if reverse:
		tmp_pins = reversed(tmp_pins)
	
	if status == GPIO.HIGH:
		state = GPIO.HIGH
	elif status == GPIO.LOW:
		state = GPIO.LOW
		
	if state is not None:
		for pin in tmp_pins:
			GPIO.output(pin, state)
			time.sleep(sleep_time)
			
def my_reverse(alist):
    newlist = []
    for i in range(1, len(alist) + 1):
        newlist.append(alist[-i])
    return newlist
	
def turn_halfs_to_left_right(sleep_time=1, reverse=False):
	tmp_pins = pins
	a = []
	b = []
	
	for i in xrange(0,len(tmp_pins)/2):
		a.append(tmp_pins[i])
		
	for i in xrange(len(tmp_pins)/2,len(tmp_pins)):
		b.append(tmp_pins[i])
	
	if reverse:
		a = my_reverse(a)
		b = my_reverse(b)
	
	for i in xrange(len(a)):
		GPIO.output(a[i], GPIO.LOW)
		GPIO.output(b[i], GPIO.LOW)
		time.sleep(sleep_time)
		GPIO.output(a[i], GPIO.HIGH)
		GPIO.output(b[i], GPIO.HIGH)
		time.sleep(sleep_time)
	
#************************
# MAIN
#************************

# SET ALL PINS TO OUT TYPE
set_all_pins_to_out_type()


# TURN ALL LIGHT OFF
chance_all_pins_to_status(GPIO.HIGH)

#####################################################################################
# TEST 01  -- TURN ON ALL LIGHTS ONE BY ONE AND AFTER TURN OFF ONE BY ONE SAME SIDE
#####################################################################################
print "TEST 01  -- TURN ON ALL LIGHTS ONE BY ONE AND AFTER TURN OFF ONE BY ONE SAME SIDE"
chance_all_pins_to_status(GPIO.LOW, 0.2)
chance_all_pins_to_status(GPIO.HIGH, 0.2)
chance_all_pins_to_status(GPIO.HIGH)


#####################################################################################
# TEST 02  -- TURN ON ALL LIGHTS ONE BY ONE AND AFTER TURN OFF ONE BY ONE BACK SIDE
#####################################################################################
chance_all_pins_to_status(GPIO.LOW, 0.2)
chance_all_pins_to_status(GPIO.HIGH, 0.2, True)
chance_all_pins_to_status(GPIO.HIGH)

#####################################################################################
# TEST 02  -- TURN ON ALL LIGHTS ONE BY ONE AND AFTER TURN OFF ONE BY ONE BACK SIDE
#####################################################################################
turn_halfs_to_left_right(0.2)
turn_halfs_to_left_right(0.2, True)
turn_halfs_to_left_right(0.2)
turn_halfs_to_left_right(0.2, True)
