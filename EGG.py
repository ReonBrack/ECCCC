#imports
import math

#globals
a = int(input("a? "))
b = int(input("b? "))
p = int(input("p? "))
couples = []

#functions
def do_calc():
	for x in range(0, p):
		for y in range(0, p):
			if is_couple(x, y) is True:
				couples.append("({},{})".format(str(x),str(y)))
			
def is_couple(x, y):
	part1 = (math.pow(y, 2)) % p
	part2 = ((math.pow(x, 3) + a*x + b)) % p
	return part1 == part2

def print_couples():
	for c in couples:
		print c	
	
#start of the script
do_calc()
print_couples()


	
