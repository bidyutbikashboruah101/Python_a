# r = read only
# w = write only
# r+ = read and write
# a = append something at the end of the file
sn_file = open('second(file to read).txt', 'r')
# print(sn_file.readable())    # to check if the file is readable
# print(sn_file.readline())  # to read the first line of the file
print(sn_file.read())          # tp read the whole file at once
sn_file.close()