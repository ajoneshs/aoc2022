import re
import anytree

input = open("input\day07_input.txt", "r").read()

level = 0
current_action = ''
file_system = []
dir_sizes = {}
temp_list = []

for line in input.splitlines():
    # user initiated actions
    if line[0] == '$':
        if line[2:4] == 'cd':
            if line[5] == '/':
                level = 0
                active_dir = '/'
                print('outermost dir')
                print(level)
            if line[5:7] == '..':
                level -= 1
                print(line)
                print('went back one')
                print(level)
            else:
                level += 1
                print(line)
                print('went forward one')
                print(level)
                temp_list.append(line[5:])
        if line[2:4] == 'ls':
            print(line)
            print('listing dirs')
            current_action = 'ls'
    # output to user initiated action
    else:
        if current_action == 'ls':
            if line[0:3] == 'dir':
                new_dir = line[4:]
            else:
                space = line.find(' ')   # does assigning a variable to a value that I'll use multiple times save time?
                new_file = line[space+1:]
                new_file_size = line[0:space]
                print('found a new file with file size')
                print(new_file)
                print(new_file_size)


print(temp_list)

print(len(temp_list) == len(set(temp_list)))
print(len(temp_list))
print(len(set(temp_list)))