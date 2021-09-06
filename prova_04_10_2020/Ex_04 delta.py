import math
a = 1
b = 2
c = -3
delta = (b**2)-4*a*c
if delta > 0:
    delta = math.sqrt(delta)
    r1 = (-b+delta)/(2*a)
    r2 = (-b-delta)/(2*a)
    print(r1,r2)