import math
a = 1
b = -1.4
c = 0.01
d = 0.11
x1 = 0
y1 = 0
alpha = 1
E = 10**(-4)

def f(x,y):
    return a*x + b*y + math.exp(c*(x**2) + d*(y**2))

def fproizv(x,y):
    return (a + 2*c*x * math.exp(c * x**2 + d * y**2), b + 2*d*y * math.exp(c * x**2 + d * y**2))

def step(x1,y1,alpha):
    if((fproizv(x1,y1)[0] < E/2) and (fproizv(x1,y1)[1] < E/2)):
        return (x1,y1)
    else:
        x2 = x1 - alpha * fproizv(x1,y1)[0]
        y2 = y1 - alpha * fproizv(x1,y1)[1]
        if(f(x2,y2) > f(x1,y1)):
            return step(x1,y1,alpha/2)
        else:
            return step(x2,y2,alpha)
ans = step(x1,y1,alpha)
print ans
print f(ans[0],ans[1])