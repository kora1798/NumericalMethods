from math import sqrt

def f1(x):
	return 6 * (x**5)

def f2(x):
	return x ** (1/10) * sqrt(1 + x**2)

def ParabolM(n):
	step = (b - a)/n
	points = [(a + step * i) for i in range(0, n + 1)]
	sum1 = sum2 = 0
	for i in range(1, n):
		sum1 += f(points[i])
	for i in range(0, n):
		sum2 += f(points[i] + step/2)
	J = (step/6)*(f(a) + f(points[n]) + 2 * sum1 + 4 * sum2)
	return J

def Runge(n):
	if n >= 2:
		return (ParabolM(n) - ParabolM(round(n/2)))/(2**4 - 1)
	else:
		return "-"

def Kdelta(n):
	if n >= 4:
		return round((ParabolM(round(n/2)) - ParabolM(round(n/4)))/(ParabolM(n) - ParabolM(round(n/2))), 2)
	else:
		return "-"

def deltateor(n):
	step = 1/ n
	return (720/2880)*(step)**4

temp = input("1 - проинтегрировать функцию 6x^5\n2 - проинтегрировать сложную функцию на отрезке [0,1.5]\n3 - проинтегрировать сложную функцию на отрезке [0.001,1.5]\n")

if temp == "1":
	f = f1
	a = 0
	b = 1
if temp == "2":
	f = f2
	a = 0
	b = 1.5
if temp == "3":
	f = f2
	a = 0.001
	b = 1.5


n = 1
str = "{0:^5} {1:^30} {2:^30} {3:^30} {4:^30}".format("n", "Kdelta", "D_tochnoe", "D_Runge", "D_teor")
print(str)
while n <= 65536:
	if temp == "1":
		temp2 = 1 - ParabolM(n)
	else:
		temp2 = "-"
	str = "{0:<5} {1:^30} {2:<30} {3:<30} {4:<30}".format(n, Kdelta(n), temp2, Runge(n), deltateor(n))
	print(str)
	n = 2*n
print(ParabolM(65536))