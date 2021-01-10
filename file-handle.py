# File permission
# to whom Group or User
# Read, Create / Write / Append, Delete and Execute
# x = Create
# r = Read
# w = Write
# a = Apend

filePath = './target/dev.txt'
writeToFilePath = './target/dest.dev.txt'

# Read a file
# fileHandler = open(filePath, "r")
# print(fileHandler.read())
# fileHandler.close()

# Close file autometically
# with open(filePath, "w") as fileHandler:
#     print(fileHandler.read())
    

# Read line
# with open(filePath, "r") as fileHandler:
#     for line in fileHandler:
#         print(line)

# Write to file
with open(filePath, "w") as fileHandler:
    fileHandler.write('Sample Text')

# Read line and write to destination
with open(filePath, "r") as sourceFileHandler:
    with open(writeToFilePath, "w") as destFileHandler:
        for line in sourceFileHandler:
            destFileHandler.write('->{}\n'.format(line))