from math import pow, fabs, cos, sin

x, y = map(float, input().split())

a = x**2+1
b = x**2 + (x*y+y**2)/(y**2+( (y+x*y)/(fabs(x*y)+5) ))
c = 1/( 1+cos(x)+1/sin(fabs(x)) )
d = (a/b) + c

print('%.2f'%d)