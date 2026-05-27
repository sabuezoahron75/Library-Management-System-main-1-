"""Main entry point for the Library Management System."""

from services import LibraryService
from exceptions import (
    BookNotFoundError,
    MemberNotFoundError,
    BookUnavailableError,
    BookAlreadyAvailableError,
    LoanNotFoundError
)

def display_menu():
    """Display the main menu to the user."""
    print("\n" + "="*50)
    print("     LIBRARY MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add Book")
    print("2. Register Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. View Books")
    print("6. View Members")
    print("7. View Loans")
    print("8. Exit")
    print("="*50)
    return input("Enter your choice (1-8): ")

def add_book_flow(service):
    """Flowchart: _01_add_book.svg"""
    print("\n--- Add Book ---")
    try:
        book_id = input("Enter Book ID: ").strip()
        title = input("Enter Book Title: ").strip()
        author = input("Enter Book Author: ").strip()
        
        if not all([book_id, title, author]):
            print("Error: All fields are required.")
            return
        
        book = service.add_book(book_id, title, author)
        print(f"✓ Book added: {title}")
    except Exception as e:
        print(f"Error: {e}")

def register_member_flow(service):
    """Flowchart: _02_register_member.svg"""
    print("\n--- Register Member ---")
    try:
        member_id = input("Enter Member ID: ").strip()
        name = input("Enter Member Name: ").strip()
        email = input("Enter Member Email: ").strip()
        
        if not all([member_id, name, email]):
            print("Error: All fields are required.")
            return
        
        member = service.register_member(member_id, name, email)
        print(f"✓ Member registered: {name}")
    except Exception as e:
        print(f"Error: {e}")

def borrow_book_flow(service):
    """Flowchart: _03_borrow_book.svg"""
    print("\n--- Borrow Book ---")
    try:
        book_id = input("Enter Book ID: ").strip()
        member_id = input("Enter Member ID: ").strip()
        
        if not all([book_id, member_id]):
            print("Error: Book ID and Member ID are required.")
            return
        
        loan = service.borrow_book(book_id, member_id)
        print(f"✓ {loan.member.name} borrowed {loan.book.title}")
        print(f"  Loan ID: {loan.loan_id}")
    except BookNotFoundError:
        print("Error: Book not found.")
    except MemberNotFoundError:
        print("Error: Member not found.")
    except BookUnavailableError:
        print("Error: Book is already borrowed.")
    except Exception as e:
        print(f"Error: {e}")

def return_book_flow(service):
    """Flowchart: _04_return_book.svg"""
    print("\n--- Return Book ---")
    try:
        book_id = input("Enter Book ID: ").strip()
        member_id = input("Enter Member ID: ").strip()
        
        if not all([book_id, member_id]):
            print("Error: Book ID and Member ID are required.")
            return
        
        loan = service.return_book(book_id, member_id)
        print(f"✓ {loan.member.name} returned {loan.book.title}")
        print(f"  Loan ID: {loan.loan_id}")
    except BookNotFoundError:
        print("Error: Book not found.")
    except MemberNotFoundError:
        print("Error: Member not found.")
    except BookAlreadyAvailableError:
        print("Error: Book is already available.")
    except LoanNotFoundError:
        print("Error: No active loan found for this book and member.")
    except Exception as e:
        print(f"Error: {e}")

def view_books_flow(service):
    """Flowchart: _05_view_book.svg"""
    print("\n--- View Books ---")
    books = service.view_books()
    
    if not books:
        print("No books found.")
        return
    
    print("Books:")
    for book in books:
        print(f"  {book}")

def view_members_flow(service):
    """Flowchart: _06_view_member.svg"""
    print("\n--- View Members ---")
    members = service.view_members()
    
    if not members:
        print("No members found.")
        return
    
    print("Members:")
    for member in members:
        print(f"  {member}")

def view_loans_flow(service):
    """Flowchart: _07_view_loan.svg"""
    print("\n--- View Loans ---")
    loans = service.view_loans()
    
    if not loans:
        print("No loans found.")
        return
    
    print("Loans:")
    for loan in loans:
        print(f"  {loan}")

def exit_flow():
    """Flowchart: _08_exit.svg"""
    print("\nProgram closed.")

def main():
    """Main application loop."""
    service = LibraryService()
    
    while True:
        choice = display_menu()
        
        if choice == "1":
            add_book_flow(service)
        elif choice == "2":
            register_member_flow(service)
        elif choice == "3":
            borrow_book_flow(service)
        elif choice == "4":
            return_book_flow(service)
        elif choice == "5":
            view_books_flow(service)
        elif choice == "6":
            view_members_flow(service)
        elif choice == "7":
            view_loans_flow(service)
        elif choice == "8":
            exit_flow()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()
