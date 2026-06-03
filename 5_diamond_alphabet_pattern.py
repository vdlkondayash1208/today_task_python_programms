rows = int(input("enter the number of rows: "))

# Combine upper + lower using one loop
for i in range(1, 2 * rows):
    if i <= rows:
        n = i
    else:
        n = 2 * rows - i

    # spaces
    print(" " * (rows - n), end="")

    # forward letters
    for j in range(n):
        print(chr(65 + j), end="")

    # backward letters
    for j in range(n - 2, -1, -1):
        print(chr(65 + j), end="")

    print()