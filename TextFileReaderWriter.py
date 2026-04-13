from FileReaderWriter import FileReaderWriter

class TextFileReaderWriter(FileReaderWriter):
    def read(self, filename):
        try:
            with open(filename, 'r') as file:
                words = []
                for line in file:
                    words.extend(line.split())
                return words
            
        except FileNotFoundError:
            print(f"Warning: {filename} not found in the current directory")
            return []
        except Exception as e:
            print(f"Error reading {filename}: {e}")
            return []
            

    def write(self, filepath, data):
        with open(filepath, "w") as text_file:
            text_file.write(data)
