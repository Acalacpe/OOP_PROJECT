import os
import re
from patterns import get_sequence_pattern, get_repetition_char, get_keyboard_patterns
from TextFileReaderWriter import TextFileReaderWriter


def get_feedback(password, analyzer):
    feedback = []
    dataset_results = check_dataset(password)

    if "passwords" in dataset_results:
        feedback.append(f"Don't use common passwords: {', '.join(dataset_results['passwords'])}")

    if "names" in dataset_results:
        feedback.append(f"Avoid using names: {', '.join(dataset_results['names'])}")

    if "dictionary" in dataset_results:
        feedback.append(f"Avoid dictionary words: {', '.join(dataset_results['dictionary'])}")

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


def split_words(password):
    parts = re.findall(r'[A-Z]?[a-z]+|[A-Z]+(?=[A-Z]|$)', password)
    return [p.lower() for p in parts if len(p) >= 4]

def check_dataset(password):
    reader = TextFileReaderWriter()
    base_dir = os.path.dirname(__file__)
    password_lower = password.lower()
    split_parts = split_words(password)

    def is_valid(word):
        return len(word) >= 4 and word.isalpha()

    def collect_matches(word_list):
        matches = set()
        for word in word_list:
            word_clean = word.strip().lower()
            if not is_valid(word_clean):
                continue

            if word_clean in password_lower:
                matches.add(word_clean)

            for part in split_parts:
                if word_clean == part:
                    matches.add(word_clean)

        return matches

    results = {
        "passwords": set(),
        "names": set(),
        "dictionary": set()
    }

    results["passwords"] = collect_matches(
        reader.read(os.path.join(base_dir, "data/passwords.txt"))
    )

    name_files = [
        "data/female_names.txt",
        "data/male_names.txt",
        "data/surnames.txt"
    ]

    for file in name_files:
        results["names"].update(
            collect_matches(reader.read(os.path.join(base_dir, file)))
        )

    results["dictionary"] = collect_matches(
        reader.read(os.path.join(base_dir, "data/english_wikipedia.txt"))
    )

    return {k: sorted(v) for k, v in results.items() if v}