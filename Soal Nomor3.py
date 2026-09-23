n = int(input("Masukkan Angka Fibonacci : "))

a = 0
b = 1
i = 0

while i < n:
    print(a, end=" ")

    a,b = b, a + b

    i = i + 1