from math import fabs, sin, tan, sqrt, pow

x1, x2, c, d = map(float, input().split())
# c, d = map(int,input().split())

a = pow(sin(fabs(c * x2 ** 3 + d * x1 ** 3 - c * d)), 2)

b = sqrt(c * x1 ** 2 + d * x2 ** 2 + 7)

f = tan(x1 * x2 ** 2 + d ** 3)

G = fabs(a / b) + f

print('%.2f' % G)
