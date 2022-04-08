# File : Standard files | Directories
import os


class File:

    def __init__(self, path):
        self.path = path

    def typeoffile(self):
        if os.path.isfile(self.path):
            return "standard file"
        elif os.path.isdir(self.path):
            return "dir"
        else:
            return "not a file"



absolute_path = os.path.dirname(__file__)
print(absolute_path)