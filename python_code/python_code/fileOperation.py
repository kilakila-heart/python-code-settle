file_object = open('D:\Data\yoochoose-test.dat')
file_object_w = open('D:\Data\yoochoose-test-sample.dat', 'w')
n = 10000
index = 0
for line in file_object:
    file_object_w.write(line)
    if index < n:
        index += 1
    else:
        break
file_object_w.close()

