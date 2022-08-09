    from math import e, fabs, pow
x , y= map(float,input().split())

a  = x + y
b = y*y + abs( (y*y+2)/(x + (x*x*x)/5) )
c = pow(e, (y+2))
c1 = (a/b) + c

print('%.2f'%(c1)) 