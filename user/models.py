import uuid
from passlib.hash import pbkdf2_sha256

class User:
    def __init__(self, id=None, name=None, email=None, password=None):
        self.id = id or uuid.uuid4().hex  # Generate UUID if not provided
        self.name = name
        self.email = email
        self.password = self.encrypt_password(password) if password else None

    @staticmethod
    def encrypt_password(password):
        """Encrypts the password using pbkdf2_sha256."""
        return pbkdf2_sha256.hash(password)

    @staticmethod
    def verify_password(hashed_password, password):
        """Verifies the password."""
        return pbkdf2_sha256.verify(password, hashed_password)

    def to_dict(self):
        """Convert the User object to a dictionary."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password
        }
