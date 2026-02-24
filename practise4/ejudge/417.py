import math

# Ввод данных
R = float(input())
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

dx = x2 - x1
dy = y2 - y1

length_AB = math.hypot(dx, dy)

a = dx**2 + dy**2
b = 2 * (dx*x1 + dy*y1)
c = x1**2 + y1**2 - R**2

discriminant = b**2 - 4*a*c

if discriminant < 0:
    print("0.0000000000")
else:
    sqrt_D = math.sqrt(discriminant)
    t1 = (-b - sqrt_D) / (2*a)
    t2 = (-b + sqrt_D) / (2*a)
    
    t_start = max(0, min(t1, t2))
    t_end = min(1, max(t1, t2))
    
    if t_start > t_end:
        print("0.0000000000")
    else:
        inside_length = (t_end - t_start) * length_AB
        print(f"{inside_length:.10f}")