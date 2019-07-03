from e3 import is_prime
def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num

if __name__ == '__main__':
    num = int(input('plz input a positive nubmer'))
    if is_palindrome(num) and is_prime(num):
        print('%d is a prime palindrome' % num)