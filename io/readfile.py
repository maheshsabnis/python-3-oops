# Open the file and the read all lines from it

with open('./../files/file.txt','r') as f:
    lines = f.readlines()
    f.close()
    
    
for l in lines:
    print(l)
        
    


# with open('./../files/file.txt', 'r') as f:
#     lines3 = f.readline()
#     f.close()
# print(f'Three Lines {lines3}')
