numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []

not_primes = []

is_prime = True

for number in numbers:
    if number < 2:
        continue
    for i in range(2, number):
        if number % i == 0:
            not_primes.append(number)
            is_prime = False
            break
    if is_prime:
        primes.append(number)
    is_prime = True

print('primes:', primes)
print('not_primes:', not_primes)
