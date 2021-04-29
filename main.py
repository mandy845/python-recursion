def Fib(n):
    if n <= 1:
        return n
    else:
        return Fib(n - 1) + Fib(n - 2)
nterms = int(input("Enter the number of terms"))

if nterms <= 0:
    print ("Error")
else:
    print("Fibonacci sequence :")
    for i in range(nterms):
        print(Fib(i))