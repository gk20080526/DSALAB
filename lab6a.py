# Stack Implementation using Array

stack = []
MAX = 5

while True:
    print("\n===== STACK OPERATIONS =====")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    # Push
    if choice == 1:
        if len(stack) == MAX:
            print("Stack Overflow!")
        else:
            value = int(input("Enter value to push: "))
            stack.append(value)
            print(value, "pushed into stack.")

    # Pop
    elif choice == 2:
        if len(stack) == 0:
            print("Stack Underflow!")
        else:
            value = stack.pop()
            print(value, "popped from stack.")

    # Peek
    elif choice == 3:
        if len(stack) == 0:
            print("Stack is empty.")
        else:
            print("Top element is:", stack[-1])

    # Display
    elif choice == 4:
        if len(stack) == 0:
            print("Stack is empty.")
        else:
            print("Stack elements:")
            for i in range(len(stack) - 1, -1, -1):
                print(stack[i])

    # Exit
    elif choice == 5:
        print("Program terminated.")
        break

    else:
        print("Invalid choice!")
