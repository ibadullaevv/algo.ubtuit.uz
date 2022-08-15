from math import sqrt, log

a, x = map(float, input().split())

b = sqrt(x - 1) + sqrt(x + 2) + log((sqrt(a * x ** 2) + 2), 10)
c = sqrt(sqrt(x + 2) + sqrt(x + 24) + x ** 5)
TT = b / c

print('%.2f' % TT)
