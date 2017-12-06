instr = []
with open('day5-input.txt') as f:
    for line in f.readlines():
        instr.append(int(line))

steps = 0
idx = 0
while idx < len(instr):
    step = instr[idx]
    instr[idx] += 1
    idx = idx + step
    steps += 1

print('Steps: {}'.format(steps))