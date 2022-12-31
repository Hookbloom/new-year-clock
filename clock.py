from datetime import datetime
from math import floor
from time import sleep

def printTime():
	midnight = datetime(2022, 1, 1)
	now = datetime.now()
	print (str(round((midnight - now).total_seconds(), 0)) + " seconden")

def main():
	while (True):
		sleep(1)
		printTime()

if __name__ == "__main__":
	main()
