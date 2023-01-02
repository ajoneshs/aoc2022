import numpy

input = open("input\day10_input.txt", "r").read().splitlines()
#input = open("input\day10_sample_input.txt", "r").read().splitlines()

cycles = 0
ss_at_cycle = [0]
X = 1
visual = []
for i in range(6):
    visual.append(['.']*40)


for line in input:
    cycles += 1
    ss_at_cycle.append(X*cycles)
    if (cycles-1)%40 in range(X-1, X+2):
        visual[(cycles-1)//40][(cycles-1)%40] = '#'

    if 'addx' in line:
        cycles += 1
        ss_at_cycle.append(X*cycles)
        if (cycles-1)%40 in range(X-1, X+2):
            visual[(cycles-1)//40][(cycles-1)%40] = '#'

        X += int(line[5:])


# answer to part 1 (sum of signal strengths at given intervals)
print(sum([ss_at_cycle[20], ss_at_cycle[60], ss_at_cycle[100], ss_at_cycle[140], ss_at_cycle[180], ss_at_cycle[220]]))

# answer to part 2 ()
print('\n'.join([''.join(i) for i in visual]))