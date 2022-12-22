import os

class File:
    def __init__(self, filename: str, mode: str) -> None:
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        if os.path.isfile(self.filename):
            self.file = open(self.filename, self.mode)
        else:
            self.file = open(self.filename, 'w+')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.file.close()
        return True

with File('example.txt', 'a+') as file:
    file.write('Всем привет!')
