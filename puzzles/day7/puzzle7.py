import os
import sys
from pydantic import BaseModel

sys.setrecursionlimit(2000)

# Testing data ---------------------------------------------------------------
test = """\
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

# Setting up the data --------------------------------------------------------

# Read the input file
path = os.getcwd() + r"\puzzles\day7\input.txt"
with open(path) as f:
    lines = f.read()

test = test.split("\n")
commands = lines.split("\n")

# PART ONE -------------------------------------------------------------------


class File(BaseModel):
    size: int
    name: str


class Directory(BaseModel):
    name: str
    parent: "Directory" = None
    subdirs: list["Directory"] = None
    files: list[File] = None
    size: int = 0

    def add_subdir(self, dir: "Directory"):
        dir.parent = self
        if self.subdirs is None:
            self.subdirs = [dir]
        else:
            self.subdirs.append(dir)

    def add_file(self, file: File):
        self.size += file.size

        current_parent = self.parent
        while current_parent is not None:
            current_parent.size += file.size
            current_parent = current_parent.parent

        if self.files is None:
            self.files = [file]
        else:
            self.files.append(file)

    def get_subdir(self, search_str: str):
        if self.subdirs is None:
            return None
        for dir in self.subdirs:
            if search_str == dir.name:
                return dir


def initalizalize_directory(data):
    return Directory(name=data.pop(0).split()[2])


def parse_command(commands, current_dir: Directory):
    if len(commands) == 0:
        return
    command = commands.pop(0)

    match command.split():
        case ["$", "cd", ".."]:
            parse_command(commands, current_dir.parent)
        case ["$", "cd", dir]:
            parse_command(commands, current_dir.get_subdir(dir))
        case ["dir", new_dir]:
            current_dir.add_subdir(Directory(name=new_dir))
            parse_command(commands, current_dir)
        case ["$", "ls"]:
            parse_command(commands, current_dir)
        case [size, filename]:
            current_dir.add_file(File(size=size, name=filename))
            parse_command(commands, current_dir)


def get_dir_sizes(input_dir: Directory, result=[]):
    if input_dir.parent is None:
        result.append(input_dir.size)

    for dir in input_dir.subdirs:
        result.append(dir.size)
        if dir.subdirs is not None:
            get_dir_sizes(dir, result=result)
    return result


# dir = initalizalize_directory(test)
# parse_command(test, dir)

dir = initalizalize_directory(commands)
parse_command(commands, dir)

dir_sizes = get_dir_sizes(dir)
p1_solution = sum([size for size in dir_sizes if size <= 100000])

# Output for PART ONE
print("---PART ONE---")
print("Answer to puzzle:", p1_solution)

# PART TWO -------------------------------------------------------------------

amount_to_delete = 30000000 - (70000000 - dir.size)
p2_solution = min([size for size in dir_sizes if size >= amount_to_delete])

# Output for PART TWO
print("---PART TWO---")
print("Answer to puzzle:", p2_solution)
