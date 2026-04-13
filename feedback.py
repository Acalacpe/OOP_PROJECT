import os
from patterns import get_sequence_pattern, get_repetition_char, get_keyboard_patterns
from TextFileReaderWriter import TextFileReaderWriter


def get_feedback(password, analyzer):
    feedback = []
    category, match = check_dataset(password)

    if category == "passwords":
        feedback.append(f"Don't use common passwords = {match}")

    elif category == "names":
        feedback.append(f"Don't use names = {match}")

    elif category == "dictionary":
        feedback.append(f"Don't use word = {match}")

    if len(password) < 8:
        feedback.append("Use at least 8 characters")

    if not analyzer.has_uppercase():
        feedback.append("Add uppercase letters")

    if not analyzer.has_lowercase():
        feedback.append("Add lowercase letters")

    if not analyzer.has_number():
        feedback.append("Include numbers")

    if not analyzer.has_special():
        feedback.append("Use special characters")

    sequence = get_sequence_pattern(password)
    if sequence:
        feedback.append(f"Avoid sequence = {sequence}")
    else:
        keyboard_patterns = get_keyboard_patterns()
        password_lower = password.lower()
        
        for pattern in keyboard_patterns:
            if pattern in password_lower:
                feedback.append(f"Avoid sequence = {pattern}")
                break

    repetition = get_repetition_char(password)
    if repetition:
        feedback.append(f"Avoid repeating character = '{repetition}'")

    return feedback


def check_dataset(password):
    reader = TextFileReaderWriter()
    base_dir = os.path.dirname(__file__)
    password_lower = password.lower()

    
    name_files = [
        "data/female_names.txt",
        "data/male_names.txt",
        "data/surnames.txt"
    ]


    word_list = reader.read(os.path.join(base_dir, "data/passwords.txt"))
    for word in word_list:
        word_clean = word.strip().lower()
        if word_clean in password_lower:
            return "passwords", word_clean


    for file in name_files:
        word_list = reader.read(os.path.join(base_dir, file))
        for word in word_list:
            word_clean = word.strip().lower()
            if word_clean in password_lower:
                return "names", word_clean

    
    word_list = reader.read(os.path.join(base_dir, "data/english_wikipedia.txt"))
    for word in word_list:
        word_clean = word.strip().lower()
        if word_clean in password_lower:
            return "dictionary", word_clean


    return None, None