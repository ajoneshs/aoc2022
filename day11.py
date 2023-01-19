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
        test = re.findall('\d+', split_block[3])
        recipient_if_true = re.findall('\d+', split_block[4])
        recipient_if_false = re.findall('\d+', split_block[5])

        # just a placeholder til I figure out how I want to organize things
        monkeys.append(monkey)
        inventories.append(inventory)
        operations.append(operation)
        tests.append(test)
        recipient_if_true_list.append(recipient_if_true)
        recipient_if_false_list.append(recipient_if_false)


setup(input)

print(monkeys)
print(inventories)
print(operations)
print(tests)
print(recipient_if_true_list)
print(recipient_if_false_list)