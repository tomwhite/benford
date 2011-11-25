#!/usr/bin/python

import os,sys,re

# finds all files below path and accumulates in found
def find(path, found):
  if os.path.isfile(path):
    found.append(path)
  else:
    for sub in os.listdir(path):
      find(os.path.join(path, sub), found)

# filters according to file extension
def filterFile(filename):
  return re.compile('.*\\.(jpeg|jpg)').match(filename)
  
# print sizes of filtered files
found = []
find(sys.argv[1], found)
found = filter(filterFile, found)

for file in found:
  print os.path.getsize(file)
  
