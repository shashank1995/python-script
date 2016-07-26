import time
import sys
import matplotlib.pyplot as plt

def moreDetails():
	lines = open("/proc/net/dev", "r").readlines()

	columnLine = lines[1]
	_, receiveCols , transmitCols = columnLine.split("|")
	receiveCols = map(lambda a:"recv_"+a, receiveCols.split())
	transmitCols = map(lambda a:"trans_"+a, transmitCols.split())

	cols = receiveCols+transmitCols

	faces = {}
	for line in lines[2:]:
		if line.find(":") < 0: continue
		face, data = line.split(":")
		faceData = dict(zip(cols, data.split()))
		faces[face] = faceData

	import pprint
	pprint.pprint(faces)
	
def get_bytesReceived():
	summ = 0
	lining = open("/proc/net/dev", "r").readlines()
	for line in lining[2:]:
		a,b = line.split(":")
		arr = []
		for d in range(16):
			arr.append(d)
		c = dict(zip(arr, b.split()))
		summ = summ + int(c[0])
	return summ

def get_bytesTransmitted():
	summ = 0
	lining = open("/proc/net/dev", "r").readlines()
	for line in lining[2:]:
		a,b = line.split(":")
		arr = []
		for d in range(16):
			arr.append(d)
		c = dict(zip(arr, b.split()))
		summ = summ + int(c[8])
	return summ

lis = []
lis1 = []
def pretty_speed(speed,du):
    units = ['bps', 'Kbps', 'Mbps', 'Gbps']
    unit = 0
    while speed >= 1024:
        speed /= 1024.0
        unit += 1
    speed = speed * 8
    while speed >= 1024:
	speed /= 1024.0
	unit += 1
    speed1 = speed
    if unit == 0 and du == 'down':
	speed1 = 0
	lis.append(speed1)
    elif unit == 0 and du == 'up':
	speed1 = 0
	lis1.append(speed1)
    elif unit == 1 and du == 'down':
	speed1 = speed * 0.001
	lis.append(speed1)
    elif unit == 1 and du == 'up':
	speed1 = speed * 0.001
	lis1.append(speed1)
    elif unit == 2 and du == 'down':
	lis.append(speed1)
    elif unit == 2 and du == 'up':
	lis1.append(speed1)
    print '%0.2f %s' % (speed, units[unit])

def pretty_usage(speed):
    units = ['b', 'Kb', 'Mb', 'Gb']
    unit = 0
    while speed >= 1024:
        speed /= 1024.0
        unit += 1
    print '%0.2f %s' % (speed, units[unit])

def realTimeSpeed():
	for i in range(7):
		initial = get_bytesReceived()
		time.sleep(1)
		final = get_bytesReceived()
		du = 'down'
		print "Download speed:",
		pretty_speed(final-initial,du)
		initial = get_bytesTransmitted()
		time.sleep(1)
		final = get_bytesTransmitted()
		du = 'up'
		print "Upload speed:",
		pretty_speed(final-initial,du)
		print('')
	plt.plot([1,2,3,4,5,6,7],lis,'b-',[1,2,3,4,5,6,7],lis1,'r-')
	plt.ylabel('blue line download and red line upload (mbps)')
	plt.xlabel('time')
	lis[:] = []
	lis1[:] = []
	plt.show()

def totalUsage():
	a = get_bytesReceived()
	print "Total download:",
	pretty_usage(a)
	b= get_bytesTransmitted()
	print "Total Upload:",
	pretty_usage(b)
	print('')

def exit():
	sys.exit(1)

def main():
	print "Choose from the following options:"
	print "1.Total download and upload usage"
	print "2.Internet speed"
	print "3.More details"
	print "4.Exit"
	a = input()
	options = {1 : totalUsage,
		   2 : realTimeSpeed,
		   3 : moreDetails,
		   4 : exit
		   }
	options[a]()
	main()

main()
	
