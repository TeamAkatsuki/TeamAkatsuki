import os

class MyDir:
    def __init__(self, dir):
        self.dir = dir
        self.files = []

    def dir_list(self):
        with os.scandir(self.dir) as entries:
            for entry in entries:
                self.files.append(entry.name)

    def helloworld(self):
        with open("{}/helloworld.txt".format(self.dir),'w') as file:
            file.write("hello world")

class MyDir2:
    def __init__(self, dir):
        self.dir = dir

    def dir_list(self):
        files = []
        with os.scandir(self.dir) as entries:
            for entry in entries:
                files.append(entry.name)
        return files


class MyDir3:
    def __init__(self, dir):
        self.dir = dir
        self.files = []
        self.dir_list()

    def dir_list(self):
        with os.scandir(self.dir) as entries:
            for entry in entries:
                self.files.append(entry.name)

    def create_file(self, filename="untitled.txt", message="hi"):
        with open("{}/{}".format(self.dir, filename), "w") as f:
            f.write(message)

# with open("foo.txt", "w") as f:
#     f.write("Life is too short, you need python")

a = MyDir()
a.hellowrld()