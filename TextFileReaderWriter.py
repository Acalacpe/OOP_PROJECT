class TextFileReaderWriter:
    def read(self, filename):
        try:
            with open(filename, 'r', encoding="utf-8") as file:
                words = []
                for line in file:
                    clean = line.strip().split()[0]  # 👈 takes ONLY first word
                    if clean:
                        words.append(clean.lower())
                return words
        except FileNotFoundError:
            return []