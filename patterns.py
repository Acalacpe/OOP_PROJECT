def has_sequence(password):
    sequences = ["123", "abc", "qwerty", "asd"]
    return any(seq in password.lower() for seq in sequences)

def has_repetition(password):
    return any(password.count(c) > 2 for c in password)