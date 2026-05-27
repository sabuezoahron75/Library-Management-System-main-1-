"""Member model for the Library Management System."""

class Member:
    """Represents a member in the library."""
    
    def __init__(self, member_id, name, email):
        """Initialize a Member object.
        
        Args:
            member_id (str): Unique identifier for the member
            name (str): Full name of the member
            email (str): Email address of the member
        """
        self.member_id = member_id
        self.name = name
        self.email = email
    
    def __str__(self):
        """Return string representation of the member."""
        return f"{self.member_id} - {self.name} ({self.email})"
    
    def __repr__(self):
        """Return detailed representation of the member."""
        return f"Member(id={self.member_id}, name={self.name}, email={self.email})"
