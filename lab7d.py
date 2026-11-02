class Node:
    """Represents a single node in the circular linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularQueueLinkedList:
    """Implements a Circular Queue using a Linked List data structure."""
    def __init__(self):
        # We only need to maintain the rear pointer.
        # rear.next will automatically point to the front node.
        self.rear = None

    def is_empty(self):
        """Checks if the queue is empty."""
        return self.rear is None

    def enqueue(self, data):
        """Inserts an element at the rear of the circular queue."""
        new_node = Node(data)
        
        if self.is_empty():
            # If the queue is empty, the new node points to itself
            new_node.next = new_node
            self.rear = new_node
        else:
            # New node points to the current front (rear.next)
            new_node.next = self.rear.next
            # Current rear points to the new node
            self.rear.next = new_node
            # Move the rear pointer to the new node
            self.rear = new_node
        print(f"Successfully enqueued: {data}")

    def dequeue(self):
        """Removes and returns the front element from the queue."""
        if self.is_empty():
            print("Queue Underflow! The queue is empty.")
            return None
        
        front = self.rear.next
        removed_data = front.data
        
        # If there is only one node in the queue
        if self.rear == front:
            self.rear = None
        else:
            # Bypass the front node to isolate it
            self.rear.next = front.next
            
        print(f"Successfully dequeued: {removed_data}")
        return removed_data

    def peek(self):
        """Returns the front element without removing it."""
        if self.is_empty():
            print("The queue is empty. Nothing to peek.")
            return None
        
        front = self.rear.next
        return front.data

    def display(self):
        """Displays all the elements present in the circular queue."""
        if self.is_empty():
            print("Queue is empty.")
            return
        
        print("Circular Queue elements: ", end="")
        front = self.rear.next
        temp = front
        
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == front:
                break
        print("(back to front)")


def main():
    """Menu-driven interface for the Circular Queue."""
    cq = CircularQueueLinkedList()
    
    while True:
        print("\n--- CIRCULAR QUEUE OPERATIONS ---")
        print("1. Enqueue (Insert)")
        print("2. Dequeue (Delete)")
        print("3. Peek (Front Element)")
        print("4. Display Queue")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()
        
        if choice == '1':
            value = input("Enter the value to enqueue: ")
            cq.enqueue(value)
        elif choice == '2':
            cq.dequeue()
        elif choice == '3':
            front_val = cq.peek()
            if front_val is not None:
                print(f"Front element is: {front_val}")
        elif choice == '4':
            cq.display()
        elif choice == '5':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option from 1 to 5.")


if __name__ == "__main__":
    main()
