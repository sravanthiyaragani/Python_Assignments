digits = list(map(int, input("Enter digits separated by space: ").split()))

number = 0

# Convert list to number
for digit in digits:
    number = number * 10 + digit

# Add one
number += 1

# Convert number back to list
result = []

while number > 0:
    result.append(number % 10)
    number //= 10

result.reverse()

print("Output:", result)