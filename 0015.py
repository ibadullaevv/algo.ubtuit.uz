r1 ,r2 ,r3 = map(int, input().split())

r = r1*r2*r3/( r2*r3+r1*r3+r1*r2 ) 

print('%.2f'%r)