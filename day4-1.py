total_valid = 0
with open('day4-input.txt') as f:
    for line in f.readlines():
        valid_dict = {}
        words = (line[:-1]).split(' ')
        is_valid = True
        for w in words:
            if w in valid_dict.keys():
                is_valid = False
                break
            else:
                valid_dict[w] = 1
        if is_valid:
            total_valid += 1
print("Total valid: {}".format(total_valid))