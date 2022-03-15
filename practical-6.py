from datetime import datetime

name=input('What is your name?\n')
age=int(input('How old are you?\n'))
hundred=int((100-age)+datetime.now().year)
print('Hey %s, You are %s year old, you will turn 100 year old in %s, \n' % (name,age,hundred))