# Python Program to Implement Doubly Linked List (DLL)

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # 1. Create Linked List
    def create(self):
        n = int(input("Enter number of nodes: "))

        for i in range(n):
            data = int(input("Enter data: "))
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
            else:
                temp = self.head

                while temp.next is not None:
                    temp = temp.next

                temp.next = new_node
                new_node.prev = temp

        print("Doubly Linked List created successfully.")

    # 2. Insert at Beginning
    def insert_beginning(self):
        data = int(input("Enter data: "))
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        print("Node inserted at beginning.")

    # 3. Insert at End
    def insert_end(self):
        data = int(input("Enter data: "))
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next is not None:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

        print("Node inserted at end.")

    # 4. Insert at Index
    def insert_index(self):
        index = int(input("Enter index: "))
        data = int(input("Enter data: "))

        new_node = Node(data)

        # Insert at beginning
        if index == 0:
            if self.head is None:
                self.head = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node

            print("Node inserted at index", index)
            return

        temp = self.head
        count = 0

        while temp is not None and count < index:
            temp = temp.next
            count += 1

        if temp is None:
            print("Invalid index.")
            return

        new_node.prev = temp.prev
        new_node.next = temp

        temp.prev.next = new_node
        temp.prev = new_node

        print("Node inserted at index", index)

    # 5. Delete by Value
    def delete_by_value(self):
        value = int(input("Enter value to delete: "))

        temp = self.head

        while temp is not None and temp.data != value:
            temp = temp.next

        if temp is None:
            print("Value not found.")
            return

        # If deleting first node
        if temp.prev is None:
            self.head = temp.next

            if self.head is not None:
                self.head.prev = None

        else:
            temp.prev.next = temp.next

            if temp.next is not None:
                temp.next.prev = temp.prev

        print("Node with value", value, "deleted.")

    # 6. Delete Prior Node
    def delete_prior_node(self):
        value = int(input("Enter value: "))

        temp = self.head

        while temp is not None and temp.data != value:
            temp = temp.next

        if temp is None:
            print("Value not found.")
            return

        # No node exists before the first node
        if temp.prev is None:
            print("No prior node exists.")
            return

        prior = temp.prev

        # If prior is the first node
        if prior.prev is None:
            self.head = temp
            temp.prev = None
        else:
            prior.prev.next = temp
            temp.prev = prior.prev

        print("Prior node of", value, "deleted.")

    # 7. Delete Last Node
    def delete_last(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head

        # Only one node
        if temp.next is None:
            self.head = None
            print("Last node deleted.")
            return

        while temp.next is not None:
            temp = temp.next

        temp.prev.next = None

        print("Last node deleted.")

    # 8. Count Number of Nodes
    def count_nodes(self):
        count = 0
        temp = self.head

        while temp is not None:
            count += 1
            temp = temp.next

        print("Number of nodes:", count)

    # 9. Display / Traverse
    def display(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head

        print("Doubly Linked List:", end=" ")

        while temp is not None:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")


# Main Program
dll = DoublyLinkedList()

while True:

    print("\n----- DOUBLY LINKED LIST -----")
    print("1. Create LL")
    print("2. Insert at Beginning")
    print("3. Insert at End")
    print("4. Insert at Index")
    print("5. Delete by Value")
    print("6. Delete Prior Node")
    print("7. Delete Last Node")
    print("8. Count Number of Nodes")
    print("9. Display / Traverse")
    print("10. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        dll.create()

    elif choice == 2:
        dll.insert_beginning()

    elif choice == 3:
        dll.insert_end()

    elif choice == 4:
        dll.insert_index()

    elif choice == 5:
        dll.delete_by_value()

    elif choice == 6:
        dll.delete_prior_node()

    elif choice == 7:
        dll.delete_last()

    elif choice == 8:
        dll.count_nodes()

    elif choice == 9:
        dll.display()

    elif choice == 10:
        print("Program exited.")
        break

    else:
        print("Invalid choice. Please try again.")
