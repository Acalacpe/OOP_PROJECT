class PasswordAnalyzer:
    def __init__(self, password):
        self.password = password

    def length(self):
        return len(self.password)

    def has_uppercase(self):
        return any(c.isupper() for c in self.password)

    def has_lowercase(self):
        return any(c.islower() for c in self.password)

    def has_number(self):
        return any(c.isdigit() for c in self.password)

    def has_special(self):
        special = "!@#$%^&*()"
        return any(c in special for c in self.password)