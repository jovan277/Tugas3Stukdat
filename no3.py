def fib(n):
    l=[]
    a, b = 1, 1
    while a < n:
        l.append(a)
        a, b = b, a+b
        print(''.join(str(li) for li in l))
fib(int(input("Masukkan angka : ")))