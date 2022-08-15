from math import sqrt, fabs, cos

a, b, c, x = map(float, input().split())

q = 8.2 * x ** 2 + sqrt(fabs(x ** 3 + 3 * x) + cos(x - 2))
w = a / 4 + b / 3 + c / 2 + 1
w1 = 0.75 + q / w

print('%.2f' % w1)
