class Queue:
    def __init__(self, capacity):
        """
        Initializes the queue with a fixed capacity.
        In Python, a standard list acts as the underlying array.
        """
        self.capacity = capacity
        self.queue = []

    def is_full(self):
        """Checks if the queue has reached its maximum capacity."""
        return len(self.queue) == self.capacity

    def is_empty(self):
        """Checks if the queue contains no elements."""
        return len(self.queue) == 0

    def enqueue(self, item):
        """Adds an item to the rear of the queue."""
        if self.is_full():
            print("\n❌ Queue Overflow! Cannot add item. The queue is full.")
        else:
            self.queue.append(item)
            print(f"\n✅ Successfully enqueued: {item}")

    def dequeue(self):
        """Removes and returns the item at the front of the queue."""
        if self.is_empty():
            print("\n❌ Queue Underflow! Cannot remove item. The queue is empty.")
            return None
        else:
            # pop(0) removes the element at the index 0 (front of the queue)
            removed_item = self.queue.pop(0)
            print(f"\n✅ Successfully dequeued: {removed_item}")
            return removed_item

    def peek(self):
        """Returns the item at the front without removing it."""
        if self.is_empty():
            print("\n❌ The queue is empty. Nothing to peek.")
            return None
        else:
            front_item = self.queue[0]
            print(f"\n🔍 Front element (Peek): {front_item}")
            return front_item

    def display(self):
        """Prints all elements in the queue from front to rear."""
        if self.is_empty():
            print("\n📋 The queue is currently empty.")
        else:
            print("\n📋 Current Queue status:")
            print("Front ->", " -> ".join(map(str, self.queue)), "-> Rear")
            print(f"Total elements: {len(self.queue)} / {self.capacity}")


def main():
    # Get max size for the array-based queue simulation
    while True:
        try:
            capacity = int(input("Enter the maximum capacity of the queue: "))
            if capacity > 0:
                break
            print("Please enter a positive integer greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Initialize the queue object
    my_queue = Queue(capacity)

    # Menu-driven interface
    while True:
        print("\n" + "="*30)
        print("      QUEUE OPERATIONS MENU")
        print("="*30)
        print("1. Enqueue (Insert element)")
        print("2. Dequeue (Remove element)")
        print("3. Peek (View front element)")
        print("4. Display Queue")
        print("5. Exit")
        print("="*30)

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            item = input("Enter the value to enqueue: ")
            my_queue.enqueue(item)
        
        elif choice == '2':
            my_queue.dequeue()
            
        elif choice == '3':
            my_queue.peek()
            
        elif choice == '4':
            my_queue.display()
            
        elif choice == '5':
            print("\n👋 Exiting the program. Goodbye!")
            break
            
        else:
            print("\n❌ Invalid choice! Please select a valid option between 1 and 5.")


if __name__ == "__main__":
    main()
