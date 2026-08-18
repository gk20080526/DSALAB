def launch(n):
    for i in range(n, -1, -1):
        if i == 0:
            print("launch")
        else:
            print(i)

n = int(input("Enter countdown number: "))
launch(n)
