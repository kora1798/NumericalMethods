from math import sin, pi, fabs
from pprint import pprint

def data(n):
    bdata=[]
    step = pi / n
    x = 0  
    for i in range(n + 1):
        bdata.append((x, sin(x)))
        x += step
    return bdata

def Xs(n):
    xdata=[]
    step = pi / n
    x = step/2
    for i in range(n):
        xdata.append(x)
        x += step
    return xdata

def splinefuncs(n, xdata):
    Ss=[]
    ms = computation(n)
    step = pi / n
    bdata = data(n)
    k = 0
    for i in range(1,n+1):
        S = ((bdata[i][0] - xdata[k])**3 - step**2 * (bdata[i][0] - xdata[k])) * ms[i-1]/(6*step) + ((xdata[k] - bdata[i - 1][0])**3 - step**2 * (xdata[k] - bdata[i - 1][0]))* ms[i]/(6*step) + (bdata[i][0] - xdata[k]) * bdata[i - 1][1]/step + (xdata[k] - bdata[i - 1][0])*bdata[i][1]/step
        Ss.append(S)
        k += 1
    return Ss

def coeffs(n):
    bdata = data(n)
    step = pi / n
    cfs = []
    for i in range(1, n):
        cfs.append(dict(a = 2*step/3, b = step/6, c = step/6, d = (bdata[i+1][1] - 2*bdata[i][1] + bdata[i-1][1])/step))
    return cfs
        
def computation(n):
    lambdas=[0]
    nus=[0]
    step = pi / n
    cfs = coeffs(n)
    for i in range(1, n):
        lambdas.append(-cfs[i-1]['b']/(lambdas[i - 1] *cfs[i-1]['c'] + cfs[i-1]['a']))
        nus.append((cfs[i-1]['d'] - cfs[i-1]['c'] * nus[i - 1])/(lambdas[i - 1] * cfs[i-1]['c'] + cfs[i-1]['a']))
    ms = [0 for i in range(n+1)]
    for i in range(n - 1, 0, -1):
        ms[i] = nus[i] + lambdas[i] * ms[i + 1]
    return ms

n = 5
maxdeltas = []
maxdeltas2 = []
while n <= 640:
	S = [sin(x) for x in Xs(n)]
	G = splinefuncs(n, Xs(n))
	maxdeltas.append((n, max([S[i] - G[i] for i in range(n)])))
	n*=2
for i in range(1, len(maxdeltas)):
	maxdeltas2.append(maxdeltas[i-1][1]/maxdeltas[i][1])
for i in range(len(maxdeltas2)):
	print (maxdeltas[i][0],maxdeltas[i][1], maxdeltas[i][1],"%.2f" % maxdeltas2[i])