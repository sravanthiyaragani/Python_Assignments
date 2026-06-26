# 1. Sum of Digits
num = int(input("Enter a number: "))
temp = num
sum_digits = 0

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    temp //= 10

print("Sum of Digits =", sum_digits)


# 2. Reverse a Number
num = int(input("\nEnter a number: "))
temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

print("Reverse Number =", reverse)


# 3. Count Digits
num = int(input("\nEnter a number: "))
temp = num
count = 0

while temp > 0:
    count += 1
    temp //= 10

print("Number of Digits =", count)


# 4. Check Even or Odd
num = int(input("\nEnter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# 5. Check Prime Number
num = int(input("\nEnter a number: "))

flag = True

if num <= 1:
    flag = False
else:
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break

if flag:
    print("Prime Number")
else:
    print("Not a Prime Number")


# 6. Factorial
num = int(input("\nEnter a number: "))

fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)


# 7. Factors of a Number
num = int(input("\nEnter a number: "))

print("Factors are:")
for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")

print()


# 8. Palindrome Number
num = int(input("\nEnter a number: "))

original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original == reverse:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")


# 9. Armstrong Number
num = int(input("\nEnter a number: "))

original = num
length = len(str(num))
total = 0

while num > 0:
    digit = num % 10
    total += digit ** length
    num //= 10

if total == original:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")


# 10. GCD (HCF)
a = int(input("\nEnter First Number: "))
b = int(input("Enter Second Number: "))

small = a if a < b else b

gcd = 1

for i in range(1, small + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print("GCD =", gcd)