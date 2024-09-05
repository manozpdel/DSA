#include <iostream>
using namespace std;

#define MAX 4

class Stack {
private:
    int top;
    int inp_array[MAX];

public:
    Stack() {
        top = -1;
    }

    void push(int value) {
        if (top == MAX - 1) {
            cout << "Stack Overflow!!"<<endl;
        } else {
            top = top + 1;
            inp_array[top] = value;
        }
    }

    void pop() {
        if (top == -1) {
            cout << "Stack Underflow!!";
        } else {
            cout << "\nPopped element: " << inp_array[top]<<endl;
            top = top - 1;
        }
    }

    void show() {
        if (top == -1) {
            cout << "Stack Underflow!!"<<endl;
        } else {
            cout << "\nElements present in the stack: \n";
            for (int i = top; i >= 0; --i)
                cout << inp_array[i] << endl;
        }
    }
};

int main() {
    int option,value;
    Stack stack;

    while (true) {
        cout << "\nPerform operations on the stack:";
        cout << "\n1.Push the element\n2.Pop the element\n3.Show\n4.End";
        cout << "\n\nEnter the choice: ";
        cin >> option;

        switch (option) {
            case 1:
                cout<<"Enter the value you want to push?"<<endl;
                cin>>value;
                stack.push(value);
                break;
            case 2:
                stack.pop();
                break;
            case 3:
                stack.show();
                break;
            case 4:
                return 0;
            default:
                cout << "\nInvalid choice!!";
        }
    }
}
