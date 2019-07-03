x = int(input('x = '))
y = int(input('y = '))
if x > y:
    x, y = y, x # swap variable in one line

for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('The GCD of %d and %d is ' % (x, y, factor))
        print('The LCM of %d and %d is ' % (x, y, x * y // factor))
        break
        
