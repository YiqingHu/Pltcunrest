#!/usr/bin/python
import math

file = open("MM_1990-2017.txt","r")
data = file.readlines()
array = []

for line in data:
    category = line.split(",")
    array.append(category)

ID = []
freq = 1
i = 1
while i < len(array):
    #row = []
    if array[i][0] == array[i-1][0] and array[i][14] == array[i-1][14] and array[i][13] == array[i-1][13] and array[i][1] == array[i-1][1]:
        freq += 1
    else:
        #row.append(array[i][0],array[i][14],array[i][13],array[i][1],freq)
        print(array[i-1][0]+","+array[i-1][14]+","+array[i-1][13]+","+array[i-1][1]+","+str(freq))
        freq = 1
        #ID.append(row)
        print("\n")
    i += 1    


