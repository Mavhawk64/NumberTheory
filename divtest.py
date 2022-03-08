def div_test(a,b):
	if b == 0:
		return False
	return a % b == 0

def quotient_remainder(a,b):
	if b == 0:
		return None
	q = int(a/b)
	r = a%b
	return q,r

def t(n):
	seq.append(n)
	if n == 1:
		return len(seq)
	if n % 2 == 0:
		return t(int(n/2))
	return t(int(0.5*(3*n+1)))

def base_convert(num,base,builder=[]):
	q,r = quotient_remainder(num,base)
	print(f"{num} = {base}*{q} + {r}")
	if r > 9:
		r = chr(r+87).upper()
	r = str(r)
	builder.append(r)
	if q == 0:
		builder.reverse()
		return ''.join(builder)
	return base_convert(q,base,builder)


# print(div_test(62405,5))
# print(quotient_remainder(39,5))
# seq = []
# print(t(7))
# print(seq)
print(37*57198266342+20)
print(base_convert(2116335854674,37))