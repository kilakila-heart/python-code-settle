import string

file_object = open('D:\Data\yoochoose-buys.dat')
file_object_w = open('D:\Data\yoochoose-buys-small.dat', 'w')
n = 100
s = []
for line in file_object:
    index = string.atoi(line.split(",")[0])
    if index <= n:
        s.append(line)
s.sort()
for line in s:
    file_object_w.write(line)
    
file_object_w.close()

