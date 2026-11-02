class CircularQueue:
    def __init__(self, capacity):
        """
        Initializes the Circular Queue with a predefined fixed capacity.
        """
        self.capacity = capacity
        self.queue = [None] * capacity  # Simulating a fixed-size array
        self.front = -1
        self.rear = -1

    def is_full(self):
        """Checks if the queue is full."""
        return (self.rear + 1) % self.capacity == self.front

    def is_empty(self):
        """Checks if the queue is empty."""
        return self.front == -1

    def enqueue(self, data):
        """Inserts an element into the circular queue."""
        if self.is_full():
            print("❌ Queue Overflow! Cannot enqueue. The queue is full.")
            return

        # If insertion is for the first element
        if self.is_empty():
            self.front = 0
            self.rear = 0
        else:
            # Circularly increment the rear pointer
            self.rear = (self.rear + 1) % self.capacity

        self.queue[self.rear] = data
        print(f"📥 Successfully enqueued: {data}")

    def dequeue(self):
        """Removes an element from the front of the circular queue."""
        if self.is_empty():
            print("❌ Queue Underflow! Cannot dequeue. The queue is empty.")
            return None

        removed_element = self.queue[self.front]
        self.queue[self.front] = None  # Clear the slot

        # If only one element was left, reset the queue pointers
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            # Circularly increment the front pointer
            self.front = (self.front + 1) % self.capacity

        print(f"📤 Successfully dequeued: {removed_element}")
        return removed_element

    def peek(self):
        """Returns the front element without removing it."""
        if self.is_empty():
            print("⚠️ The queue is empty. No front element.")
            return None
        print(f"👀 Front element (Peek): {self.queue[self.front]}")
        return self.queue[self.front]

    def display(self):
        """Displays all elements currently present in the queue."""
        if self.is_empty():
            print("📁 Queue is empty.")
            return

        print("📋 Current Queue Elements: ", end="")
        if self.rear >= self.front:
            # Elements are stored in a contiguous block
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" -> ")
        else:
            # Elements have wrapped around the array boundary
            for i in range(self.front, self.capacity):
                print(self.queue[i], end=" -> ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" -> ")
        print("End")


def main():
    print("--- Circular Queue Implementation ---")
    while True:
        try:
            size = int(input("Enter the fixed capacity of the Circular Queue: "))
            if size <= 0:
                print("Size must be greater than 0. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    cq = CircularQueue(size)

    while True:
        print("\n=== CIRCULAR QUEUE MENU ===")
        print("1. Enqueue (Insert)")
        print("2. Dequeue (Delete)")
        print("3. Peek (Front Element)")
        print("4. Display Queue")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            value = input("Enter the element to enqueue: ")
            cq.enqueue(value)
        elif choice == "2":
            cq.dequeue()
        elif choice == "3":
            cq.peek()
        elif choice == "4":
            cq.display()
        elif choice == "5":
            print("Shutting down the program. Goodbye!")
            break
        else:
            print("❌ Invalid Choice! Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
