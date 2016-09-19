

# First way to open a file

open_file = open("data_file.txt")
contents = open_file.readlines()
print(contents)
open_file.close()


# Second way to open a file

with open("data_file.txt") as better_open_file:
    better_contents = better_open_file.read()

print(better_contents)
