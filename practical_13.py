#13Write a program in python to find a string using re module of regualar expressions
import re
 
s = 'This is python programming'
 
match = re.search(r'python', s)
 
print('Start Index:', match.start())
print('End Index:', match.end())