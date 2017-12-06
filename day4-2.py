letters = list('abcdefghijklmnopqrstuvwxyz')
def to_anagram_hash(word):
    hash_vec = np.zeros(len(letters),dtype=int)
    for w in word:
        hash_vec[letters.index(w)] += 1
    return np.array_str(hash_vec)

total_valid = 0
with open('day4-input.txt') as f:
    for line in f.readlines():
        valid_dict = {}
        words = (line[:-1]).split(' ')
        is_valid = True
        for w in words:
            hash_val = to_anagram_hash(w)
            if hash_val in valid_dict.keys():
                is_valid = False
                break
            else:
                valid_dict[hash_val] = 1
        if is_valid:
            total_valid += 1

print('Total valid: {}'.format(total_valid))
