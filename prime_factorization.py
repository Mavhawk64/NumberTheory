def prime_factorization_unfiltered(x):
	dictionary = dict()
	p = get_primes_to(x)
	for i in p:
		dictionary[i] = 0
	for i in p:
		while x % i == 0:
			x = int(x/i)
			dictionary[i] += 1
	return dictionary

def prime_factorization_filtered(x):
	p = get_primes_to(x)
	dictionary = prime_factorization_unfiltered(x)
	for i in p:
		if dictionary[i] == 0:
			dictionary.pop(i)
	return dictionary

def prime_factorization(x):
	dictionary = prime_factorization_filtered(x)
	st = ''
	prod = 1
	for i in dictionary:
		prod *= (i ** dictionary[i])
		st += f'{i}^({dictionary[i]}) * '
	print(prod)
	st = st[:-3]
	return st

def is_prime(x):
	for i in range(2,int(x**0.5)+1):
		if x % i == 0:
			return False
	return True

def get_primes_to(x):
	p = []
	for i in range(2,x+1):
		if is_prime(i):
			p.append(i)
	return p

print(prime_factorization(150150))