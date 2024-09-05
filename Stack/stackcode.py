class Stack:
    # Constructor to initialize the stack
    def __init__(self):
        self.MAX = 4  # Define constant size for the stack
        self.top = -1  # Initialize top pointer
        self.inp_array = [0] * self.MAX  # Initialize array to store stack elements

    # Function to push an element onto the stack
    def push(self, value):
        if self.top == self.MAX - 1:
            print("Stack Overflow!!")
        else:
            self.top += 1
            self.inp_array[self.top] = value

    # Function to pop an element from the stack
    def pop(self):
        if self.top == -1:
            print("Stack Underflow!!")
        else:
            print("\nPopped element:", self.inp_array[self.top])
            self.top -= 1

    # Function to display the elements of the stack
    def show(self):
        if self.top == -1:
            print("Stack Underflow!!")
        else:
            print("\nElements present in the stack:")
            for i in range(self.top, -1, -1):
                print(self.inp_array[i])

# Main function
if __name__ == "__main__":
    stack = Stack()  # Initializing the stack
    while True:
        # Display menu for stack operations
        print("\nPerform operations on the stack:")
        print("1. Push the element")
        print("2. Pop the element")
        print("3. Show")
        print("4. End")
        option = int(input("\nEnter the choice: "))

        # Perform operation based on user's choice
        if option == 1:
            value = int(input("Enter the value you want to push: "))
            stack.push(value)  # Call push function
        elif option == 2:
            stack.pop()  # Call pop function
        elif option == 3:
            stack.show()  # Call show function
        elif option == 4:
            break  # Exit the program
        else:
            print("\nInvalid choice!!")
