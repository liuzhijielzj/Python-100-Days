from random import randint

face = randint(1, 6) # include end number
if face == 1:
    result = 'sing'
elif face == 2:
    result = 'dance'
elif face == 3:
    result = 'dog'
else:
    result ='kidding'
print(result)