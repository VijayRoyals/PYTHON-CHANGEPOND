import string

def has_special_character(string):
    special_chars = set(string.punctuation)
    for char in string:
        if char in special_chars:
            return True
    return False


test_string = "Hello, world!"
print(f"Does '{test_string}' contain special characters? {has_special_character(test_string)}")

test_string = "Hello world"
print(f"Does '{test_string}' contain special characters? {has_special_character(test_string)}")







