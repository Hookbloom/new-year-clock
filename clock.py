from datetime import datetime
from math import floor
from time import sleep

def printTimeTo2022( offset ):
	midnight = datetime(2022, 1, 1)
	now = datetime.now()
	amountOfSecondsLeftStringifiedWithDecimal = str(round(offset + (midnight - now).total_seconds(), 0))
	amountOfSecondsLeftStringifiedWithoutDecimal = amountOfSecondsLeftStringifiedWithDecimal[:-2]
	print (amountOfSecondsLeftStringifiedWithoutDecimal + " seconden")
 
def printTimeTo2023():
    amountOfSecondsIn2022 = 365 * 24 * 60 * 60
    
    printTimeTo2022( amountOfSecondsIn2022 )

def main():
	while (True):
		sleep(1)
		printTimeTo2023()

if __name__ == "__main__":
	main()
