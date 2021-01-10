import os
import sys
import shutil

'''
Target type
----------------
1. development
2. staging
3. production
----------------
Sample comments
----------------
1. python3 cmd-argument.py staging False
2. python3 cmd-argument.py staging True
3. python3 cmd-argument.py development False
----------------
'''
# program
# python3 ./cmd-argument.py development True ./sample ./target
# python3 ./cmd-argument.py development False ./sample ./target

# Set arguments
target = sys.argv[1]
copySample = sys.argv[2]=='True'
sourceFolderPath = sys.argv[3]
destinationFolderPath = sys.argv[4]

# Declare variables
targetFilePath = destinationFolderPath + '/app.config'

# Set file path
if copySample:
    sourceFilePathInDestination = sourceFolderPath + '/app.sample.config'
else:
    if target == 'development':
        sourceFilePathInDestination = sourceFolderPath + '/app.development.config'
    elif target == 'staging':
        sourceFilePathInDestination = sourceFolderPath + '/app.staging.config'
    elif target == 'production':
        sourceFilePathInDestination = sourceFolderPath + '/app.production.config'
    else:
        print('Not sure')

if os.path.exists(sourceFilePathInDestination):
    # Copy files
    shutil.copyfile(sourceFilePathInDestination, targetFilePath)
    print('Success')
else:
    print('It\'s not a file ' + sourceFilePathInDestination)