from datetime import datetime
from math import floor
from time import sleep

amountOfSecondsIn2022 = 365 * 24 * 60 * 60

def printTimeTo2022( offset ):
	midnight = datetime(2022, 1, 1)
	now = datetime.now()
	amountOfSecondsLeftStringifiedWithDecimal = str(round(offset + (midnight - now).total_seconds(), 0))
	amountOfSecondsLeftStringifiedWithoutDecimal = amountOfSecondsLeftStringifiedWithDecimal[:-2]
	print (amountOfSecondsLeftStringifiedWithoutDecimal + " seconden")
 
def printTimeTo2023():
    
    
    printTimeTo2022( amountOfSecondsIn2022 )

def printTimeTo2026():
    amountOfSecondsIn2023and2024and2025 = (365 + 366 + 365) * 24 * 60 * 60
    amountOfSecondsBetweenStartOf2022AndEndOf2025 = amountOfSecondsIn2022 + amountOfSecondsIn2023and2024and2025	
    
    printTimeTo2022( amountOfSecondsBetweenStartOf2022AndEndOf2025 )

def main():
	while (True):
		sleep(1)
		printTimeTo2026()

if __name__ == "__main__":
	main()
