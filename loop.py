#sourceFilesNames = ['sfile1','sfile2','sfile3']
#destinationFilesNames = ['dfile1','dfile2','dfile3']
#for x in range(len(sourceFilesNames)):
#    print(sourceFilesNames[x] + " - " + destinationFilesNames[x])

source = [10,22,43,55,65,65,156,48,2544,1]
dest = [42,51,67,76,98,12,45,20,25]
'''
print(source[0] + dest[0])
print(source[0] + dest[1])
print(source[0] + dest[2])

print(source[1] + dest[0])
print(source[1] + dest[1])
print(source[1] + dest[2])

print(source[2] + dest[0])
print(source[2] + dest[1])
print(source[2] + dest[2])

for s_offset in range(len(source)):
    for d_offset in range(len(dest)):
        print(source[s_offset] + dest[d_offset])
'''
'''
for i in range(10):
    if i==0:
        print('*', end='')
    else:
        for j in range(i*2):
            print('*', end='')
    print('\n', end='')
'''
'''
for i in range(10):
    if (i+1) % 2 != 0: # allow only even number
        for j in range(10):
            print('{:2} x {:2} : {:3}'.format(i+1, j+1, ((i+1)*(j+1))))
        userInput = input('next')
        if userInput!='n':
            break
'''
# for s_offset in range(len(source)):
#     # for d_offset in range(len(dest)):
#         print(source[s_offset])

