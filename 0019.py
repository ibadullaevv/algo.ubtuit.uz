from math import log, sqrt, fabs, cos, pow, e

x , y = map(int, input().split())

a = log( fabs( (x+y)**2 + sqrt(fabs(y) + 2) - ( x - x*y/(x*x/2 -5) )),e)
b = pow(cos(x+y),2)/pow((x+y),1/3)
c = a+b

print('%.2f'%(c))