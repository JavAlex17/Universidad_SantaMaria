n = ord(input('Ingrese una letra mayúscula:'))
from random import randint
x = randint(65,90)
letra = chr(x)

if (n != x):
  if (n < x):
    print ('Está después')
    n = ord(input('Segunda oportunidad:'))
    if (n != x):
      if (n < x):
        print ('Está después')
        n= ord(input('Última oportunidad:'))
        if (n != x):
          print ('Lo siento, era', letra)
          input()
        else:
          print ('Ganaste')
          input()
      else :
        print ('Está antes')
        n= ord(input('Última oportunidad:'))
        if  (n != x) :
          print ('Lo siento, era', letra)
          input()
        else:
          print ('Ganaste')
          input()
    else: 
      print ('Ganaste')
      input()
  else :
    print ('Está antes')
    n = ord(input('Segunda oportunidad:'))
    if (n != x):
      if (n < x):
        print ('Está después')
        n= ord(input('Última oportunidad:'))
        if (n != x):
          print ('Lo siento, era', letra)
          input()
        else:
          print ('Ganaste')
          input()
      elif (n > x):
        print ('Está antes')
        n = ord(input('Última oportunidad:'))
      if (n != x):
        print ('Lo siento, era', letra )
        input()
      else:
        print ('Ganaste')
        input()
    else:
      print ('Ganaste')
      input()
else:
  print ('Ganaste')
  input()




