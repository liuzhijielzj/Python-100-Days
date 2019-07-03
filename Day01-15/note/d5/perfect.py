import time
import math

for num in range(1, 10000):
    sum = 1
    upper = int(math.sqrt(num)) + 1
    for factor in range(2, upper):
        if num % factor == 0:
            sum += factor
            if num / factor != factor:
                sum += num / factor
    if sum == num:
        print(num)