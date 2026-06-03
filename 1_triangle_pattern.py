# Triangle Pattern Program (without built-in functions)

rows = int(input("enter the number of rows: "))

i = 1
while i <= rows:
    j = 1
    while j <= i:
        print("*", end=" ")
        j = j + 1
    print()
    i = i + 1
