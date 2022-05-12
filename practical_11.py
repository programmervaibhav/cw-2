
#read a textfile line by line and displayeach wordseperates bya#
filein = open("mydoc.txt",'r')
line =" "
while line:
     line = filein.readline()
     #print(line)
     for w in line:
          if w == ' ':
               print('#\n',end = '')
          else:
               print(w,end = '')
filein.close()
