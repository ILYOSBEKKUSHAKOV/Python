import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """Calculate and return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius

# Example usage:
if __name__ == "__main__":
    r = float(input("Enter the radius of the circle: "))
    circle = Circle(r)
    
    print(f"Area of the circle: {circle.area():.2f}")
    print(f"Perimeter of the circle: {circle.perimeter():.2f}")

from datetime import date, datetime

class Person:
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = datetime.strptime(dob, "%Y-%m-%d").date()

    def calculate_age(self):
        today = date.today()
        age = today.year - self.dob.year
        
        if (today.month, today.day) < (self.dob.month, self.dob.day):
            age -= 1
        
        return age

    def __str__(self):
        return f"Name: {self.name}, Country: {self.country}, Age: {self.calculate_age()}"

if __name__ == "__main__":
    name = input("Enter name: ")
    country = input("Enter country: ")
    dob = input("Enter date of birth (YYYY-MM-DD): ")

    person = Person(name, country, dob)
    print(person)

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error: Division by zero is not allowed."
        return a / b
if __name__ == "__main__":
    calc = Calculator()

    print("Simple Calculator")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    print(f"Addition: {calc.add(a, b)}")
    print(f"Subtraction: {calc.subtract(a, b)}")
    print(f"Multiplication: {calc.multiply(a, b)}")
    print(f"Division: {calc.divide(a, b)}")



import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement this method")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


if __name__ == "__main__":
    circle = Circle(5)
    triangle = Triangle(3, 4, 5)
    square = Square(4)

    print("=== Circle ===")
    print(f"Area: {circle.area():.2f}")
    print(f"Perimeter: {circle.perimeter():.2f}\n")

    print("=== Triangle ===")
    print(f"Area: {triangle.area():.2f}")
    print(f"Perimeter: {triangle.perimeter():.2f}\n")

    print("=== Square ===")
    print(f"Area: {square.area():.2f}")
    print(f"Perimeter: {square.perimeter():.2f}")


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_recursive(current_node.left, key)
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_recursive(current_node.right, key)
        else:
            print(f"Key {key} already exists in the tree.")

    def search(self, key):
        return self._search_recursive(self.root, key)

    def _search_recursive(self, current_node, key):
        if current_node is None:
            return False
        if key == current_node.key:
            return True
        elif key < current_node.key:
            return self._search_recursive(current_node.left, key)
        else:
            return self._search_recursive(current_node.right, key)

    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.key)
            self._inorder_recursive(node.right, result)


if __name__ == "__main__":
    bst = BinarySearchTree()
    elements = [50, 30, 70, 20, 40, 60, 80]

    for el in elements:
        bst.insert(el)

    print("Inorder Traversal (Sorted):", bst.inorder_traversal())

    key = int(input("Enter a number to search: "))
    if bst.search(key):
        print(f"{key} found in the tree.")
    else:
        print(f"{key} not found in the tree.")



class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)
        print(f"Pushed: {item}")

    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.items[-1]

    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack contents (top → bottom):", list(reversed(self.items)))


if __name__ == "__main__":
    stack = Stack()

    while True:
        print("\n--- Stack Menu ---")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Display")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter item to push: ")
            stack.push(item)
        elif choice == "2":
            popped_item = stack.pop()
            if popped_item is not None:
                print(f"Popped: {popped_item}")
        elif choice == "3":
            top_item = stack.peek()
            if top_item is not None:
                print(f"Top of stack: {top_item}")
        elif choice == "4":
            stack.display()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")





class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def display(self):
        if self.head is None:
            print("The linked list is empty.")
            return
        current = self.head
        print("Linked List:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"Inserted {data} at the end.")

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at the beginning.")

    def delete_node(self, key):
        current = self.head

        if current is None:
            print("List is empty. Nothing to delete.")
            return

        if current.data == key:
            self.head = current.next
            print(f"Deleted node with value {key}.")
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            print(f"Node with value {key} not found.")
            return

        prev.next = current.next
        print(f"Deleted node with value {key}.")


if __name__ == "__main__":
    ll = LinkedList()

    while True:
        print("\n--- Linked List Menu ---")
        print("1. Display list")
        print("2. Insert at beginning")
        print("3. Insert at end")
        print("4. Delete a node")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            ll.display()
        elif choice == "2":
            data = input("Enter data to insert at beginning: ")
            ll.insert_at_beginning(data)
        elif choice == "3":
            data = input("Enter data to insert at end: ")
            ll.insert_at_end(data)
        elif choice == "4":
            key = input("Enter data to delete: ")
            ll.delete_node(key)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")



class ShoppingCart:
    def __init__(self):
        self.items = {} 

    def add_item(self, item_name, price, quantity=1):
        if item_name in self.items:
            self.items[item_name][1] += quantity
        else:
            self.items[item_name] = [price, quantity]
        print(f"Added {quantity} x {item_name}(s) to the cart.")

    def remove_item(self, item_name, quantity=1):
        if item_name not in self.items:
            print(f"{item_name} not found in the cart.")
            return
        if quantity >= self.items[item_name][1]:
            del self.items[item_name]
            print(f"Removed all {item_name}(s) from the cart.")
        else:
            self.items[item_name][1] -= quantity
            print(f"Removed {quantity} x {item_name}(s) from the cart.")

    def calculate_total(self):
        total = sum(price * qty for price, qty in self.items.values())
        return total

    def display_cart(self):
        if not self.items:
            print("Your cart is empty.")
            return
        print("\n--- Shopping Cart ---")
        for item, (price, qty) in self.items.items():
            print(f"{item}: ${price:.2f} x {qty} = ${price * qty:.2f}")
        print(f"Total: ${self.calculate_total():.2f}")
        print("----------------------")


if __name__ == "__main__":
    cart = ShoppingCart()

    while True:
        print("\n--- Shopping Cart Menu ---")
        print("1. Add item")
        print("2. Remove item")
        print("3. View cart")
        print("4. View total")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            qty = int(input("Enter quantity: "))
            cart.add_item(name, price, qty)

        elif choice == "2":
            name = input("Enter item name to remove: ")
            qty = int(input("Enter quantity to remove: "))
            cart.remove_item(name, qty)

        elif choice == "3":
            cart.display_cart()

        elif choice == "4":
            total = cart.calculate_total()
            print(f"Total price of items in cart: ${total:.2f}")

        elif choice == "5":
            print("Thank you for shopping! Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")



class Stack:
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def push(self, item):
        """Push an item onto the stack."""
        self.items.append(item)
        print(f"Pushed {item} onto the stack.")

    def pop(self):
        """Pop the top item from the stack."""
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        popped_item = self.items.pop()
        print(f"Popped {popped_item} from the stack.")
        return popped_item

    def display(self):
        """Display all items in the stack."""
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack elements (top → bottom):")
            for item in reversed(self.items):
                print(item)


if __name__ == "__main__":
    stack = Stack()

    while True:
        print("\n--- Stack Menu ---")
        print("1. Push element")
        print("2. Pop element")
        print("3. Display stack")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            element = input("Enter element to push: ")
            stack.push(element)

        elif choice == "2":
            stack.pop()

        elif choice == "3":
            stack.display()

        elif choice == "4":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")




class Queue:
    def __init__(self):
        """Initialize an empty queue."""
        self.items = []

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self.items) == 0

    def enqueue(self, item):
        """Add an item to the end of the queue."""
        self.items.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        """Remove and return the item from the front of the queue."""
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        dequeued_item = self.items.pop(0)
        print(f"Dequeued: {dequeued_item}")
        return dequeued_item

    def display(self):
        """Display all elements in the queue."""
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue elements (front → rear):", self.items)


# Example usage
if __name__ == "__main__":
    queue = Queue()

    while True:
        print("\n--- Queue Menu ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Display queue")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            element = input("Enter element to enqueue: ")
            queue.enqueue(element)

        elif choice == "2":
            queue.dequeue()

        elif choice == "3":
            queue.display()

        elif choice == "4":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")




class BankAccount:
    def __init__(self, account_number, name, balance=0):
        """Initialize a bank account with account number, customer name, and balance."""
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"${amount:.2f} deposited. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        print(f"${amount:.2f} withdrawn. New balance: ${self.balance:.2f}")

    def display_account(self):
        """Display account details."""
        print(f"Account Number: {self.account_number}")
        print(f"Customer Name: {self.name}")
        print(f"Balance: ${self.balance:.2f}")


class Bank:
    def __init__(self, name):
        """Initialize a bank with a name and an empty dictionary of accounts."""
        self.name = name
        self.accounts = {}  # key: account_number, value: BankAccount object

    def create_account(self, account_number, customer_name, initial_deposit=0):
        """Create a new customer account."""
        if account_number in self.accounts:
            print("Account number already exists.")
            return
        account = BankAccount(account_number, customer_name, initial_deposit)
        self.accounts[account_number] = account
        print(f"Account created for {customer_name} with account number {account_number}.")

    def deposit(self, account_number, amount):
        """Deposit money into a customer's account."""
        account = self.accounts.get(account_number)
        if account:
            account.deposit(amount)
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        """Withdraw money from a customer's account."""
        account = self.accounts.get(account_number)
        if account:
            account.withdraw(amount)
        else:
            print("Account not found.")

    def display_account(self, account_number):
        """Display details of a customer's account."""
        account = self.accounts.get(account_number)
        if account:
            account.display_account()
        else:
            print("Account not found.")

    def display_all_accounts(self):
        """Display all customer accounts in the bank."""
        if not self.accounts:
            print("No accounts in the bank.")
            return
        print(f"\n--- Accounts in {self.name} ---")
        for account in self.accounts.values():
            account.display_account()
            print("-----------------------------")


# Example usage
if __name__ == "__main__":
    bank = Bank("OpenAI Bank")

    while True:
        print("\n--- Bank Menu ---")
        print("1. Create account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Display account")
        print("5. Display all accounts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            acc_num = input("Enter account number: ")
            name = input("Enter customer name: ")
            initial = float(input("Enter initial deposit: "))
            bank.create_account(acc_num, name, initial)

        elif choice == "2":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            bank.deposit(acc_num, amount)

        elif choice == "3":
            acc_num = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw(acc_num, amount)

        elif choice == "4":
            acc_num = input("Enter account number: ")
            bank.display_account(acc_num)

        elif choice == "5":
            bank.display_all_accounts()

        elif choice == "6":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
