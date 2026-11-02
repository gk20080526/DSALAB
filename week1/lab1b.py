def power(P, n):
    if n == 0:
        return 1
    else:
        return P * power(P, n - 1)

P = int(input("Enter P: "))
n = int(input("Enter n: "))

result = power(P, n)
print("P^n =", result)
