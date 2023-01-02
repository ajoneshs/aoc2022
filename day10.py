input = open("input\day10_input.txt", "r").read().splitlines()
#input = open("input\day10_sample_input.txt", "r").read().splitlines()

cycles = 0
ss_at_cycle = [0]
X = 1

for line in input:
    cycles += 1
    ss_at_cycle.append(X*cycles)
    if cycles == 220:
        print('X at 220 below')
        print(X)
    if 'addx' in line:
        cycles += 1
        ss_at_cycle.append(X*cycles)
        X += int(line[5:])

# answer to part 1 (sum of signal strengths at given intervals)
print(sum([ss_at_cycle[20], ss_at_cycle[60], ss_at_cycle[100], ss_at_cycle[140], ss_at_cycle[180], ss_at_cycle[220]]))