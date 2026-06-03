# Squares of Numbers Based on User Input

n = int(input("Enter how many numbers you want: "))

i = 0
while i < n:
    num = int(input("Enter number: "))
    square = num * num
    print("Square of", num, "=", square)
    i = i + 1
