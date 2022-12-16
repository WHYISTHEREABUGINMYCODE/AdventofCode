import os
# gets file relative to inputs directory (e.g. pass in 'day1/input.txt')
def read_input(filepath):
    with open(os.getcwd() + "/inputs/" + filepath, "r") as f:
        return f.read()