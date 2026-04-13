from CSVFileReaderWriter import CSVFileReaderWriter
import csv
import os

reader = CSVFileReaderWriter()
keyboard_patterns = []

def load_keyboard_patterns():
    global keyboard_patterns
    file_path = os.path.join('data', 'keyboard_patterns.csv')
    keyboard_patterns = reader.read(file_path, column_name='pattern')
    print(f"Loaded {len(keyboard_patterns)} keyboard patterns")

def get_keyboard_patterns():
    global keyboard_patterns
    if not keyboard_patterns:
        load_keyboard_patterns()
    return keyboard_patterns

def has_sequence(password):
    password_lower = password.lower()
    
    for i in range(len(password_lower) - 2):
        char1 = ord(password_lower[i])
        char2 = ord(password_lower[i + 1])
        char3 = ord(password_lower[i + 2])
        
        if char2 - char1 == 1 and char3 - char2 == 1:
            return True
        
        if char2 - char1 == -1 and char3 - char2 == -1:
            return True
    
    return False

def get_sequence_pattern(password):
    password_lower = password.lower()
    
    for i in range(len(password_lower) - 2):
        char1 = ord(password_lower[i])
        char2 = ord(password_lower[i + 1])
        char3 = ord(password_lower[i + 2])
        
        if char2 - char1 == 1 and char3 - char2 == 1:
            return password_lower[i:i+3]
        
        if char2 - char1 == -1 and char3 - char2 == -1:
            return password_lower[i:i+3]
    
    return None

def has_repetition(password):
    return any(password.count(c) > 2 for c in password)

def get_repetition_char(password):
    for c in password:
        if password.count(c) > 2:
            return c
    return None