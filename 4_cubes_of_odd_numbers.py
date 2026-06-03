# Convert List into Cubes of Numbers (Only Odd Numbers)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Original list:", numbers)
print()

cubed_odds = []

i = 0
while i < len(numbers):
    num = numbers[i]
    if num % 2 != 0:  # Check if odd
        cube = num * num * num
        cubed_odds = cubed_odds + [cube]
    i = i + 1

print("Cubes of odd numbers:", cubed_odds)
