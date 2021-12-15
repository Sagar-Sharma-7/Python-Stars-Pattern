n = 5
for i in range(n):
    print(" " * (n-i-1) + "*" * (2*i + 1))
for j in range(n):
    print(" " * j + "*" * (2 * (n-j -1) + 1))