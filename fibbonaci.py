

n = int(input('whats your number?'))



if n == 0: 
	print('The answer is: none')
if n == 1: 
	print('The answer is: 0')
if n == 2: 
	print('The answer is: 1')
if n == 3:
	print('The answer is: 1')

def fibbo(n):

	my_fib1 = 0
	my_fib2 = 1
	
	for a in range(1,n-1):
		my_fib = my_fib1 + my_fib2
		print(my_fib)
		my_fib1 = my_fib2
		my_fib2 = my_fib
	print('here is your fibbo {} '.format(my_fib))

if n > 3:
	fibbo(n)

