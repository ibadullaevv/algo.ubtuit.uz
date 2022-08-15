from math import sqrt, sin, fabs, log, e

a, x, y = map(float, input().split())

W2 = sqrt(e ** (x * y) - x * sin(a * x) - (x * x + 2) / (fabs(x) + 5)) + sqrt(log((x * x + 2), e) + 5)

print('%.2f' % W2)
