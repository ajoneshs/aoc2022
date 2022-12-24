import numpy
input = open("day9_input.txt", "r").read().splitlines()
#input = open("day9_sample_input.txt", "r").read().splitlines()

# head x and y positions and tail x and y positions
xh, yh, xt, yt = 0, 0, 0, 0

# used to convert direction into numerical values
dir_dict = {'L': -1, 'R': 1, 'U': 1, 'D': -1}

# the list that all tail positions will be added to
tail_positions = ['0, 0']


# creates a visual representation of the rope head and tail positions
# must change size of array assigned to visual to match input being used
def visualization(xh, yh, xt, yt):
    visual = numpy.full((5,6), '.')
    visual[4-yt][xt] = 't'
    visual[4-yh][xh] = 'h'
    return visual

#print(visualization(xh, yh, xt, yt))

# takes current head position (xh and yh), moves them based on the input direction, and outputs new head position
def move_h(xh, yh, direction, increment_or_decrement):
    if direction == 'L' or direction == 'R':
        xh += increment_or_decrement
    if direction == 'U' or direction == 'D':
        yh += increment_or_decrement
    return xh, yh


# takes changed head position (xh and yh) and current tail position (xt and yt), moves them based on new head position, and outputs new tail position
def move_t(xh, yh, xt, yt, increment_or_decrement):
    if abs(xh-xt) > 1:
        xt += increment_or_decrement
        if yh != yt:
            yt += yh-yt
    if abs(yh-yt) > 1:
        yt += increment_or_decrement
        if xh != xt:
            xt += xh-xt
    return xt, yt



# feeds input to move_h and move_t and adds results to tail_positions
for row in input:
    direction = row[0]
    distance = int(row[2:])
    increment_or_decrement = dir_dict[direction]

    for i in range(distance):
        xh, yh, = move_h(xh, yh, direction, increment_or_decrement)
        xt, yt = move_t(xh, yh, xt, yt, increment_or_decrement)
        tail_positions.append(str(xt) + ', ' + str(yt))

        #print(visualization(xh, yh, xt, yt))
        #print('\n')


# answer to part 1 (total number of unique positions visited by tail)
print(len(set(tail_positions)))