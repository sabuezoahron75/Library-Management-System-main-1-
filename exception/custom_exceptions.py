"""Custom exceptions for the Library Management System."""

class LibraryException(Exception):
    """Base exception for all library-related errors."""
    pass


class BookNotFoundError(LibraryException):
    """Raised when a book is not found in the library."""
    def __init__(self, book_id):
        self.book_id = book_id
        super().__init__(f"Book not found: {book_id}")


class MemberNotFoundError(LibraryException):
    """Raised when a member is not found in the library."""
    def __init__(self, member_id):
        self.member_id = member_id
        super().__init__(f"Member not found: {member_id}")


class BookUnavailableError(LibraryException):
    """Raised when a book is not available for borrowing."""
    def __init__(self, book_id):
        self.book_id = book_id
        super().__init__(f"Book is already borrowed: {book_id}")


class BookAlreadyAvailableError(LibraryException):
    """Raised when attempting to return a book that is already available."""
    def __init__(self, book_id):
        self.book_id = book_id
        super().__init__(f"Book is already available: {book_id}")


class LoanNotFoundError(LibraryException):
    """Raised when a loan is not found."""
    def __init__(self, loan_id):
        self.loan_id = loan_id
        super().__init__(f"Loan not found: {loan_id}")
