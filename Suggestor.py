import random
import os
from patterns import get_keyboard_patterns

class Suggestor:
    def suggestPass(password):
        
        file_path = os.path.join('data', 'english_wikipedia.txt')
        
        password = Suggestor.remove_sequences(password)
        password = Suggestor.remove_repetitions(password)
        password = Suggestor.remove_keyboard_sequences(password)
        
        if password.isdigit():
            try:
                with open(file_path, 'r') as file:
                    words = []
                    for line in file:
                        if line.strip():
                            word = line.strip().split()[0]
                            words.append(word)
                
                if words:
                    random_word = random.choice(words)
                    random_word = random_word.capitalize()
                    password = random_word
                
            except FileNotFoundError:
                print(f"Warning: {file_path} not found")
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

        if len(password) < 5:
            try:
                with open(file_path, 'r') as file:
                    words = []
                    for line in file:
                        if line.strip():
                            word = line.strip().split()[0]
                            words.append(word)
                if words:
                    random_word = random.choice(words)
                    password = password + "_" + random_word
                
            except FileNotFoundError:
                print(f"Warning: {file_path} not found")
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

        passw = list(password)
        
        symbol = random.choice(['!', '@', '#', '$'])
        if symbol == '!':
            if 'l' in passw:
                passw[passw.index('l')] = '!'
            elif 'i' in passw:
                passw[passw.index('i')] = '!'
            else:
                passw.append(symbol)
        elif symbol == '@':
            if 'a' in passw:
                passw[passw.index('a')] = '@'
            else:
                passw.append(symbol)
        elif symbol == '$':
            if 's' in passw:
                passw[passw.index('s')] = '$'
            else:
                passw.append(symbol)
        elif symbol == '#':
            if 'h' in passw:
                passw[passw.index('h')] = '#'
            else:
                passw.append(symbol)

        index = random.randint(0, len(passw)-1)
        passw[index] = passw[index].upper()
        
        password = ''.join(passw)

        if len(password) > 7:
            num = random.randint(0, 10)
        elif len(password) > 6:
            num = random.randint(10, 100)
        else:
            num = random.randint(100, 1000)
        password += str(num)
        
        return password
    
    def remove_sequences(password):
        password_list = list(password)
        i = 0
        
        while i < len(password_list) - 2:
            if password_list[i].isdigit() and password_list[i+1].isdigit() and password_list[i+2].isdigit():
                num1 = ord(password_list[i])
                num2 = ord(password_list[i+1])
                num3 = ord(password_list[i+2])
                
                if (num2 - num1 == 1 and num3 - num2 == 1) or (num2 - num1 == -1 and num3 - num2 == -1):
                    del password_list[i+1]
                    continue
            
            elif password_list[i].isalpha() and password_list[i+1].isalpha() and password_list[i+2].isalpha():
                char1 = ord(password_list[i].lower())
                char2 = ord(password_list[i+1].lower())
                char3 = ord(password_list[i+2].lower())
                
                if (char2 - char1 == 1 and char3 - char2 == 1) or (char2 - char1 == -1 and char3 - char2 == -1):
                    del password_list[i+1]
                    continue
            
            i += 1
        
        return ''.join(password_list)
    
    def remove_repetitions(password):
        password_list = list(password)
        i = 0
        
        while i < len(password_list) - 2:
            if password_list[i] == password_list[i+1] == password_list[i+2]:
                del password_list[i+1]
                continue
            i += 1
        
        return ''.join(password_list)
    
    def remove_keyboard_sequences(password):
        patterns = get_keyboard_patterns()
        result = password
        password_lower = password.lower()
        
        patterns_sorted = sorted(patterns, key=len, reverse=True)
        
        for pattern in patterns_sorted:
            if pattern in password_lower:
                result = result.replace(pattern, "")
                break
        
        return result