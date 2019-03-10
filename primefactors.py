# Python3

#program to factorize given number into primes. Starting by generating primes up to 
#generate list of primes. find a larke chunk - assumed to be largest potential prime in number as upper range for prime list

def is_prime(num):
	"""return TRUE if num is a prime, and return FALSE if not"""
	if num == 0 or num == 1:
		return False 
	for x in range(2, num):
		if num % x == 0:
			return False
	else:
		return True 

def factorize(num):
	if is_prime(num):
		print('Your number is already a prime numner >> {}'.format(num))
	else:
		factors = []
		for x in range(1,num):
			if is_prime(x):
				new_num = num
				while new_num % x == 0:
					factors.append(x)
					new_num = new_num / x
				number = 1
				for x in factors:
					number = number * x
				if number == num:
					print("OK, I found all the primes in {}.".format(num))
					print("Here the primes I found: {}".format(factors))
					break

given_num = int(input('Which number do you want me to factorize?  '))
factorize(given_num)
	
# create a list of primes: >> my_primelist = filter(is_prime, range(1,num))