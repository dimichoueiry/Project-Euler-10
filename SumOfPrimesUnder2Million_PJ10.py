
added = 2

#mine, slow af
for i in range (1, 2000000,2):
    over = 0
    
    for j in range (2, i+1):
        i%j
        if i%j ==0:
            over +=1
        elif over >1:
            break
    if over == 1:
        added += i
print(added)


# project euler fast
from math import sqrt


def is_prime(number):
    if number < 2: return False
    if number % 2 == 0: return False
    n = 3
    while n <= sqrt(number):
        if number % n == 0:
            return False
        n += 2
    return True


def primes_sum_below(limit: int):
    n = 1
    sum = 2
    while n < limit:
        if is_prime(n):
            print(n)
            sum += n
        n += 2
    return sum


print(primes_sum_below(2_000_000))

    