# need to refactor this

input = open("day8_input.txt", "r").read().splitlines()       #note there is no splitlines() here
#input = open("day8_sample_input.txt", "r").read().splitlines()

# size of position matrix assuming it is square
n = len(input[0])

# hid_or_vis determines if an individual tree at coordinates (x, y) is hidden or visible
def hid_or_vis(x, y):
    L, R, A, B = False, False, False, False
    current_tree_height = input[y][x]
    for i in range(x)[::-1]: # if visible from left
        if input[y][i] >= current_tree_height:
            L = True
            break
    for i in range(x+1, n): # if visible from right
        if input[y][i] >= current_tree_height:
            R = True
            break
    for i in range(y)[::-1]: # if visible from above
        if input[i][x] >= current_tree_height:
            A = True
            break
    for i in range(y+1, n): # if visible from below
        if input[i][x] >= current_tree_height:
            B = True
            break
    if L and R and A and B:
        return 'h'
    else:
        return 'v'

# scenic_score calculates the scenic score of each individual tree and returns a list of these values
def scenic_score(x, y):
    L, R, A, B = False, False, False, False
    Lss, Rss, Ass, Bss = 0, 0, 0, 0
    current_tree_height = input[y][x]
    for i in range(x)[::-1]: # if visible from left
        Lss = x
        if input[y][i] >= current_tree_height:
            Lss = x - i
            break
    for i in range(x+1, n): # if visible from right
        Rss = n - x - 1
        if input[y][i] >= current_tree_height:
            Rss = i - x
            break
    for i in range(y)[::-1]: # if visible from above
        Ass = y
        if input[i][x] >= current_tree_height:
            Ass = y - i
            break
    for i in range(y+1, n): # if visible from below
        Bss = n - y - 1
        if input[i][x] >= current_tree_height:
            Bss = i - y
            break
    return Lss * Rss * Ass * Bss

scenic_scores = []
output = []
x = 0
y = 0

for row in input:
    output.append([])
    scenic_scores.append([])
    for column in row:
        output[y] += hid_or_vis(x, y)
        scenic_scores[y].append(scenic_score(x, y))
        x += 1
    x = 0
    y += 1



visible_counter = 0
# finds the number of visible trees in output variable
for row in output:
    for i in row:
        if i == 'v':
            visible_counter += 1


max_ss = 0
# finds highest scenic score from list (is it a list?????????????)
for row in scenic_scores:
    for i in row:
        if int(i) >= max_ss:
            max_ss = int(i)

# answer to part 1 (total number of visible trees)
print(visible_counter)

# answer to part 2 (highest possible scenic score)
print(max_ss)