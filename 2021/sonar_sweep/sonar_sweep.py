import numpy as np
import pandas as pd

file = open('depths.txt')
depths = file.read()
file.close()

depths = depths.split()
count_larger = -1
last_depth = 0

for depth in depths:
    if int(depth) > last_depth : count_larger += 1
    last_depth = int(depth)

print("part_1 answer: ", str(count_larger))

depths = pd.Series(depths)
windows = depths.rolling(3)
moving_sums = windows.sum()
moving_sums = moving_sums.tolist()[2:]

count_larger_sum = -1
last_sum = 0

for sum in moving_sums:
    if sum > last_sum : count_larger_sum += 1
    last_sum = sum

print("part_2 answer: ", str(count_larger_sum))