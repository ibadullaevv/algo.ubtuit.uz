from math import atan, cos, fabs, pow, e

x, y = map(float, input().split())

a = 1/( x + (2/(x*x)) + (3/(x*x*x)) )
b = pow( e,(x*x + 3*x) )
c = atan( x+y ) + pow( fabs(5+x),2 )
d = pow( cos(y*y + ((x*x)/2)), 2 )

f2 = ((a+b)/c) - d

print('%.2f'%(f2) ) 