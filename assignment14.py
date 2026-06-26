# 1. Sum of Digits
print("1. Sum of Digits")
num = int(input("Enter a number: "))
temp = num
sum_digits = 0

while temp > 0:
    digit = temp % 10
    sum_digits += digit
    temp //= 10

print("Sum of Digits =", sum_digits)



# 2. Reverse a Number
print("\n2. Reverse a Number")
num = int(input("Enter a number: "))
temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

print("Reverse =", reverse)




# 3. Count Digits
print("\n3. Count Digits")
num = int(input("Enter a number: "))
temp = num
count = 0

while temp > 0:
    count += 1
    temp //= 10

print("Number of Digits =", count)




# 4. Even or Odd
print("\n4. Even or Odd")
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")




# 5. Prime Number
print("\n5. Prime Number")
num = int(input("Enter a number: "))

count = 0

for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Prime Number")
else:
    print("Not a Prime Number")




# 6. Factorial
print("\n6. Factorial")
num = int(input("Enter a number: "))

fact = 1

for i in range(1, num + 1):
    fact *= i

print("Factorial =", fact)




# 7. Factors of a Number
print("\n7. Factors of a Number")
num = int(input("Enter a number: "))

print("Factors are:")

for i in range(1, num + 1):
    if num % i == 0:
        print(i, end=" ")

print()




# 8. Palindrome Number
print("\n8. Palindrome Number")
num = int(input("Enter a number: "))

temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //= 10

if num == reverse:
    print("Palindrome")
else:
    print("Not a Palindrome")




# 9. Armstrong Number
print("\n9. Armstrong Number")
num = int(input("Enter a number: "))

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
print("\n10. GCD (HCF)")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

gcd = 1

for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        gcd = i

print("GCD =", gcd)