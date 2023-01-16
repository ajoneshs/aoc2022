input = open("input\day06_input.txt", "r").read()

def packet_marker_index(num_chars, message):
    substring = message[:num_chars]
    if len(substring) == len(set(substring)):
        return message.find(substring) + num_chars
    for char in message[num_chars:]:
        substring = substring[1:] + char
        if char not in substring[:-1] and len(substring) == len(set(substring)):
            return message.find(substring) + num_chars

# answer to part 1 (index of start of message with packet markers of 4 characters)
print('Part 1: ' + str(packet_marker_index(4, input)))

# answer to part 2 (index of start of message with packet markers of 14 characters)
print('Part 2: ' + str(packet_marker_index(14, input)))