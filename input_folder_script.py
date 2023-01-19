# Part of the way through Advent of Code I decided I wanted to clean up my
# project folder by creating a subfolder for all the input files. This script
# moves each input file to the input folder, and updates each file to refer
# to the new location for the input files

import os
import shutil
import re

os.chdir('C:\eng\\aoc2022')
input_dir = 'C:\eng\\aoc2022\\input'

# moves input files from from the parent folder to the input folder
for file_name in os.listdir():
    if '_input.txt' in file_name:
        shutil.move(file_name, input_dir)
        print("successfully moved " + file_name + " to input folder")


# takes file as input, searches for text of format dayn_input.txt or 
# dayn_sample_input.txt, and adds input\\ before any matches, then writes
# the file
def file_editor(input_file):
    with open(input_file, 'r') as f:
        file_contents = f.read().splitlines()

    for counter, line in enumerate(file_contents):
        match = re.findall(r'day\d+_(?:input|sample_input).txt', line)
        if match:
            for match_counter, instance in enumerate(match):
                line = line.replace(instance, 'input\\' + match[match_counter], 1)
            file_contents[counter] = line

    with open(input_file, 'w') as f:
        f.write('\n'.join(file_contents))


# runs file_editor on all aoc day files
for file_name in os.listdir():
    if '.py' in file_name and 'input_folder_script' not in file_name:
        file_editor(file_name)
        print(file_name + " was edited")