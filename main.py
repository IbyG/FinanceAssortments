#FileName: main BY: Ibrahim George
#Date: Tuesday, December 22 2020

#calculates the amount of shares you can purchase
def positionsize(R,C,SP):
	#maximum loss
	ML = (R * C)/100
	print("\nYour maximum loss:\n",ML)

	#loss Amount
	LA = (SP * R)/100
	print("\nIndividual share loss amount:\n",LA)

	##quantity of shares to purcahse
	return(ML/LA)

def main(): 
	print("Hi this application, is used to calculate your risk management when investing")
	print("C = Capital")
	print("R = Risk per Trade (It is currently set to 2%)")
	print("SP = Share price")
	print("\n")
	C = float(input("What is your Capital?\n"))
	R = 2
	print("Risk is:\n2%")
	SP = float(input("What is the Share price?\n"))
	print("\n")
	print("The amount of share you can purchase is: ", int(positionsize(R,C,SP)))

	
main()
