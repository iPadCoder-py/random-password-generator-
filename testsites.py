import random

def password(length):
	pw = str()
	char = 'abcdefghijklmnopqrstuvwxyz1234567890'
	for i in range(length):
		pw = pw + random.choice(char)
	print(pw)
	return pw
	
randomlen = random.randint(1,10)

password(randomlen)
