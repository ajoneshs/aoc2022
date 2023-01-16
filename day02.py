input = open("input\day02_input.txt", "r").read()

score = {'A X': 1 + 3, 'A Y': 2 + 6, 'A Z': 3 + 0,
         'B X': 1 + 0, 'B Y': 2 + 3, 'B Z': 3 + 6,
	     'C X': 1 + 6, 'C Y': 2 + 0, 'C Z': 3 + 3}

# list of the outcomes for each game
outcomes = [score[i] for i in input.split("\n")]

# answer to part 1 (total points from using this strategy guide)
print(sum(outcomes))

key = {'A X': 3, 'A Y': 4, 'A Z': 8,
       'B X': 1, 'B Y': 5, 'B Z': 9,
	   'C X': 2, 'C Y': 6, 'C Z': 7}

outcomes2 = [key[i] for i in input.split("\n")]

# answer to part 2 (total points from using alternate strategy guide)
print(sum(outcomes2))