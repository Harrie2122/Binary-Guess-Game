## Project on Binary Guess Game
## By harrie and team
## dated 16/01/2021

print("Think of a Number between 0-63")
input("You will be asked 6 ques and answer it by [y/n], press any key to continue")

bine=""

que1= input("Is Your number is odd\n")
if que1 == 'y' or que1 == 'Y':
    bine = bine + '1'
elif que1 == 'n' or que1 == 'N':
    bine = bine + '0'

que2= input("""Is Your number is: 2,3,6,7,10,11,14,15,18,19,22,23,26,27,30,31,34,35,38,39,42,43,46,47, 50,51,54,
55,58,59,62,63""")
if que2 == 'y' or que2 == 'Y':
    bine = bine + '1'
elif que2 == 'n' or que2 == 'N':
    bine = bine + '0'

que3= input("Is Your number is in: 4-7, 12-15, 20-23, 28-31, 36-39, 44-47, 52-55, 60-63")
if que3 == 'y' or que3 == 'Y':
    bine = bine + '1'
elif que3 == 'n' or que3 == 'N':
    bine = bine + '0'

que4= input("Is Your number is in: 8-15, 24-31, 40-47, 56-63")
if que4 == 'y' or que4 == 'Y':
    bine = bine + '1'
elif que4 == 'n' or que4 == 'N':
    bine = bine + '0'

que5= input("Is Your number is in: 16-31, 48-63")
if que5 == 'y' or que5 == 'Y':
    bine = bine + '1'
elif que5 == 'n' or que5 == 'N':
    bine = bine + '0'

que6= input("Is Your number is in: 32-63")
if que6 == 'y' or que6 == 'Y':
    bine = bine + '1'
elif que6 == 'n' or que6 == 'N':
    bine = bine + '0'

#### BINARY CONVERSION ####
bine = list(bine)
bine.reverse()
print(bine)
value = 0
for i in range(len(bine)):
	digit = bine.pop()
	if digit == '1':
		value = value + pow(2, i)
    
print("Your Number is", value)
