class Node:
    """Class to represent a single node in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    """Class to manage stack operations using a linked list."""
    def __init__(self):
        self.top = None  # Pointer to the topmost element of the stack

    def is_empty(self):
        """Checks if the stack is empty."""
        return self.top is None

    def push(self, data):
        """Adds a new element to the top of the stack."""
        new_node = Node(data)
        new_node.next = self.top  # Link the new node to the old top
        self.top = new_node       # Move top pointer to the new node
        print(f"Successfully pushed {data} onto the stack.")

    def pop(self):
        """Removes and returns the top element from the stack."""
        if self.is_empty():
            print("Stack Underflow! The stack is empty.")
            return None
        
        popped_node = self.top    # Save the current top node
        self.top = self.top.next  # Move top pointer to the next node
        popped_node.next = None   # Unlink the removed node
        return popped_node.data

    def peek(self):
        """Returns the top element without removing it."""
        if self.is_empty():
            print("The stack is empty.")
            return None
        return self.top.data

    def display(self):
        """Displays all elements in the stack from top to bottom."""
        if self.is_empty():
            print("The stack is empty.")
            return
        
        print("\n--- Current Stack Elements (Top to Bottom) ---")
        current = self.top
        while current:
            print(f"| {current.data} |")
            current = current.next
            if current:
                print("  ↓  ")
        print("-----------------------------------------------\n")


# Menu-driven interaction block
if __name__ == "__main__":
    stack = Stack()
    
    while True:
        print("\n*** STACK OPERATIONS MENU ***")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")
        
        try:
            choice = int(input("Enter your choice (1-5): "))
            
            if choice == 1:
                element = input("Enter the value to push: ")
                stack.push(element)
            elif choice == 2:
                popped_val = stack.pop()
                if popped_val is not None:
                    print(f"Popped element: {popped_val}")
            elif choice == 3:
                top_val = stack.peek()
                if top_val is not None:
                    print(f"Top element (Peek): {top_val}")
            elif choice == 4:
                stack.display()
            elif choice == 5:
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice! Please select an option between 1 and 5.")
        except ValueError:
            print("Invalid input! Please enter a numerical choice.")
