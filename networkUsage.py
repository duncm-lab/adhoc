#!/usr/bin/python 
 
from commands import getoutput
from datetime import datetime
from os import getlogin
from time import sleep

class NETWORK_USAGE():

	def __init__(self):
		self.ifconfigRaw = str
		self.ifconfig = str
		self.datejoin = str

	def createIfconfig(self):
		self.ifconfig_raw = getoutput('ifconfig eth0')
		self.ifconfig = self.ifconfig_raw.rsplit()[-6:-4]
		self.ifconfig = self.ifconfig[0]
		self.ifconfig = self.ifconfig.replace('(', '')

	def getCurrentDate(self):
		self.date = datetime.now().ctime() 
		self.datejoin = str(self.ifconfig + 'mb' + ': ' + self.date)

	def fileObject(self):
		with open('/home/dunc/Programming/network_usage.txt', 'a') as fl:
			fl.writelines(self.datejoin + '\n')
	


def main():
	
	while getlogin() == 'dunc':
		sleep(10)
		x = NETWORK_USAGE()
		x.createIfconfig()
		x.getCurrentDate()		
		x.fileObject()
		del x			


if __name__=='__main__':
	main()	


# the while loop only repeats the same result

