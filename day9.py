import numpy
#input = open("input\day9_input.txt", "r").read().splitlines()
input = open("input\day9_sample_input.txt", "r").read().splitlines()



# used to convert direction into numerical values
dir_dict = {'L': -1, 'R': 1, 'U': 1, 'D': -1}

# the list that all tail positions will be added to
tail_positions = ['0, 0']


# creates a visual representation of the rope head and tail positions
# must change size of array assigned to visual to match input being used
def visualization(coords):
    print('len coords below')
    print(len(coords))
    visual = numpy.full((5,6), '.')
    for counter, xy_pos in coords[::-1]:
        visual[4-coords[counter][1]][coords[counter][0]] = str(counter)
        if counter == len(coords) - 1:
            visual[4-coords[counter][1]][coords[counter][0]] = 'h'
    return visual

#print(visualization(xh, yh, xt, yt))

# takes current head position (xh and yh), moves them based on the input direction, and outputs new head position
def move_h(head_pos, direction, increment_or_decrement):
    xh, yh = head_pos
    if direction == 'L' or direction == 'R':
        xh += increment_or_decrement
    if direction == 'U' or direction == 'D':
        yh += increment_or_decrement
    return xh, yh


# takes changed head position (xh and yh) and current tail position (xt and yt), moves them based on new head position, and outputs new tail position
def move_t(past_knot_pos, active_knot_pos, increment_or_decrement):              #move_t(xh, yh, xt, yt, increment_or_decrement):          
    xh, yh = past_knot_pos
    xt, yt = active_knot_pos
    if abs(xh-xt) > 1:
        xt += increment_or_decrement
        if yh != yt:
            yt += yh-yt
    if abs(yh-yt) > 1:
        yt += increment_or_decrement
        if xh != xt:
            xt += xh-xt
    return xt, yt

# for part 1:
num_knots = 1
# a list of


def rope_mover(num_knots):
    coords = [[0, 0]] + [[0, 0]] * num_knots

    for row in input:
        direction = row[0]
        distance = int(row[2:])
        increment_or_decrement = dir_dict[direction]

        for i in range(distance):
            #**replace this block with for counter, xy pos i enumerate
            for counter, xy_pos in enumerate(coords):
                if counter == 0:
                    coords[0] = move_h(coords[0], direction, increment_or_decrement)
                else:
                    coords[counter] = move_t(coords[counter-1], coords[counter], increment_or_decrement)
            print(visualization(coords))
            print('\n')
    return coords


print(rope_mover(1))




# feeds input to move_h and move_t and adds results to tail_positions




# answer to part 1 (total number of unique positions visited by tail)
#print(len(set(tail_positions)))





#pretty sure I'll need to change how increment_or_decrement is defined
# think it should be y_past - y_active or x_past - x_active