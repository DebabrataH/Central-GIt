#sourceFilesNames = ['sfile1','sfile2','sfile3']
#destinationFilesNames = ['dfile1','dfile2','dfile3']
#for x in range(len(sourceFilesNames)):
#    print(sourceFilesNames[x] + " - " + destinationFilesNames[x])

source = [2, 3, 4]
dest = [2, 3, 4]
dest2 = [3, 4, 6]
for s_offset in range(len(source)):
    for d_offset in range(len(dest)):
        for dest2_a in range(len(dest2)):
            print(source[s_offset] + dest[d_offset]+ dest2[dest2_a])
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

