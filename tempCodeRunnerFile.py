with open(filePath, "r") as sourceFileHandler:
    with open(writeToFilePath, "w") as destFileHandler:
        for line in sourceFileHandler:
            destFileHandler.write('->{}\n'.format(line))