"""Library Service containing core business logic."""

from models import Book, Member, Loan
from exceptions import (
    BookNotFoundError,
    MemberNotFoundError,
    BookUnavailableError,
    BookAlreadyAvailableError,
    LoanNotFoundError
)

class LibraryService:
    """Service class for managing library operations."""
    
    def __init__(self):
        """Initialize the LibraryService with empty collections."""
        self._books = {}          # Dictionary: book_id -> Book
        self._members = {}        # Dictionary: member_id -> Member
        self._loans = []          # List of Loan objects
        self._loan_counter = 0    # Counter for generating loan IDs
    
    # ==================== ADD BOOK ====================
    def add_book(self, book_id, title, author):
        """Add a new book to the library.
        
        Flowchart: _01_add_book.svg
        
        Args:
            book_id (str): Unique identifier for the book
            title (str): Title of the book
            author (str): Author of the book
        
        Returns:
            Book: The created Book object
        """
        # Create Book object with available = True
        book = Book(book_id, title, author)
        
        # Store book in _books dictionary with key = book.book_id
        self._books[book.book_id] = book
        
        return book
    
    # ==================== REGISTER MEMBER ====================
    def register_member(self, member_id, name, email):
        """Register a new member to the library.
        
        Flowchart: _02_register_member.svg
        
        Args:
            member_id (str): Unique identifier for the member
            name (str): Full name of the member
            email (str): Email address of the member
        
        Returns:
            Member: The created Member object
        """
        # Create Member object
        member = Member(member_id, name, email)
        
        # Store member in _members dictionary with key = member.member_id
        self._members[member.member_id] = member
        
        return member
    
    # ==================== BORROW BOOK ====================
    def borrow_book(self, book_id, member_id):
        """Process a book borrow transaction.
        
        Flowchart: _03_borrow_book.svg
        
        Args:
            book_id (str): ID of the book to borrow
            member_id (str): ID of the member borrowing
        
        Returns:
            Loan: The created Loan object
        
        Raises:
            BookNotFoundError: If book doesn't exist
            MemberNotFoundError: If member doesn't exist
            BookUnavailableError: If book is already borrowed
        """
        # Lookup book
        book = self._books.get(book_id)
        # Decision 1: book is None?
        if book is None:
            raise BookNotFoundError(book_id)
        
        # Lookup member
        member = self._members.get(member_id)
        # Decision 2: member is None?
        if member is None:
            raise MemberNotFoundError(member_id)
        
        # Decision 3: not book.available?
        if not book.available:
            raise BookUnavailableError(book_id)
        
        # book.borrow() → sets available = False
        book.borrow()
        
        # Generate loan_id "L{n:03}"
        self._loan_counter += 1
        loan_id = f"L{self._loan_counter:03d}"
        
        # Create Loan and append to _loans list
        loan = Loan(loan_id, book, member)
        self._loans.append(loan)
        
        return loan
    
    # ==================== RETURN BOOK ====================
    def return_book(self, book_id, member_id):
        """Process a book return transaction.
        
        Flowchart: _04_return_book.svg (implementation mirrors borrow with return logic)
        
        Args:
            book_id (str): ID of the book to return
            member_id (str): ID of the member returning
        
        Returns:
            Loan: The closed Loan object
        
        Raises:
            BookNotFoundError: If book doesn't exist
            MemberNotFoundError: If member doesn't exist
            BookAlreadyAvailableError: If book is already available
            LoanNotFoundError: If active loan not found
        """
        # Lookup book
        book = self._books.get(book_id)
        if book is None:
            raise BookNotFoundError(book_id)
        
        # Lookup member
        member = self._members.get(member_id)
        if member is None:
            raise MemberNotFoundError(member_id)
        
        # Check if book is available
        if book.available:
            raise BookAlreadyAvailableError(book_id)
        
        # Find active loan for this book and member
        active_loan = None
        for loan in self._loans:
            if (loan.is_active and 
                loan.book.book_id == book_id and 
                loan.member.member_id == member_id):
                active_loan = loan
                break
        
        if active_loan is None:
            raise LoanNotFoundError(f"{book_id}-{member_id}")
        
        # Return the book → sets available = True
        book.return_book()
        
        # Close the loan
        active_loan.close_loan()
        
        return active_loan
    
    # ==================== VIEW BOOKS ====================
    def view_books(self):
        """Get list of all books in the library.
        
        Flowchart: _05_view_book.svg
        
        Returns:
            list: List of Book objects
        """
        # Return list(_books.values())
        return list(self._books.values())
    
    # ==================== VIEW MEMBERS ====================
    def view_members(self):
        """Get list of all members in the library.
        
        Flowchart: _06_view_member.svg
        
        Returns:
            list: List of Member objects
        """
        # Return list(_members.values())
        return list(self._members.values())
    
    # ==================== VIEW LOANS ====================
    def view_loans(self):
        """Get list of all loans in the library.
        
        Flowchart: _07_view_loan.svg
        
        Returns:
            list: List of Loan objects
        """
        # Return list(_loans)
        return list(self._loans)
    
    # ==================== UTILITY METHODS ====================
    def get_book(self, book_id):
        """Get a specific book by ID.
        
        Args:
            book_id (str): ID of the book
        
        Returns:
            Book: The Book object or None
        """
        return self._books.get(book_id)
    
    def get_member(self, member_id):
        """Get a specific member by ID.
        
        Args:
            member_id (str): ID of the member
        
        Returns:
            Member: The Member object or None
        """
        return self._members.get(member_id)
    
    def get_active_loans_for_member(self, member_id):
        """Get all active loans for a specific member.
        
        Args:
            member_id (str): ID of the member
        
        Returns:
            list: List of active Loan objects for the member
        """
        return [loan for loan in self._loans 
                if loan.member.member_id == member_id and loan.is_active]
