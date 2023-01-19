import re

#input = open("input\day11_input.txt", "r").read().splitlines()
input = open("input\day11_sample_input.txt", "r").read().split('\n\n')


monkeys = []
inventories = []
operations = []
tests = []
recipient_if_true_list = []
recipient_if_false_list = []

def setup(input):
    for block in input:
        split_block = block.splitlines()
        print(split_block[0])
        monkey = re.findall('\d+', split_block[0])
        inventory = re.findall('\d+', split_block[1])
        operation = re.findall('(\*|\+) (\d+|old)', split_block[2])
        print(f"operation is {operation}")
        print(f"operation[0][0] is {operation[0]}")
        test = re.findall('\d+', split_block[3])
        recipient_if_true = re.findall('\d+', split_block[4])
        recipient_if_false = re.findall('\d+', split_block[5])

        # just a placeholder til I figure out how I want to organize things
        monkeys.append(int(monkey[0]))
        inventories.append(inventory)
        operations.append(operation[0])
        tests.append(int(test[0]))
        recipient_if_true_list.append(int(recipient_if_true[0]))
        recipient_if_false_list.append(int(recipient_if_false[0]))


setup(input)

print(monkeys)
print(inventories)
print(operations)
print(tests)
print(recipient_if_true_list)
print(recipient_if_false_list)

def one_round():
    for monkey in monkeys:
        for counter, old in enumerate(inventories[monkey]):
            if operations[monkey][1] == 'old':
                new = eval(f"{old}{operations[monkey][0]}{old}")
            else:
                new = eval(f"{old}{operations[monkey][0]}{operations[monkey][1]}")
            print(new)
        # change inventory here
one_round()

'''
for round in range(20):

# go through 1 round, 20 times
for round in range(20):
    one_round()

'''