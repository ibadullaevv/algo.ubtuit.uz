from math import tan, cos, log, pi, log2

x , y= map(float,input().split())

a = 2 * tan(x + pi/6)
b = 1/3 + pow(cos(y + x*x), 2)
c = log( (x*x+2),2 )

f1 = a/b + c

print("%.2f"%f1)