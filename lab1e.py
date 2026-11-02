def fibonacci(n, a=0, b=1):
    if n == 0:
        return

    print(a, end=" ")
    fibonacci(n - 1, b, a + b)


n = int(input("Enter number of terms: "))

fibonacci(n)
