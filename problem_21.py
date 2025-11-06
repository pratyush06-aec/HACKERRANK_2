import math

def find_angle(a, b):
    rad= math.acos(b/math.sqrt(a**2+b**2))
    deg= math.degrees(rad)
    return round(deg)

c= int(input())
d= int(input())
print(f"{find_angle(c, d)}°")