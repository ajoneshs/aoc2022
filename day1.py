input = open("input\day1_input.txt", "r").read()

# a list of the total calories each elf carries
calorie_inventory = [sum([int(j) for j in i.split('\n')]) for i in input.split("\n\n")] 

# answer to part 1 (calories carried by elf who carries most calories)
print(max(calorie_inventory))

# answer to part 2 (inventories of top 3 elves)
calorie_inventory.sort(reverse = True)
print(sum(calorie_inventory[0:3]))