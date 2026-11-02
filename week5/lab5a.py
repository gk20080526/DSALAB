class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Create LL
    def create(self):
        n = int(input("Enter number of nodes: "))

        for i in range(n):
            data = int(input("Enter element: "))
            self.insert_end(data)

    # 2. Insert at Beginning
    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # 3. Insert at End
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    # 4. Insert at Index
    def insert_index(self, data, index):
        if index == 0:
            self.insert_beginning(data)
            return

        new_node = Node(data)
        temp = self.head

        for i in range(index - 1):
            if temp is None:
                print("Invalid index")
                return
            temp = temp.next

        if temp is None:
            print("Invalid index")
            return

        new_node.next = temp.next
        temp.next = new_node

    # 5. Delete by Value
    def delete_value(self, value):
        if self.head is None:
            print("List is empty")
            return

        if self.head.data == value:
            self.head = self.head.next
            return

        temp = self.head

        while temp.next and temp.next.data != value:
            temp = temp.next

        if temp.next is None:
            print("Value not found")
        else:
            temp.next = temp.next.next

    # 6. Delete Prior Node
    def delete_prior(self, value):
        if self.head is None or self.head.next is None:
            print("No prior node exists")
            return

        if self.head.next.data == value:
            self.head = self.head.next
            return

        prev = None
        current = self.head
        next_node = self.head.next

        while next_node and next_node.data != value:
            prev = current
            current = next_node
            next_node = next_node.next

        if next_node is None:
            print("Value not found")
        else:
            if prev is None:
                self.head = next_node
            else:
                prev.next = next_node

    # 7. Delete Last Node
    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        temp = self.head

        while temp.next.next:
            temp = temp.next

        temp.next = None

    # 8. Count Nodes
    def count(self):
        count = 0
        temp = self.head

        while temp:
            count += 1
            temp = temp.next

        print("Number of nodes:", count)

    # 9. Display
    def display(self):
        temp = self.head

        if temp is None:
            print("List is empty")
            return

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


ll = SinglyLinkedList()

while True:
    print("\n--- SINGLY LINKED LIST ---")
    print("1. Create LL")
    print("2. Insert at Beginning")
    print("3. Insert at End")
    print("4. Insert at Index")
    print("5. Delete by Value")
    print("6. Delete Prior Node")
    print("7. Delete Last Node")
    print("8. Count Number of Nodes")
    print("9. Display/Traverse")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        ll.create()

    elif choice == 2:
        data = int(input("Enter value: "))
        ll.insert_beginning(data)

    elif choice == 3:
        data = int(input("Enter value: "))
        ll.insert_end(data)

    elif choice == 4:
        data = int(input("Enter value: "))
        index = int(input("Enter index: "))
        ll.insert_index(data, index)

    elif choice == 5:
        value = int(input("Enter value to delete: "))
        ll.delete_value(value)

    elif choice == 6:
        value = int(input("Enter value whose prior node is to be deleted: "))
        ll.delete_prior(value)

    elif choice == 7:
        ll.delete_last()

    elif choice == 8:
        ll.count()

    elif choice == 9:
        ll.display()

    elif choice == 10:
        print("Program ended")
        break

    else:
        print("Invalid choice")
