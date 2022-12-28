import re

input = open("input\day5_input.txt", "r").read()

initial_crate_layout = [[] for i in range(9)]

# this loop splits up the input .txt file into a matrix of the starting crate positions
for row in input.splitlines()[0:8]: # if i run into an issue, revert to using split('\n') instead of splitlines()
    counter = 3
    col_counter = 0
    for c in row:
        if counter < 4:
            counter += 1
        else:
            if not c.isspace():
                initial_crate_layout[col_counter].insert(0, c)
            col_counter += 1
            counter = 1

# creates a variable of the instructions for how the crates will be moved
instructions = input.splitlines()[10:]

# function that moves crates according to instructions and crane type, and then outputs a string of the crates at the top of each stack
def tops(crate_layout, instructions, crane_type):
    # done to fully copy the list and its component lists, rather than just copying the list's pointer
    crate_layout = [i[:] for i in crate_layout]

    top_crates = ''
    
    for line in instructions:

        current_step = re.findall(r"\d+", line)

        if crane_type == 9000:
            crate_layout[int(current_step[2])-1].extend(reversed(crate_layout[int(current_step[1])-1][-int(current_step[0]):]))
        else:
            crate_layout[int(current_step[2])-1].extend(crate_layout[int(current_step[1])-1][-int(current_step[0]):])
        
        crate_layout[int(current_step[1])-1] = crate_layout[int(current_step[1])-1][0:len(crate_layout[int(current_step[1])-1])-int(current_step[0])]

    for stack in crate_layout:
        top_crates += stack[-1]

    return top_crates

# answer to part 1 (top crates using 9000 crane)
print('Part 1: ' + tops(initial_crate_layout, instructions, 9000))

# answer to part 2 (top crates using 9001 crane)
print('Part 2: ' + tops(initial_crate_layout, instructions, 9001))