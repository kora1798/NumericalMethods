def realvalue(n):
	result = 0
	for i in range(1, n + 1):
		result += 1/(i ** 1.1)
	return result

def extrapol(z1, z2, k):
	return z2 + (z2 - z1)/(2**k - 1)

zt = 10.5844484649508098
extr3 = 10.5844484649508098
str = "{0:<6}{1:^20}{2:^25}{3:^25}{4:^25}{5:^25}{6:^25}".format("n", "zn - zt", "zn - zn(1)", "zn(1) - zt", "delta(n)", "zn(2) - zt", "delta(n)(1)")
print (str)
n = 2
while n <= 131072:
	rv1 = realvalue(n)
	extr1 = extrapol(realvalue(round(n/2)), realvalue(n), 0.1)
	if n>=4:
		extr2 =  extrapol(realvalue(round(n/4)), realvalue(round(n/2)), 0.1)
		str = "{0:<6}{1:^20}{2:^25}{3:^25}{4:^25}{5:^25}{6:^25}".format(n, round(rv1 - zt, 3), rv1 - extr1, extr1 - zt, (extr1 - zt)/round(rv1 - zt, 3), extrapol(extr1, extr2, -1.1) - zt, (extrapol(extr1, extr2, -1.1) - zt)/(extr1 - zt))
	else:
		str = "{0:<6}{1:^20}{2:^25}{3:^25}{4:^25}{5:^25}{6:^25}".format(n, round(rv1 - zt, 3),  rv1 - extr1, extr1 - zt,(extr1 - zt)/round(rv1 - zt, 3), "-", "-")
	print (str)
	n *= 2
