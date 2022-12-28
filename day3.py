input = open("input\day3_input.txt", "r").read()

# a list where each element consists of the contents of one haversack
input_list = input.split()

# takes item type (letter) as input and outputs its priority
def get_priority(i):
    if i.islower():
        priority = ord(i) - 96
    if i.isupper():            # might just want else here although this improves readability at cost of efficiency
        priority = ord(i) - 38
    return priority

# initializes variables used in for loop below
priority_sum = 0
priority_sum2 = 0
counter = 0
group = []

# runs through each haversack, finds the duplicate item, and adds the item's priority to the total
for i in input_list:

    # splits each element of the list into two parts, finds the element present in both parts, then adds the corresponding priority to the total
    midpoint = int(0.5 * len(i))
    p1 = i[0:midpoint]
    p2 = i[midpoint:]
    for item in p1:
        if item in p2:
            priority_sum += get_priority(item)
            break
    
    # splits list into groups of 3, searches for the group's badge (the character they all have in common), then adds the corresponding priority to the total
    group.append(i)
    counter += 1
    if counter == 3:
        for j in group[0]:
            if j in group[1] and j in group[2]:
                priority_sum2 += + get_priority(j)
                break
        group = []
        counter = 0


# answer to part 1 (total priority of all items contained in both compartments of a haversack)
print('Part 1: ' + str(priority_sum))

# answer to part 2 (sum of priorities of all groups' badges)
print('Part 2: ' + str(priority_sum2))