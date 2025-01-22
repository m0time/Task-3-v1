import pytest 

from palindrome import is_palindrome

def test_palindrome_standard():
    assert is_palindrome("racecar") == True

def test_palindrome_caps():
    assert is_palindrome("Racecar") == True

def test_palindrome_false():
    assert is_palindrome("hello") == False

def test_palindrome_specialcharacters():
    assert is_palindrome("No 'x' in Nixon") == True

def test_palindrome_nothing():
    assert is_palindrome("") == True


if __name__ == "__main__":
    pytest.main()
