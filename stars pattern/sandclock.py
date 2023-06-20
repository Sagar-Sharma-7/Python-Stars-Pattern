# Hourglass pattern
n = 5
for i in range(n):
    print(" " * i +  "*" * (2 * (n-i -1) + 1))
for j in range(n):
    print(" " * (n-j-1) + "*" * (2 * j + 1))