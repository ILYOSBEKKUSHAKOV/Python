
class Task:
    def __init__(self, title, description, due_date):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.completed = False

    def mark_complete(self):
        self.completed = True

    def __str__(self):
        status = "✓ Completed" if self.completed else "✗ Incomplete"
        return f"Title: {self.title}\nDescription: {self.description}\nDue Date: {self.due_date}\nStatus: {status}\n"


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task.title}' added.")

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                print(f"Task '{title}' marked as complete.")
                return
        print(f"Task '{title}' not found.")

    def list_all_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task)

    def list_incomplete_tasks(self):
        incomplete = [task for task in self.tasks if not task.completed]
        if not incomplete:
            print("No incomplete tasks.")
        else:
            for task in incomplete:
                print(task)


def main():
    todo = ToDoList()

    while True:
        print("\n--- ToDo List Menu ---")
        print("1. Add Task")
        print("2. Mark Task Complete")
        print("3. List All Tasks")
        print("4. List Incomplete Tasks")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            title = input("Task title: ")
            desc = input("Task description: ")
            due = input("Due date: ")
            todo.add_task(Task(title, desc, due))

        elif choice == '2':
            title = input("Enter task title to mark complete: ")
            todo.mark_task_complete(title)

        elif choice == '3':
            print("\n--- All Tasks ---")
            todo.list_all_tasks()

        elif choice == '4':
            print("\n--- Incomplete Tasks ---")
            todo.list_incomplete_tasks()

        elif choice == '5':
            print("Exiting program...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()



class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def edit(self, new_title, new_content):
        self.title = new_title
        self.content = new_content

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nContent: {self.content}\n"


class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)
        print(f"Post '{post.title}' added successfully.")

    def list_all_posts(self):
        if not self.posts:
            print("No posts available.")
        else:
            for i, post in enumerate(self.posts, start=1):
                print(f"Post #{i}\n{post}")

    def list_posts_by_author(self, author):
        filtered_posts = [post for post in self.posts if post.author.lower() == author.lower()]
        if not filtered_posts:
            print(f"No posts found by author: {author}")
        else:
            for post in filtered_posts:
                print(post)

    def delete_post(self, title):
        for post in self.posts:
            if post.title.lower() == title.lower():
                self.posts.remove(post)
                print(f"Post '{title}' deleted.")
                return
        print(f"Post '{title}' not found.")

    def edit_post(self, title):
        for post in self.posts:
            if post.title.lower() == title.lower():
                new_title = input("Enter new title: ")
                new_content = input("Enter new content: ")
                post.edit(new_title, new_content)
                print("Post updated successfully.")
                return
        print(f"Post '{title}' not found.")

    def display_latest_posts(self, count=3):
        if not self.posts:
            print("No posts available.")
            return

        latest = self.posts[-count:] 
        print(f"--- Latest {len(latest)} Posts ---")
        for post in reversed(latest):
            print(post)


def main():
    blog = Blog()

    while True:
        print("\n--- Blog Menu ---")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. List Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. Display Latest Posts")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == '1':
            title = input("Post title: ")
            content = input("Post content: ")
            author = input("Author name: ")
            blog.add_post(Post(title, content, author))

        elif choice == '2':
            print("\n--- All Posts ---")
            blog.list_all_posts()

        elif choice == '3':
            author = input("Enter author name: ")
            print(f"\n--- Posts by {author} ---")
            blog.list_posts_by_author(author)

        elif choice == '4':
            title = input("Enter title of post to delete: ")
            blog.delete_post(title)

        elif choice == '5':
            title = input("Enter title of post to edit: ")
            blog.edit_post(title)

        elif choice == '6':
            count = input("How many latest posts do you want to display? (default=3): ")
            count = int(count) if count.strip().isdigit() else 3
            blog.display_latest_posts(count)

        elif choice == '7':
            print("Exiting Blog System...")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()


class Account:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return

        if amount > self.balance:
            print("Insufficient balance! Overdraft not allowed.")
            return

        self.balance -= amount
        print(f"Withdrawn {amount}. New balance: {self.balance}")

    def __str__(self):
        return f"Account Number: {self.account_number}\nHolder: {self.holder_name}\nBalance: {self.balance}\n"


class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)
        print(f"Account {account.account_number} created successfully.")

    def find_account(self, acc_number):
        for acc in self.accounts:
            if acc.account_number == acc_number:
                return acc
        return None

    def check_balance(self, acc_number):
        acc = self.find_account(acc_number)
        if acc:
            print(f"Balance for account {acc_number}: {acc.balance}")
        else:
            print("Account not found.")

    def deposit(self, acc_number, amount):
        acc = self.find_account(acc_number)
        if acc:
            acc.deposit(amount)
        else:
            print("Account not found.")

    def withdraw(self, acc_number, amount):
        acc = self.find_account(acc_number)
        if acc:
            acc.withdraw(amount)
        else:
            print("Account not found.")

    def transfer(self, from_acc_num, to_acc_num, amount):
        from_acc = self.find_account(from_acc_num)
        to_acc = self.find_account(to_acc_num)

        if not from_acc or not to_acc:
            print("One or both accounts not found.")
            return

        if amount <= 0:
            print("Transfer amount must be positive.")
            return

        if from_acc.balance < amount:
            print("Insufficient balance for transfer.")
            return

        from_acc.balance -= amount
        to_acc.balance += amount
        print(f"Transferred {amount} from {from_acc_num} to {to_acc_num}.")

    def display_account(self, acc_number):
        acc = self.find_account(acc_number)
        if acc:
            print(acc)
        else:
            print("Account not found.")


def main():
    bank = Bank()

    while True:
        print("\n--- Banking System Menu ---")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Display Account Details")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == '1':
            acc_number = input("Enter account number: ")
            holder = input("Enter account holder name: ")
            balance = float(input("Initial balance: "))
            bank.add_account(Account(acc_number, holder, balance))

        elif choice == '2':
            acc = input("Enter account number: ")
            bank.check_balance(acc)

        elif choice == '3':
            acc = input("Enter account number: ")
            amount = float(input("Amount to deposit: "))
            bank.deposit(acc, amount)

        elif choice == '4':
            acc = input("Enter account number: ")
            amount = float(input("Amount to withdraw: "))
            bank.withdraw(acc, amount)

        elif choice == '5':
            from_acc = input("Enter source account number: ")
            to_acc = input("Enter destination account number: ")
            amount = float(input("Amount to transfer: "))
            bank.transfer(from_acc, to_acc, amount)

        elif choice == '6':
            acc = input("Enter account number: ")
            bank.display_account(acc)

        elif choice == '7':
            print("Exiting Banking System...")
            break

        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()
