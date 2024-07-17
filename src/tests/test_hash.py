"""
This file contains the tests for hashing the passwords
"""
from src.helpers.hash import hash_password, verify_password

def test_hash_password():
    """
    This function tests the hash_password (bcrypt hashed passwords start with $2b$)
    """
    password = "test123"
    hashed_password = hash_password(password)

    assert hashed_password != password
    assert hashed_password.startswith("$2b$")

def test_hash_password_inputs():
    """
    This function tests different password inputs for the hash_password function
    """
    password = ""
    hashed_password = hash_password(password)

    password2 = None
    hashed_password2 = hash_password(password2)

    password3 = True
    hashed_password3 = hash_password(password3)

    password4 = 10
    hashed_password4 = hash_password(password4)

    password5 = {"test":"value"}
    hashed_password5 = hash_password(password5)

    password6 = "test123"
    hashed_password6 = hash_password(password6)

    assert hashed_password is None
    assert hashed_password2 is None
    assert hashed_password3 is None
    assert hashed_password4 is None
    assert hashed_password5 is None
    assert hashed_password6 is not None

def test_verify_password():
    """
    This function tests the validity of the verify_password function
    """
    password = "test123"
    hashed_password = hash_password(password)

    assert verify_password(password, hashed_password) is True
    assert verify_password("wrong_password", hashed_password) is False

def test_hash_consistency():
    """
    This function tests the consistency of the hashing and verification functions
    """
    password = "test123"
    hashed_password1 = hash_password(password)
    hashed_password2 = hash_password(password)

    # Even though the password is the same, the hash should be different due to salting
    assert hashed_password1 != hashed_password2
    assert verify_password(password, hashed_password1) is True
    assert verify_password(password, hashed_password2) is True

def test_verify_with_different_passwords():
    """
    This function tests different password scenarios
    """
    password1 = "password1"
    password2 = "password2"

    hashed_password1 = hash_password(password1)
    hashed_password2 = hash_password(password2)

    assert verify_password(password1, hashed_password1) is True
    assert verify_password(password2, hashed_password2) is True
    assert verify_password(password1, hashed_password2) is False
    assert verify_password(password2, hashed_password1) is False
