import numpy

input = open("input\day9_input.txt", "r").read().splitlines()
#input = open("input\day9_sample_input.txt", "r").read().splitlines()

# used to convert direction into numerical values
dir_dict = {'L': -1, 'R': 1, 'U': 1, 'D': -1}


# outputs sign of input (+ or -)
def sign(input):
    return 1 if input > 0 else -1


# creates a visual representation of the rope head and tail positions
# only works (without modification) with sample input
def visualization(coords, visual_type):
    if visual_type == 1:
        visual = numpy.full((5,6), '.')
    elif visual_type == 2:
        visual = [['.']*6] + [['.']*6] + [['.']*6] + [['.']*6] + [['.']*6]

    for counter, xy_pos in reversed(list(enumerate(coords))):
        visual[4-xy_pos[1]][xy_pos[0]] = str(counter)
        if counter == 0:
            visual[4-xy_pos[1]][xy_pos[0]] = 'H'

    if visual_type == 2:
        visual = '\n'.join([''.join(row) for row in visual])

    header = footer = '_' * 85 + '\n'

    print(header)
    print(coords)
    print(visual)
    print(footer)


# takes current head position (xh and yh), moves them based on the 
# input direction, and outputs new head position
def move_h(head_pos, direction):
    xh, yh = head_pos

    if direction == 'L' or direction == 'R':
        xh += dir_dict[direction]
    if direction == 'U' or direction == 'D':
        yh += dir_dict[direction]

    return xh, yh


# takes changed head position (xh and yh) and current tail position
# (xt and yt), moves them based on new head position, and outputs new 
# tail position
def move_t(past_knot_pos, active_knot_pos):
    xh, yh = past_knot_pos
    xt, yt = active_knot_pos

    if abs(xh-xt) > 1:
        xt += sign(xh-xt)*1
        if yh != yt:
            yt += sign(yh-yt)*1
    if abs(yh-yt) > 1:
        yt += sign(yh-yt)*1
        if xh != xt:
            xt += sign(xh-xt)*1

    return xt, yt


# outputs number of positions visited by tail for given number of knots
def rope_mover(num_knots):
    coords = [[0, 0]] * num_knots
    unique_tail_positions = [(0, 0)]

    for row in input:
        direction = row[0]
        distance = int(row[2:])

        for i in range(distance):
            #
            for counter, xy_pos in enumerate(coords):
                past_knot = coords[counter-1]
                active_knot = coords[counter]

                if counter == 0:
                    coords[0] = move_h(coords[0], direction)
                else:
                    coords[counter] = move_t(past_knot, active_knot)
            
            # goes through coords generated this loop and adds new tail positions
            if coords[num_knots-1] not in unique_tail_positions:
                unique_tail_positions.append(coords[num_knots-1])

            #visualization(coords, 2)

    return unique_tail_positions


# answer to part 1 (total unique spaces visited by tail with 2 knots)
print('Part 1: ' + str(len(rope_mover(2))))

# answer to part 2 (total unique spaces visited by tail with 10 knots)
print('Part 2: ' + str(len(rope_mover(10))))