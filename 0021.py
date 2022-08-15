from math import pow

a, b = map(float, input().split())

T = pow(a, 1 / 5) + pow((b * (a + b) / (2 * b + a * b)), 1 / 4) * (a ** 2 + b ** 2 + 2)

print('%.2f' % T)
