# Circular Linked List (CLL)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # 1. Create Linked List
    def create(self):
        n = int(input("Enter number of nodes: "))

        for i in range(n):
            data = int(input("Enter data: "))
            self.insert_end(data)

        print("Circular Linked List created successfully.")

    # 2. Insert at Beginning
    def insert_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        new_node.next = self.head
        temp.next = new_node
        self.head = new_node

    # 3. Insert at End
    def insert_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        temp.next = new_node
        new_node.next = self.head

    # 4. Insert at Index
    def insert_at_index(self, data, index):
        if index < 0:
            print("Invalid index.")
            return

        if index == 0:
            self.insert_beginning(data)
            return

        if self.head is None:
            print("List is empty. Only index 0 is allowed.")
            return

        new_node = Node(data)
        temp = self.head
        count = 0

        while count < index - 1 and temp.next != self.head:
            temp = temp.next
            count += 1

        if count != index - 1:
            print("Index out of range.")
            return

        new_node.next = temp.next
        temp.next = new_node

    # 5. Delete by Value
    def delete_by_value(self, value):
        if self.head is None:
            print("List is empty.")
            return

        # If head has the value
        if self.head.data == value:

            # Only one node
            if self.head.next == self.head:
                self.head = None
                print("Node deleted.")
                return

            temp = self.head

            while temp.next != self.head:
                temp = temp.next

            temp.next = self.head.next
            self.head = self.head.next

            print("Node deleted.")
            return

        # Search for the value
        prev = self.head
        curr = self.head.next

        while curr != self.head:
            if curr.data == value:
                prev.next = curr.next
                print("Node deleted.")
                return

            prev = curr
            curr = curr.next

        print("Value not found.")

    # 6. Delete Prior Node
    def delete_prior_node(self, value):
        if self.head is None or self.head.next == self.head:
            print("Not enough nodes.")
            return

        # If value is at head, delete last node
        if self.head.data == value:
            self.delete_last()
            return

        prev = self.head
        curr = self.head.next

        while curr != self.head:
            if curr.data == value:

                # If curr is second node
                if prev == self.head:
                    self.delete_first()
                    return

                # Find node before prev
                before_prev = self.head

                while before_prev.next != prev:
                    before_prev = before_prev.next

                before_prev.next = curr
                print("Prior node deleted.")
                return

            prev = curr
            curr = curr.next

        print("Value not found.")

    # Helper function: Delete first node
    def delete_first(self):
        if self.head is None:
            return

        if self.head.next == self.head:
            self.head = None
            return

        temp = self.head

        while temp.next != self.head:
            temp = temp.next

        temp.next = self.head.next
        self.head = self.head.next

    # 7. Delete Last Node
    def delete_last(self):
        if self.head is None:
            print("List is empty.")
            return

        if self.head.next == self.head:
            self.head = None
            print("Last node deleted.")
            return

        temp = self.head

        while temp.next.next != self.head:
            temp = temp.next

        temp.next = self.head
        print("Last node deleted.")

    # 8. Count Number of Nodes
    def count_nodes(self):
        if self.head is None:
            return 0

        count = 1
        temp = self.head.next

        while temp != self.head:
            count += 1
            temp = temp.next

        return count

    # 9. Display / Traverse
    def display(self):
        if self.head is None:
            print("List is empty.")
            return

        temp = self.head

        print("Circular Linked List:")

        while True:
            print(temp.data, end=" -> ")
            temp = temp.next

            if temp == self.head:
                break

        print("(back to head)")


# Main Program
cll = CircularLinkedList()

while True:

    print("\n========== CIRCULAR LINKED LIST ==========")
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
        cll.create()

    elif choice == 2:
        data = int(input("Enter data: "))
        cll.insert_beginning(data)

    elif choice == 3:
        data = int(input("Enter data: "))
        cll.insert_end(data)

    elif choice == 4:
        data = int(input("Enter data: "))
        index = int(input("Enter index: "))
        cll.insert_at_index(data, index)

    elif choice == 5:
        value = int(input("Enter value to delete: "))
        cll.delete_by_value(value)

    elif choice == 6:
        value = int(input("Enter value whose prior node should be deleted: "))
        cll.delete_prior_node(value)

    elif choice == 7:
        cll.delete_last()

    elif choice == 8:
        print("Number of nodes:", cll.count_nodes())

    elif choice == 9:
        cll.display()

    elif choice == 10:
        print("Program terminated.")
        break

    else:
        print("Invalid choice.")
