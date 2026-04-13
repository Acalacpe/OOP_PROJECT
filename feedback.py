import os
from patterns import has_sequence, has_repetition
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

    if has_sequence(password):
        feedback.append("Avoid sequences like 123 or abc")

    if has_repetition(password):
        feedback.append("Avoid repeating characters")

    return feedback


def check_dataset(password):
    reader = TextFileReaderWriter()
    base_dir = os.path.dirname(__file__)

    datasets = {
        "passwords": "data/passwords.txt",
        "names": [
            "data/female_names.txt",
            "data/male_names.txt",
            "data/surnames.txt"
        ],
        "dictionary": "data/english_wikipedia.txt"
    }


    
    for file in datasets["names"]:
        word_list = reader.read(os.path.join(base_dir, file))
        for word in word_list:
            if password.lower() == word.lower():
                return "names", word
    
    word_list = reader.read(os.path.join(base_dir, datasets["dictionary"]))
    for word in word_list:
        if password.lower() == word.lower():
            return "dictionary", word
        
    word_list = reader.read(os.path.join(base_dir, datasets["passwords"]))
    for word in word_list:
        if password.lower() == word.lower():
            return "passwords", word

    return None, None