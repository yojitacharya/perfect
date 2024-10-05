import math

def is_prime(n):
    if n < 2:
        return False
    j = 2
    while j*j <= n:
        if n % j == 0:
            return False
        j += 1
    return True

def sum_of_divisors(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum

def is_perfect(n):
    return sum_of_divisors(n) == n

found = False
i = 2
print("Started")
while not found:
    if is_prime(i) and is_perfect(i):
        print("Found prime perfect number:", i)
        found = True
        break
    if(i % 10000 == 0):
        print(i)
    i += 1
print("No Perfect Prime Found")