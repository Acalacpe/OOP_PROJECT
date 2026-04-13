import random
import string

class Generator:
    def generate():
        lower = random.choice(string.ascii_lowercase)
        upper = random.choice(string.ascii_uppercase)
        digit = random.choice(string.digits)
        symbol = random.choice("!@#$%^&*")

        rest = ''.join(random.choice(string.ascii_letters + string.digits + "!@#$%^&*") for _ in range(12))

        password = list(lower + upper + digit + symbol + rest)
        random.shuffle(password)

        return ''.join(password)