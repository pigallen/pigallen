import random
import string
import json

# Helper functions
def generate_isbn():
    return ''.join(random.choices(string.digits, k=13))

def generate_title():
    words = ['The', 'A', 'An', 'Mystery', 'Adventure', 'Journey', 'Legend', 'Quest', 'Saga', 'Chronicle']
    return ' '.join(random.choices(words, k=4))

def generate_author():
    first_names = ['John', 'Jane', 'Alex', 'Alice', 'Michael', 'Michelle', 'Chris', 'Christina']
    last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis']
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_price():
    return round(random.uniform(5, 100), 2)

def generate_stock():
    return random.randint(0, 50)

# Book class
class Book:
    def __init__(self, isbn, title, author, price, stock):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock

    def to_dict(self):
        return {
            'isbn': self.isbn,
            'title': self.title,
            'author': self.author,
            'price': self.price,
            'stock': self.stock
        }

    def __str__(self):
        return f"{self.title} by {self.author} - ${self.price} [{self.stock} in stock]"

# Inventory class
class Inventory:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def list_books(self):
        for book in self.books:
            print(book)

    def to_dict(self):
        return [book.to_dict() for book in self.books]

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.to_dict(), file, indent=4)

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            books = json.load(file)
            self.books = [Book(**book) for book in books]

# Customer class
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cart = []

    def add_to_cart(self, book):
        self.cart.append(book)

    def remove_from_cart(self, isbn):
        self.cart = [book for book in self.cart if book.isbn != isbn]

    def view_cart(self):
        for book in self.cart:
            print(book)

    def checkout(self):
        total = sum(book.price for book in self.cart)
        self.cart.clear()
        print(f"Total: ${total:.2f}. Thank you for your purchase!")

# Bookstore class
class Bookstore:
    def __init__(self, name):
        self.name = name
        self.inventory = Inventory()
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def find_customer(self, email):
        for customer in self.customers:
            if customer.email == email:
                return customer
        return None

    def simulate(self):
        # Generate random books
        for _ in range(50):
            book = Book(generate_isbn(), generate_title(), generate_author(), generate_price(), generate_stock())
            self.inventory.add_book(book)

        # Generate random customers
        customer_names = ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Brown']
        customer_emails = ['john@example.com', 'jane@example.com', 'alice@example.com', 'bob@example.com']
        for name, email in zip(customer_names, customer_emails):
            self.add_customer(Customer(name, email))

        # Display inventory
        print("Inventory:")
        self.inventory.list_books()

        # Simulate customer actions
        customer = self.find_customer('john@example.com')
        if customer:
            book = self.inventory.find_book(self.inventory.books[0].isbn)
            if book:
                customer.add_to_cart(book)
                print("\nCustomer's cart after adding a book:")
                customer.view_cart()
                customer.checkout()

        # Save and load inventory to/from file
        self.inventory.save_to_file('inventory.json')
        self.inventory.load_from_file('inventory.json')
        print("\nInventory after loading from file:")
        self.inventory.list_books()

# Main function
def main():
    bookstore = Bookstore("Fantasy Books")
    bookstore.simulate()

if __name__ == "__main__":
    main()
