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

# Set Arg

Target = sys.argv[1]
copySample = sys.argv[2]=='True'
sourceFolderPath = sys.argv[3]
destinationFolderPath = sys.argv[4]

# declear variable

sourceFolderPath = '/Users/dev_catalina/Downloads/MultiBeast 12.3.0 Catalina Edition'
destinationFolderPath = '/Users/dev_catalina/Desktop/1'

if copySample: 
    sourceFolderPath