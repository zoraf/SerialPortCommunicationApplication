import serial
import sys
import glob
import time

class ListAllPort():
	global serialPortToCommunicate 
	# global baudrate = 115200
	def __init__(self):
		print("new ListAllPort Object is created")

	def serial_ports(self):
	    if sys.platform.startswith('win'):
	        ports = ['COM%s' % (i + 1) for i in range(256)]
	    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
	        # this excludes your current terminal "/dev/tty"
	        ports = glob.glob('/dev/tty[A-Za-z]*')
	    elif sys.platform.startswith('darwin'):
	        ports = glob.glob('/dev/tty.*')
	    else:
	        raise EnvironmentError('Unsupported platform')

	    result = []
	    for port in ports:
	        try:
	            s = serial.Serial(port)
	            s.close()
	            result.append(port)
	            serialPortToCommunicate = serial.Serial(port,115200)
	        except (OSError, serial.SerialException):
	            pass
	    print(result)
   	def readData(self):
   		serialPortToCommunicate.timeout = 2
   		print serialPortToCommunicate.is_open
   		if serialPortToCommunicate.is_open:
	   		while True:
	   			size = serialPortToCommunicate.inWaiting()
	   			if size:
	   				data = serialPortToCommunicate.read(size)
	   				print data
				else:
					print 'no data'
				time.sleep(1)
		else:
			print 'serial port is not open'
