import os
import shutil
import fileinput

# Declare variable
sourceFolderPath = '/Users/dev_catalina/Desktop/PythonPractice/sample'
destinationFolderPath = '/Users/dev_catalina/Desktop/PythonPractice/target'
sourceFilePathInDestination = destinationFolderPath + '/app.sample.config'
targetFilePath = destinationFolderPath + '/app.config'
sourceConnectionStringParam = '{CONNECTION_STRING}'
connectionString = 'host=localhost port=5432 dbname=taop user=taop'

# Try to delete target folder if exists
shutil.rmtree(destinationFolderPath, ignore_errors=True)

# Copy folder
#shutil.copytree(sourceFolderPath, destinationFolderPath)

# Rename file
os.rename(sourceFilePathInDestination,targetFilePath)

# Replace text
with fileinput.FileInput(targetFilePath, inplace=True) as file:
    for line in file:
        print(line.replace(sourceConnectionStringParam, connectionString), end='')