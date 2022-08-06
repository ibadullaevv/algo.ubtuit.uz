from math import pi

h, r = map(int, input().split())
v = (pi * r * r * h) / 3
print('%.2f' % v)
