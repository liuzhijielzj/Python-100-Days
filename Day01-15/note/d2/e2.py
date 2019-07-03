import math
radius = float(input('plz input radius of the circle: '))
perimeter = 2 * math.pi * radius
area = math.pi * (radius ** 2)
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)