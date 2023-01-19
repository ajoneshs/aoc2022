import re
import copy

input = open("input\day11_input.txt", "r").read().split('\n\n')
#input = open("input\day11_sample_input.txt", "r").read().split('\n\n')

monkeys = []
inventories_original = []
operations = []
tests = []
recipient_if_true_list = []
recipient_if_false_list = []

def setup(input):
    for block in input:
        split_block = block.splitlines()
        monkey = re.findall('\d+', split_block[0])
        inventory = re.findall('\d+', split_block[1])
        operation = re.findall('(\*|\+) (\d+|old)', split_block[2])
        test = re.findall('\d+', split_block[3])
        recipient_if_true = re.findall('\d+', split_block[4])
        recipient_if_false = re.findall('\d+', split_block[5])

        # eventually organize this better
        monkeys.append(int(monkey[0]))
        inventories_original.append(inventory)
        operations.append(operation[0])
        tests.append(int(test[0]))
        recipient_if_true_list.append(int(recipient_if_true[0]))
        recipient_if_false_list.append(int(recipient_if_false[0]))

setup(input)
monkey_biz_counter_original = [0] * len(monkeys)

# without using a smaller number for the stress factor, this program would 
# take an absurd time to execute; using the least common multiple makes it
# much faster and ensures it will still correctly reassign items
mod = 1
for i in tests:
    mod *= i


# goes through one round, assigns inventory accordingly, and increments 
# monkey_biz_counter for each item inspection
def one_round(stress_type, inventories, monkey_biz_counter):
    if stress_type == 'high':
        stress_factor = mod
    else:
        stress_factor = 3
    for monkey in monkeys:
        for worry in inventories[monkey]:
            monkey_biz_counter[monkey] += 1
            if operations[monkey][1] == 'old':
                worry = eval(f"{worry}{operations[monkey][0]}{worry}")
            else:
                worry = eval(f"{worry}{operations[monkey][0]}{operations[monkey][1]}")
            if stress_type == 'high':
                worry = worry % stress_factor
            else:
                worry = worry // stress_factor
            if worry % tests[monkey] == 0:
                inventories[recipient_if_true_list[monkey]].append(worry)
            else:
                inventories[recipient_if_false_list[monkey]].append(worry)
        inventories[monkey] = []
    return inventories, monkey_biz_counter


# this calculates monkey business (product of two top inspection counts) for
# a given number of rounds and stress_type
def monkey_biz(rounds, stress_type):
    monkey_biz_counter = monkey_biz_counter_original.copy()
    inventories = copy.deepcopy(inventories_original)
    for round in range(rounds):
        inventories, monkey_biz_counter = one_round(stress_type, inventories, monkey_biz_counter)
    first = max(monkey_biz_counter)
    monkey_biz_counter.remove(first)
    second = max(monkey_biz_counter)
    return first*second

# answer to part 1 (level of monkey business after 20 rounds)
print(monkey_biz(20, 'low'))

# answer to part 2 (level of monkey business after 10000 rounds)
print(monkey_biz(10000, 'high'))