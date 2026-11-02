class Node:
    """A class representing a single node in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    """A class representing a queue using a linked list."""
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        """Checks if the queue is empty."""
        return self.front is None

    def enqueue(self, item):
        """Adds an item to the rear of the queue."""
        new_node = Node(item)
        
        # If the queue is empty, the new node becomes both front and rear
        if self.rear is None:
            self.front = self.rear = new_node
            print(f"Successfully enqueued: {item}")
            return
            
        # Add the new node at the end of the queue and change rear
        self.rear.next = new_node
        self.rear = new_node
        print(f"Successfully enqueued: {item}")

    def dequeue(self):
        """Removes and returns the item from the front of the queue."""
        if self.is_empty():
            print("Queue Underflow! The queue is empty.")
            return None
        
        # Store previous front and move front one node ahead
        temp = self.front
        self.front = temp.next

        # If front becomes None, then change rear also as None
        if self.front is None:
            self.rear = None
            
        print(f"Successfully dequeued: {temp.data}")
        return temp.data

    def peek(self):
        """Returns the item at the front of the queue without removing it."""
        if self.is_empty():
            print("Queue is empty! Nothing to peek.")
            return None
        return self.front.data

    def display(self):
        """Displays all elements currently in the queue."""
        if self.is_empty():
            print("Queue is empty!")
            return
        
        print("Queue elements (Front to Rear): ", end="")
        current = self.front
        while current:
            print(current.data, end=" -> " if current.next else "\n")
            current = current.next


def main():
    """Menu-driven interface for the queue operations."""
    q = Queue()
    
    while True:
        print("\n--- Queue Operations Menu ---")
        print("1. Enqueue (Insert)")
        print("2. Dequeue (Delete)")
        print("3. Peek (Front Element)")
        print("4. Display Queue")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            item = input("Enter the value to enqueue: ")
            q.enqueue(item)
        elif choice == '2':
            q.dequeue()
        elif choice == '3':
            front_item = q.peek()
            if front_item is not None:
                print(f"Element at the front is: {front_item}")
        elif choice == '4':
            q.display()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option between 1 and 5.")

if __name__ == "__main__":
    main()
