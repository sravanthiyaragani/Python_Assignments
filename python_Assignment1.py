a = 10
b = 5

print("Arithmetic Operators")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponent:", a ** b)

print("\nComparison Operators")
print("a == b :", a == b)
print("a != b :", a != b)
print("a > b :", a > b)
print("a < b :", a < b)
print("a >= b :", a >= b)
print("a <= b :", a <= b)

print("\nAssignment Operators")
x = 10
print("Initial Value:", x)

x += 5
print("x += 5 :", x)

x -= 3
print("x -= 3 :", x)

x *= 2
print("x *= 2 :", x)

x /= 4
print("x /= 4 :", x)

print("\nLogical Operators")
print("(a > b) and (a < 20):", (a > b) and (a < 20))
print("(a < b) or (a < 20):", (a < b) or (a < 20))
print("not(a > b):", not(a > b))

print("\nBitwise Operators")
print("a & b :", a & b)
print("a | b :", a | b)
print("a ^ b :", a ^ b)
print("~a :", ~a)
print("a << 1 :", a << 1)
print("a >> 1 :", a >> 1)

print("\nMembership Operators")
list1 = [10, 20, 30, 40]
print("20 in list1 :", 20 in list1)
print("50 not in list1 :", 50 not in list1)

print("\nIdentity Operators")
m = [1, 2, 3]
n = m
p = [1, 2, 3]

print("m is n :", m is n)
print("m is p :", m is p)
print("m is not p :", m is not p)