from TextFileReaderWriter import TextFileReaderWriter
from timeFormat import timeFormat

def findCrackTime(password):
    time = 0
    found = False
    reader = TextFileReaderWriter()

    files = [
    'data/passwords.txt',
    'data/female_names.txt',
    'data/male_names.txt',
    'data/surnames.txt',
    'data/english_wikipedia.txt'
]

    for filename in files:
        if found:
            break

        word_list = reader.read(filename)

        if password in word_list:
            index = word_list.index(password)
            time = index * 0.1
            found = True
        else:
            time += len(word_list) * 0.1

    if not found:
        additional = 1
        for char in password:
            additional *= (ord(char) * 0.1)
        time += additional

    return timeFormat(int(time))