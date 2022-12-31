#Create a program that simulates the flipping of a coin and prints whether it landed on heads or tails.

print ("""==========================================================
			Flip the coin
==========================================================
""")


#import random

import random

#face or dry
F_or_D = ['FACE', 'DRY']

print ("type >>> go <<< to start the game")

palabra = ('go')
go = input(str())

if palabra in go:
	print ('Good luck! its: ' + random.choice(F_or_D))


print ("""==========================================================""")
