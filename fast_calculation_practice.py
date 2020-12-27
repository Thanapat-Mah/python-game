"""
fast calculation practice
"""

import random as r

#set initial values
round = 1
user_input = ""
amount = 0
numlist = []
ans = 0

#calculation buffer
callist = []
num1 = 0
num2 = 0
op = 0
op_rand = 'y'
oplist = ["+", "-", "*", "/"]
log = "" #calculation log

print("<i> Enter \"end\" to end program") #start program

#loop program
while(user_input != "end"):
	#reset values
	numlist = []
	log = ""
	
	#check round, set amount of number
	if(round > 20): round = 1 #reset round
	if(round <= 10): amount = 4
	else: amount = 5
	
	#random number
	for i in range(0, amount): numlist.append(r.randint(1, 9))
	callist = numlist.copy()
		
	#calculate
	for i in range(0, amount - 1):
		#random pair of number
		num1 = int(callist.pop(r.randint(0, len(callist) - 1)))
		num2 = int(callist.pop(r.randint(0, len(callist) - 1)))
		op_rand = 'y'
		
		#random operation & calculate
		while(op_rand == 'y'):
			op = r.randint(0, 3)
			if(op == 0): ans = num1 + num2
			elif(op == 1): ans = num1 - num2
			elif(op == 2): ans = num1 * num2
			else: 
				if(num2 != 0): ans = num1 / num2
					
			if((ans%1 == 0) and (ans >= 0) and (num2 != 0)):
				callist.append(ans)
				op_rand = 'n'
				
				#calculation log
				log = log + str(num1) + oplist[op] + str(num2)
				if(len(callist) > 1): log += ", "
	
	#output
	print("\n<", round, "/20> ", int(ans), " | ", numlist, sep = "", end = "") #question
	user_input = input("<?> Enter to continue: ") #input
	print("<i>", log) #show answer
	round += 1
	
print("\n<i> Program end")