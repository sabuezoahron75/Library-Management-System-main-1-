# Library Management System

A comprehensive Python-based Library Management System that implements core library operations including book management, member registration, and loan tracking.

## Project Structure

```
Library-Management-System-main/
├── models/
│   ├── __init__.py
│   ├── book.py           # Book model
│   ├── member.py         # Member model
│   └── loan.py           # Loan model
├── services/
│   ├── __init__.py
│   └── library_service.py  # Core business logic
├── exceptions/
│   ├── __init__.py
│   └── custom_exceptions.py  # Custom exception classes
├── main.py               # Main application entry point
└── README.md
```

## Features

### 1. Add Book (Flowchart: _01_add_book.svg)
Adds a new book to the library system with:
- Book ID
- Title
- Author
- Initial availability status (available = True)

### 2. Register Member (Flowchart: _02_register_member.svg)
Registers a new member to the library with:
- Member ID
- Full Name
- Email Address

### 3. Borrow Book (Flowchart: _03_borrow_book.svg)
Processes book borrowing with validation:
- Checks if book exists
- Checks if member exists
- Validates book availability
- Creates a loan record
- Generates unique Loan ID (L001, L002, ...)

**Error Handling:**
- `BookNotFoundError`: Book doesn't exist
- `MemberNotFoundError`: Member doesn't exist
- `BookUnavailableError`: Book is already borrowed

### 4. Return Book (Flowchart: _04_return_book.svg)
Processes book returns with validation:
- Verifies book and member existence
- Confirms book is borrowed
- Updates book availability
- Closes the loan record

### 5. View Books (Flowchart: _05_view_book.svg)
Displays all books with their status:
- Shows book ID, title, author
- Displays availability status (Available/Borrowed)

### 6. View Members (Flowchart: _06_view_member.svg)
Lists all registered members with:
- Member ID
- Name
- Email

### 7. View Loans (Flowchart: _07_view_loan.svg)
Displays all loan transactions:
- Loan ID
- Member name
- Book title
- Loan status (Active/Closed)

### 8. Exit (Flowchart: _08_exit.svg)
Gracefully terminates the application

## Data Models

### Book
```python
Class: Book
Attributes:
  - book_id: str (unique identifier)
  - title: str
  - author: str
  - available: bool (default: True)
Methods:
  - borrow(): marks book as unavailable
  - return_book(): marks book as available
```

### Member
```python
Class: Member
Attributes:
  - member_id: str (unique identifier)
  - name: str
  - email: str
```

### Loan
```python
Class: Loan
Attributes:
  - loan_id: str (auto-generated L001, L002, ...)
  - book: Book object
  - member: Member object
  - borrow_date: datetime
  - return_date: datetime (None if active)
  - is_active: bool (True for active loans)
Methods:
  - close_loan(): closes the loan transaction
```

## Exception Handling

The system includes custom exceptions:
- `LibraryException`: Base exception
- `BookNotFoundError`: Book ID not found
- `MemberNotFoundError`: Member ID not found
- `BookUnavailableError`: Book already borrowed
- `BookAlreadyAvailableError`: Book not borrowed
- `LoanNotFoundError`: Loan transaction not found

## Usage

### Running the Application

```bash
python main.py
```

### Menu Navigation

```
==================================================
     LIBRARY MANAGEMENT SYSTEM
==================================================
1. Add Book
2. Register Member
3. Borrow Book
4. Return Book
5. View Books
6. View Members
7. View Loans
8. Exit
==================================================
```

### Example Workflow

1. **Add Books**
   - Input: ID: B001, Title: Python Programming, Author: Guido van Rossum
   - Output: ✓ Book added: Python Programming

2. **Register Members**
   - Input: ID: M001, Name: John Doe, Email: john@example.com
   - Output: ✓ Member registered: John Doe

3. **Borrow Books**
   - Input: Book ID: B001, Member ID: M001
   - Output: ✓ John Doe borrowed Python Programming
   - Generated Loan ID: L001

4. **View Books**
   - Shows: B001 - Python Programming by Guido van Rossum [Borrowed]

5. **View Loans**
   - Shows: L001 - John Doe borrowed Python Programming [Active]

6. **Return Book**
   - Input: Book ID: B001, Member ID: M001
   - Output: ✓ John Doe returned Python Programming

## Design Pattern

The system uses:
- **Service Layer Pattern**: `LibraryService` encapsulates business logic
- **Model Pattern**: Separate classes for Book, Member, and Loan
- **Exception Pattern**: Custom exceptions for error handling
- **Dictionary/List Storage**: In-memory data structures

## Flowchart Mappings

Each function in the codebase maps directly to its corresponding flowchart:

| Function | Flowchart | Location |
|----------|-----------|----------|
| add_book() | _01_add_book.svg | services/library_service.py |
| register_member() | _02_register_member.svg | services/library_service.py |
| borrow_book() | _03_borrow_book.svg | services/library_service.py |
| return_book() | _04_return_book.svg | services/library_service.py |
| view_books() | _05_view_book.svg | services/library_service.py |
| view_members() | _06_view_member.svg | services/library_service.py |
| view_loans() | _07_view_loan.svg | services/library_service.py |
| main() | _08_exit.svg | main.py |

## Future Enhancements

- Database integration (SQLite, PostgreSQL)
- Due date tracking and late fees
- Book search and filtering
- Member borrowing history
- Reservation system
- Email notifications
- Web interface (Flask/Django)
- API endpoints (REST)

## Notes

- All data is stored in-memory and will be lost when the program exits
- For production use, integrate with a persistent database
- Consider adding authentication and authorization
- Implement logging for audit trails
