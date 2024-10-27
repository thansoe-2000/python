# r = read
# a = append
# w = write
# x = create
import os
file = open("names.txt")


# print(file.read())
# print(file.read(3))

# print(file.readline())
# print(file.readline())

# for line in file:
#     print(line)

# file.close()

# try:
#     file=open('names.txt')
#     print(file.read())
# except:
#     print("The file doesn't exist")

file = open("names.txt", 'a')
file.write("Phyu Hla\n")
file.close()

file=open('names.txt')
print(file.read())
file.close()

file = open('name_list', 'w')
file.close()


# create a file
if not os.path.exists('thansoe.txt'):
    file = open('thansoe.txt', 'x')
    file.close()
    
# delete a file
# avoid an error if it doesn't exist
if os.path.exists('thansoe.txt'):
    os.remove('thansoe.txt')
else:
    print('the file you wish to delete does not exist')

