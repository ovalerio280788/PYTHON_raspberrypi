import getopt
import sys
import RPi.GPIO as GPIO
import time


##################################################################################################
# usage
##################################################################################################
def usage():
    print "\nUsage: " + sys.argv[0] + " [options]"
    print """
    Enable/Disable 110v current flow.
    Options:
        -s, --status       Status (1 -> enable / 0 -> Disable)\t*REQUIRED
        -p, --pin          Pin number to enable disable\t\t*REQUIRED
        -h, --help         Display this help
        """
    sys.exit(0)
	
try:
    opts, extra_params = getopt.getopt(sys.argv[1:],
                                       "s:p:h",
                                       ["status=", "pin", "help"])
except getopt.GetoptError, err:
    print str(err)
    usage()
	
status=-1
pin=0

for opt, arg in opts:
    if opt in ['-s', '--status']:
        status = int(arg)
    elif opt in ['-p', '--pin']:
        pin = int(arg)
    elif opt in ['-h', '--help']:
        usage()
		
if status == -1 or pin == 0:
	print "\n\nCHECK PARAMETERS AGAIN PLEASE\n\n"
	usage()


def chance_pins_to_status(pin, status, sleep_time=0):
        if status is not None:
                GPIO.output(pin, status)
                time.sleep(sleep_time)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)

#**************************************************************
# MAIN
#**************************************************************
if status is 1:
	chance_pins_to_status(pin, GPIO.HIGH)
else:
	chance_pins_to_status(pin, GPIO.LOW)


