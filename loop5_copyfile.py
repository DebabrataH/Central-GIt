import os
import shutil
from shutil import copyfile

source = ['/Users/dev_catalina/Downloads/MultiBeast 12.3.0 Catalina Edition', '/Users/dev_catalina/Downloads/Clover_v2.5k_r5070',]
destination= ['/Users/dev_catalina/Desktop/1','/Users/dev_catalina/Desktop/2', '/Users/dev_catalina/Desktop/3', '/Users/dev_catalina/Desktop/4']

for x_source in range(len(source)):
    for y_destination in range(len(destination)):
        sourceFolderName = os.path.basename(source[x_source])
        destinationFolderFullPath = os.path.join(destination[y_destination], sourceFolderName)
        shutil.copytree(source[x_source], destinationFolderFullPath)

# NEED TO KNOW 