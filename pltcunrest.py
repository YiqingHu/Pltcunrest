#!/usr/bin/python
import math

file = open("MM_1990-2017_1.txt","r")
data = file.readlines()
array = []

for line in data:
    category = line.split("\t")
    array.append(category)
freq = int(array[0][16])
ID = []
govt = 0
pviolent = 0
i = 1
while i < len(array):
    #row = []
    if array[i][10] == "1":
        pviolent = 1
    if array[i][15] != "ignore":
        govt = 1
    if array[i][0] == array[i-1][0] and array[i][14] == array[i-1][14] and array[i][13] == array[i-1][13] and array[i][1] == array[i-1][1]:
        freq += int(array[i][16])
    else:
        #row.append(array[i][0],array[i][14],array[i][13],array[i][1],freq)
        print(array[i-1][0]+"\t"+array[i-1][14]+"\t"+array[i-1][13]+"\t"+array[i-1][1]+"\t"+str(freq)+"\t"+str(pviolent)+"\t"+str(govt))
        freq = int(array[i][16])
        pviolent = 0
        govt = 0
        #ID.append(row)
        print("\n")
    i += 1    


