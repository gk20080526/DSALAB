
SIZE = 10


# 1. SEPARATE CHAINING
class SeparateChaining:
    def __init__(self):
        self.table = [[] for _ in range(SIZE)]

    def insert(self, key):
        index = key % SIZE
        if key not in self.table[index]:
            self.table[index].append(key)
        print("Inserted successfully.")

    def search(self, key):
        index = key % SIZE
        return key in self.table[index]

    def delete(self, key):
        index = key % SIZE
        if key in self.table[index]:
            self.table[index].remove(key)
            print("Deleted successfully.")
        else:
            print("Key not found.")

    def display(self):
        for i in range(SIZE):
            print(i, ":", self.table[i])


# 2. LINEAR PROBING
class LinearProbing:
    def __init__(self):
        self.table = [None] * SIZE

    def insert(self, key):
        index = key % SIZE

        for i in range(SIZE):
            pos = (index + i) % SIZE

            if self.table[pos] == key:
                print("Key already exists.")
                return

            if self.table[pos] is None:
                self.table[pos] = key
                print("Inserted successfully.")
                return

        print("Hash table is full.")

    def search(self, key):
        index = key % SIZE

        for i in range(SIZE):
            pos = (index + i) % SIZE

            if self.table[pos] is None:
                return False

            if self.table[pos] == key:
                return True

        return False

    def delete(self, key):
        index = key % SIZE

        for i in range(SIZE):
            pos = (index + i) % SIZE

            if self.table[pos] is None:
                print("Key not found.")
                return

            if self.table[pos] == key:
                self.table[pos] = "DELETED"
                print("Deleted successfully.")
                return

        print("Key not found.")

    def display(self):
        for i in range(SIZE):
            print(i, ":", self.table[i])


# 3. QUADRATIC PROBING
class QuadraticProbing:
    def __init__(self):
        self.table = [None] * SIZE

    def insert(self, key):
        index = key % SIZE

        for i in range(SIZE):
            pos = (index + i * i) % SIZE

            if self.table[pos] == key:
                print("Key already exists.")
                return

            if self.table[pos] is None or self.table[pos] == "DELETED":
                self.table[pos] = key
                print("Inserted successfully.")
                return

        print("Insertion failed. No available position.")

    def search(self, key):
        index = key % SIZE

        for i in range(SIZE):
            pos = (index + i * i) % SIZE

            if self.table[pos] is None:
                return False

            if self.table[pos] == key:
                return True

        return False

    def delete(self, key):
        index = key % SIZE

        for i in range(SIZE):
            pos = (index + i * i) % SIZE

            if self.table[pos] is None:
                print("Key not found.")
                return

            if self.table[pos] == key:
                self.table[pos] = "DELETED"
                print("Deleted successfully.")
                return

        print("Key not found.")

    def display(self):
        for i in range(SIZE):
            print(i, ":", self.table[i])


# MAIN MENU
chaining = SeparateChaining()
linear = LinearProbing()
quadratic = QuadraticProbing()

while True:
    print("\n--- HASHING ---")
    print("1. Separate Chaining")
    print("2. Linear Probing")
    print("3. Quadratic Probing")
    print("4. Exit")

    method = int(input("Choose hashing method: "))

    if method == 4:
        print("Program terminated.")
        break

    if method not in [1, 2, 3]:
        print("Invalid choice.")
        continue

    if method == 1:
        h = chaining
    elif method == 2:
        h = linear
    else:
        h = quadratic

    while True:
        print("\n1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. Display")
        print("5. Back to main menu")

        op = int(input("Enter operation: "))

        if op == 1:
            key = int(input("Enter key: "))
            h.insert(key)

        elif op == 2:
            key = int(input("Enter key: "))
            if h.search(key):
                print("Key found.")
            else:
                print("Key not found.")

        elif op == 3:
            key = int(input("Enter key: "))
            h.delete(key)

        elif op == 4:
            h.display()

        elif op == 5:
            break

        else:
            print("Invalid operation.")
