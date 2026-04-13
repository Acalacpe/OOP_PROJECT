import math

def calculate_entropy(password):

    if not password:
        return 0

    password = str(password)

    charset = 0

    if any(c.islower() for c in password):
        charset += 26
    if any(c.isupper() for c in password):
        charset += 26
    if any(c.isdigit() for c in password):
        charset += 10
    if any(c in "!@#$%^&*()" for c in password):
        charset += 10

    if charset == 0:
        return 0

    return len(password) * math.log2(charset)