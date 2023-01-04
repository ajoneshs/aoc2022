import re

input = open("input\day4_input.txt", "r").read()
input_list = input.split()

# initializes variables used in for loop below
full_list = []
contained_in_counter = 0
overlap_counter = 0

# determines if either elf's assignment is contained in the other elf's assignment
def contained_in(list):
    # is first assignment in pair contained in second assignment?
    if list[0] >= list[2] and list[1] <= list[3]:
        return True
    # is second assignment in pair contained in first assignment?
    elif list[2] >= list[0] and list[3] <= list[1]:
        return True
    else:
        return False

# determines if there is any overlap between a pair's assignments
def overlaps(list):
    if list[0] >= list[2] and list[0] <= list[3]:
        return True
    if list[1] >= list[2] and list[1] <= list[3]:
        return True
    if list[2] >= list[0] and list[2] <= list[1]:
        return True
    if list[3] >= list[0] and list[3] <= list[1]:
        return True

# goes through input list, looks at each pair, applies the contained_in and overlap functions, and increments the relevant counter if one of the functions returns true
for i in input_list:
    bounds = re.findall(r"\d+", i)
    full_list.append(bounds)
    bounds_as_int_list = [int(j) for j in bounds]
    if contained_in(bounds_as_int_list):
        contained_in_counter += 1
        overlap_counter += 1   # since all instances where contained_in is true, overlap will also be true so saves some time
    elif overlaps(bounds_as_int_list):
        overlap_counter += 1

# answer to part 1 (total number of pairs with an assignment completely contained in partner's assignment)
print('Part 1: ' + str(contained_in_counter))

# answer to part 2 (total number of pairs where assignments overlap at all)
print('Part 2: ' + str(overlap_counter))