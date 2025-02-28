import pickle    # The pickle module is used for saving and loading data to and from files .
import os       #  the os module handles file existence checks and modifications .

# Define Book and Student classes
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.issued_to = None  # Stores student ID if issued

    def __str__(self):
        return f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Issued to: {self.issued_to or 'None'}"


class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.issued_books = []  # Stores book IDs

    def __str__(self):
        return f"Student ID: {self.student_id}, Name: {self.name}, Issued Books: {self.issued_books}"


# File operations
def save_data(filename, data):
    with open(filename, 'wb') as file:
        pickle.dump(data, file)


def load_data(filename):
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)
    return {}


# Functions for the LMS

# To issue a book
def issue_book():
    student_id = input("Enter student ID: ")
    book_id = input("Enter book ID to issue: ")

    students = load_data('student.dat')
    books = load_data('book.dat')

    if student_id in students and book_id in books:
        student = students[student_id]
        book = books[book_id]
        
        if book.issued_to is None:
            book.issued_to = student_id
            student.issued_books.append(book_id)
            print("Book issued successfully.")
        else:
            print("Book is already issued to another student.")
    else:
        print("Invalid student ID or book ID.")
    
    save_data('student.dat', students)
    save_data('book.dat', books)


# To return the book
def deposit_book():
    student_id = input("Enter student ID: ")
    book_id = input("Enter book ID to deposit: ")

    students = load_data('student.dat')
    books = load_data('book.dat')

    if student_id in students and book_id in books:
        student = students[student_id]
        book = books[book_id]
        
        if book.issued_to == student_id:
            book.issued_to = None
            student.issued_books.remove(book_id)
            print("Book deposited successfully.")
        else:
            print("This book was not issued to the student.")
    else:
        print("Invalid student ID or book ID.")
    
    save_data('student.dat', students)
    save_data('book.dat', books)


# To create a new Student details
def create_student():
    student_id = input("Enter new student ID: ")
    name = input("Enter student name: ")

    students = load_data('student.dat')
    if student_id not in students:
        students[student_id] = Student(student_id, name)
        save_data('student.dat', students)
        print("Student record created successfully.")
    else:
        print("Student with this ID already exists.")


# To display all students
def display_all_students():
    students = load_data('student.dat')
    if students:
        for student in students.values():
            print(student)
    else:
        print("No students found.")


# To display a specific Student
def display_student():
    student_id = input("Enter student ID: ")
    students = load_data('student.dat')
    
    if student_id in students:
        print(students[student_id])
    else:
        print("Student record not found.")

# To modify a specific student
def modify_student():
    student_id = input("Enter student ID to modify: ")
    students = load_data('student.dat')
    
    if student_id in students:
        name = input("Enter new name: ")
        students[student_id].name = name
        save_data('student.dat', students)
        print("Student record modified.")
    else:
        print("Student record not found.")

# To delete a Specific Student
def delete_student():
    student_id = input("Enter student ID to delete: ")
    students = load_data('student.dat')
    
    if student_id in students:
        del students[student_id]
        save_data('student.dat', students)
        print("Student record deleted.")
    else:
        print("Student record not found.")

# To create a new book record
def create_book():
    book_id = input("Enter new book ID: ")
    title = input("Enter book title: ")
    author = input("Enter book author: ")

    books = load_data('book.dat')
    if book_id not in books:
        books[book_id] = Book(book_id, title, author)
        save_data('book.dat', books)
        print("Book record created successfully.")
    else:
        print("Book with this ID already exists.")

# To display all the  created books
def display_all_books():
    books = load_data('book.dat')
    if books:
        for book in books.values():
            print(book)
    else:
        print("No books found.")

# To display a Specific Book
def display_book():
    book_id = input("Enter book ID: ")
    books = load_data('book.dat')
    
    if book_id in books:
        print(books[book_id])
    else:
        print("Book record not found.")

# To modify a specific book
def modify_book():
    book_id = input("Enter book ID to modify: ")
    books = load_data('book.dat')
    
    if book_id in books:
        title = input("Enter new title: ")
        author = input("Enter new author: ")
        books[book_id].title = title
        books[book_id].author = author
        save_data('book.dat', books)
        print("Book record modified.")
    else:
        print("Book record not found.")

# To delete a specific Book
def delete_book():
    book_id = input("Enter book ID to delete: ")
    books = load_data('book.dat')
    
    if book_id in books:
        del books[book_id]
        save_data('book.dat', books)
        print("Book record deleted.")
    else:
        print("Book record not found.")


# Main menu will display first Automatically
def main_menu():
    while True:
        print("\nLibrary Management System")
        print("1. Book Issue")
        print("2. Book Deposit")
        print("3. Administration Menu")
        print("4. Exit")
        print("-----------------------------------------------------")
        choice = input("Enter your choice: ")

        if choice == '1':
            issue_book()
        elif choice == '2':
            deposit_book()
        elif choice == '3':
            admin_menu()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Administration Menu
def admin_menu():
    while True:
        print("\nAdministration Menu")
        print("1. Create Student Record")
        print("2. Display All Students Record")
        print("3. Display Specific Student Record")
        print("4. Modify Student Record")
        print("5. Delete Student Record")
        print("6. Create Book")
        print("7. Display All Books")
        print("8. Display Specific Book")
        print("9. Modify Book")
        print("10. Delete Book Record")
        print("11. Back to Main Menu")
        print("-----------------------------------------------------------")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_student()
        elif choice == '2':
            display_all_students()
        elif choice == '3':
            display_student()
        elif choice == '4':
            modify_student()
        elif choice == '5':
            delete_student()
        elif choice == '6':
            create_book()
        elif choice == '7':
            display_all_books()
        elif choice == '8':
            display_book()
        elif choice == '9':
            modify_book()
        elif choice == '10':
            delete_book()
        elif choice == '11':
            break
        else:
            print("Invalid choice. Please try again.")


# Run the main menu
if __name__ == "__main__":
    main_menu()
