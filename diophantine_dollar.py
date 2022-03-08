# x = 25*q + 10*d + 5*n + p

def sol_quarter(x,p=0,n=0,d=0):
	if (x-10*d-5*n-p) % 25 == 0:
		return [int((x-10*d-5*n-p)/25),d,n,p]
	return None

def sol_dime_quarter(x,p=0,n=0):
	pass


def sol_nickel_dime_quarter(x,p=0):
	pass

def sol_all_four_coins(x):
	pass