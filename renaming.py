# Part of the way through Advent of Code I decided I wanted to clean up my
# project folder by creating a subfolder for all the input files. This script
# moves each input file to the input folder, and updates each file to refer
# to the new location for the input files

import os
import re
import git

solutions_dir = 'C:\eng\\aoc2022'
input_dir = 'C:\eng\\aoc2022\input'
repo = git.Repo(solutions_dir)


# changes file name from dayn... to day0n... where n is a single digit
# double digit days are left alone
def name_changer(dir):
    intermediate_list = []
    intermediate_list_changed = []
    os.chdir(dir)
    for file in os.listdir():
        match = re.findall(r'\d+', file)
        if match and len(match[0]) == 1:
            new_name = file[0:3] + str(0) + file[3:]
            os.rename(file, new_name)
            intermediate_list.append(file)
            intermediate_list_changed.append(new_name)
            print(f"{file} was renamed to {new_name}")
    return intermediate_list, intermediate_list_changed


def commit_name_change(option, old_names, new_names):
    prefix = ''
    if option == 'input':
        prefix = 'input/'
    for counter, new_name in enumerate(new_names):
        repo.git.add(prefix + new_name)
        repo.git.rm(prefix + old_names[counter])
        print(f"{old_names[counter]} was renamed to {new_name}")
    message = f"Rename single digit {option} file names"
    repo.git.commit('-m', message)
    print(f"Committed with message: {message}")


# takes directory as input, looks inside files, finds all instances
# where there is a single digit day number, and adds a 0 in front
# i.e. day1 -> day01
def file_editor(dir):
    os.chdir(solutions_dir)
    edited_files = []
    # just means for all items in dir that are not folders
    for file in [file for file in os.listdir() if os.path.isfile(os.path.join(dir, file))]:
        match = re.findall(r'\d+', file)
        if match and len(match[0]) == 1:
            edited_files.append(file)
            with open(file, 'r') as f:
                file_contents = f.read().splitlines()

            for counter, line in enumerate(file_contents):
                match = re.findall(r'input\\day\d+_(?:input|sample_input).txt', line)
                if match:
                    submatch = re.findall(r'\d+', match[0])
                    line = line.replace(submatch[0], ("0" + submatch[0]))
                    file_contents[counter] = line
                    print(f"{file} line #{counter} was edited to say {line}")

            with open(file, 'w') as f:
                f.write('\n'.join(file_contents))
    return edited_files


def commit_file_edits(edited_files):
    for file in edited_files:
        repo.git.add(file)
    message = "Edit files to reflect changed input names"
    repo.git.commit('-m', message)
    print(f"Committed with message: {message}")


edited_files = file_editor(solutions_dir)
commit_file_edits(edited_files)

solutions_old_names, solutions_new_names = name_changer(solutions_dir)
inputs_old_names, inputs_new_names = name_changer(input_dir)
commit_name_change('solution', solutions_old_names, solutions_new_names)
commit_name_change('input', inputs_old_names, inputs_new_names)

repo.git.push()