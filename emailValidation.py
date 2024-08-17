import re

def fnEmailValidation(email):
    if re.match(f"[^@]+@[^@]+\.[^@]+", email):
        return True
    return False

email = input('Enter email address: ')
fnEmailValidation(email)