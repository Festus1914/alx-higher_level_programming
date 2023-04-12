#!/usr/bin/python3
''' 
Function that inserts a line of text to a file, after each line containing a specific string
'''


idef append_after(filename="", search_string="", new_string=""):
    ''' Function search and update.
    '''
    with open(filename, 'r+') as f:
        lines = f.readlines()
        i = 0
        for line in lines:
            if line.find(search_string) is not -1:
                lines.insert(i + 1, new_sting)
            i += 1
        f.seek(0)
        f.write("".join(lines))
