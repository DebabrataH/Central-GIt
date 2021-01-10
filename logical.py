import shutil

"""
Target type
----------------
1. development
2. staging
3. production
----------------
"""
# Declare variables
target = 'staging'
copySample = False
sourceFolderPath = './sample'
destinationFolderPath = './target'
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