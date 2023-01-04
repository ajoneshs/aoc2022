import re

#input = open("input\day11_input.txt", "r").read().splitlines()
input = open("input\day11_sample_input.txt", "r").read().split('\n\n')


'''
for block in input:
    for line in block.splitlines():
        a
'''
namelist = []
inventorylist = []
operationlist = []
testlist = []
recipient_if_true_list = []
recipient_if_false_list = []

def setup(input):
    for block in input:
        split_block = block.splitlines()
        print(split_block[0])
        name = re.findall('\d+', split_block[0])
        inventory = re.findall('\d+', split_block[1])
        operation = re.findall('(\*|\+) (\d+|old)', split_block[2])
        test = re.findall('\d+', split_block[3])
        recipient_if_true = re.findall('\d+', split_block[4])
        recipient_if_false = re.findall('\d+', split_block[5])

        # just a placeholder til I figure out how I want to organize things
        namelist.append(name)
        inventorylist.append(inventory)
        operationlist.append(operation)
        testlist.append(test)
        recipient_if_true_list.append(recipient_if_true)
        recipient_if_false_list.append(recipient_if_false)


setup(input)

print(namelist)
print(inventorylist)
print(operationlist)
print(testlist)
print(recipient_if_true_list)
print(recipient_if_false_list)