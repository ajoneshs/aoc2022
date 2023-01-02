input = open("input\day10_input.txt", "r").read().splitlines()
#input = open("input\day10_sample_input.txt", "r").read().splitlines()

# initializes variables used in for loop below
cycles = 0
ss_at_cycle = [0]
X = 1
# creates a 6x40 matrix of dots
visual = []
for i in range(6):
    visual.append(['.']*40)


# runs through each line in input
for line in input:
    # starts with incrementing the current cycle and adding the signal strenth 
    # to the list
    cycles += 1
    ss_at_cycle.append(X*cycles)
    # replaces the corresponding . with a # if the sprite overlaps with the 
    # current draw position
    if (cycles-1)%40 in range(X-1, X+2):
        visual[(cycles-1)//40][(cycles-1)%40] = '#'

    # addx takes two cycles, so this repeats above process, and increments/
    # decrements X according to the instructions
    if 'addx' in line:
        cycles += 1
        ss_at_cycle.append(X*cycles)
        if (cycles-1)%40 in range(X-1, X+2):
            visual[(cycles-1)//40][(cycles-1)%40] = '#'

        X += int(line[5:])


# answer to part 1 (sum of signal strengths at given intervals)
print(sum([ss_at_cycle[20], ss_at_cycle[60], ss_at_cycle[100], ss_at_cycle[140], ss_at_cycle[180], ss_at_cycle[220]]))

# answer to part 2 (letters appearing on screen)
print('\n'.join([''.join(i) for i in visual]))