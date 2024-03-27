"""Module for demo of files."""

import os
cwd = os.getcwd()

# handle = open(filename,mode)
file_handle = open(os.path.join(cwd,'chapter-07','files.py'),'r')

for line in file_handle:
    if line.startswith('#'):
        print(line.rstrip())
