while True:
	input1 = input("1st nummber: ")		#get first input
	input2 = input("2nd nummber: ")		#get second input

	try:
		int1 = int(input1)					#convert 1st input to int
		int2 = int(input2)					#convert 2nd input to int
	except ValueError:
		print("invalid input, try again!")
		continue
	break


solution = int1 + int2 				#add 'int1' to 'int2' and store in 'solution'

print(str(int1) + " plus " + str(int2) + " is " + str(solution))						#print solution