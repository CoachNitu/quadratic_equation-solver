# Python program to find roots of quadratic equation 
import math 
import time
import sys
import os
import time
import subprocess

import platform

# function for finding roots
def equationroots( a, b, c):

	# calculating discriminant using formula
	dis = b * b - 4 * a * c
	sqrt_val = math.sqrt(abs(dis))

	# checking condition for discriminant
	if dis > 0:
		print("\n ----------------Calculating----------------")
		time.sleep(420. / 100)
		print(" \n  real and different roots ")
		print((-b + sqrt_val)/(2 * a))
		print((-b - sqrt_val)/(2 * a))

	elif dis == 0:
		print(" \n real and same roots")
		print(-b / (2 * a))

	# when discriminant is less than 0
	else:
		print("\n ----------------Calculating----------------")
		time.sleep(420. / 100)

		print(" \n Complex Roots")
		print(- b / (2 * a), " + i", sqrt_val)
		print(- b / (2 * a), " - i", sqrt_val)


def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(10. / 1000)


slowprint("[!] Starting : ")
time.sleep(4)
os.system('')


def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(4. / 100)


slowprint("    \033[91m")
print('''                              

    
███╗░░░███╗░█████╗░████████╗██╗░░██╗███████╗███╗░░░███╗░█████╗░████████╗██╗░█████╗░░██████╗
████╗░████║██╔══██╗╚══██╔══╝██║░░██║██╔════╝████╗░████║██╔══██╗╚══██╔══╝██║██╔══██╗██╔════╝
██╔████╔██║███████║░░░██║░░░███████║█████╗░░██╔████╔██║███████║░░░██║░░░██║██║░░╚═╝╚█████╗░
██║╚██╔╝██║██╔══██║░░░██║░░░██╔══██║██╔══╝░░██║╚██╔╝██║██╔══██║░░░██║░░░██║██║░░██╗░╚═══██╗
██║░╚═╝░██║██║░░██║░░░██║░░░██║░░██║███████╗██║░╚═╝░██║██║░░██║░░░██║░░░██║╚█████╔╝██████╔╝
╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═════╝░

██╗░██████╗
██║██╔════╝
██║╚█████╗░
██║░╚═══██╗
██║██████╔╝
╚═╝╚═════╝░

███████╗░█████╗░░██████╗██╗░░░██╗
██╔════╝██╔══██╗██╔════╝╚██╗░██╔╝
█████╗░░███████║╚█████╗░░╚████╔╝░
██╔══╝░░██╔══██║░╚═══██╗░░╚██╔╝░░
███████╗██║░░██║██████╔╝░░░██║░░░
╚══════╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░                       ''')

print("\n")
print(" Enter Values Of 'A' 'B' 'C'")
time.sleep(420. / 100)
print("\n")
a = float(input('Enter value of a: '))
time.sleep(40. / 100)
b = float(input('Enter value of b: '))
time.sleep(42. / 100)
c = float(input('Enter value of c: '))



if a == 0: 
		print("Heck! I think you entered some wrong numbers. Fix it or you will still get errors :(")

else: 
	equationroots(a, b, c)
