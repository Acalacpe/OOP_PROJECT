import random
import string

class Suggestor:
    def suggestPass(password):

        base = list(password)

        lower = random.choice(string.ascii_lowercase)
        upper = random.choice(string.ascii_uppercase)
        digit = random.choice(string.digits)
        symbol = random.choice("!@#$%^&*")

        base = base[:10]

        base.extend([lower, upper, digit, symbol])

        while len(base) < 16:
            base.append(random.choice(string.ascii_letters + string.digits + "!@#$%^&*"))

        random.shuffle(base)

        return ''.join(base)