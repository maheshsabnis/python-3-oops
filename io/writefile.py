# Writing the file

lines = ['I am Line 1',
         'I am Line 2',
         'I am Line 3',
         'I am Line 4',
         'I am Line 5',
         'I am Line 6',
         'I am Line 7',
         'I am Line 8'
        ]
with open('./../files/newfile.txt',  'w') as f:
    for l in lines:
        f.write(l+'\n')