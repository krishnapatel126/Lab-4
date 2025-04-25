n = int(input("Enter a Number: "))

if n <= 1:
    is_prime = False
else:
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
print("Prime:", is_prime)

divisors = [i for i in range(1, n) if n % i == 0]
if sum(divisors) == n:
    print("Perfect: True")
else:
    print("Perfect: False")

num_str = str(n)
power = len(num_str)
sum_of_powers = sum(int(digit) ** power for digit in num_str)
if sum_of_powers == n:
    print("Armstrong: True")
else:
    print("Armstrong: False")

if str(n) == str(n)[::-1]:
    print("Palindrome: True")
else:
    print("Palindrome: False")


square = n * n
if str(square).endswith(str(n)):
    print("Automorphic: True")
else:
    print("Automorphic: False")
