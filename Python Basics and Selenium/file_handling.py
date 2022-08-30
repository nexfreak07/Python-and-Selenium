file = open("read.txt")

# Read all the contents of the file
print(file.read())

# Read the first line of file
print(file.readline())
# Second time the file pointer will go to next line
print(file.readline())
# Read and Readline are connected. If read() has read up to certain characters, readline will continue from the next

# To read line by line we need torun a for loop
# line() will take characters and lines will take whole token of string
for line in file.readlines():
    print(line)
#
file.close()

# Writing into files
# use with open so that you don't close files always
with open("read.txt", "r") as reader:
        content = reader.readlines() # readlines() everything and stores in a list and readlineO() will store character by character
        reversed(content)
        with open('read.txt', 'w') as writer:
            for lines1 in reversed(content):
                writer.write(lines1)


