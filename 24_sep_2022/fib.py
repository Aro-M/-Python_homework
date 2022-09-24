def Fib(n):
    if n <= 0:
        print("Incorrect value")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fib(n - 1) + Fib(n - 2)
x  = int(input("input a  value "))
print(Fib(x))
