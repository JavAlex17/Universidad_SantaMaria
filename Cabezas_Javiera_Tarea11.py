#NO BORRE ESTE CODIGO
import os
os.system('color')

colores = [('negro','\033[0;37;48m'),
           ('blanco','\033[0;37;47m'),
           ('rojo','\033[0;37;41m'),
           ('verde','\033[0;37;42m'),
           ('amarillo','\033[0;37;43m'),
           ('azul','\033[0;37;44m'),
           ('magenta','\033[0;37;45m'),
           ('celeste','\033[0;37;46m')]

lienzo= [
['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco']
]

nativo='\033[m'
#COMIENCE A PROGRAMAR ABAJO DE ESTA LINEA (NO BORRE EL CODIGO ANTERIOR)

def dibujar_lienzo(lienzo,colores,nativo):
    cont = 0
    wea = ''
    print('  01234567')
    while cont<8:
        for fila in lienzo:
            if cont<8:
                for pix in fila:
                    for color,codigo in colores:
                        if pix == color:
                            b = codigo
                            wea += (b+' '+nativo)
                print(cont,wea)
                cont += 1
                wea = ''
    return ''

def pintar_lienzo(lienzo,fila,columna,color):
    n = 0
    for lista in lienzo:
        if n == fila:
            lista[columna] = color
        n+=1
    lienzo += lista
    return lienzo

def menu_prin(z,lienzo,colores,nativo):
    while z == 2:
        print('1)Crear nuevo dibujo')
        print('2)Salir')
        a = int(input('Seleccione una opción:'))
        if a == 1:
            lienzo = [
              ['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
              ['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
              ['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
              ['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
              ['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
              ['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
              ['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
              ['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco']
              ]
            dibujar_lienzo(lienzo,colores,nativo)
            z = 0
        else:
          a = 2
          z = 0
    return a


def ciclo_infinito(z,lienzo,colores,nativo):
  lienzo = [
  ['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
  ['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
  ['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
  ['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
  ['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
  ['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
  ['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco'],
  ['blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco', 'blanco']
  ]
  while z == 1:
    while z == 1:
      y = int(input('Ingrese fila:'))
      x = int(input('Ingrese columna:'))
      colour = input('Ingrese color:')
      dibujar_lienzo(pintar_lienzo(lienzo,y,x,colour),colores,nativo)
      print('1)Dibujar un punto')
      print('2)Volver al menú principal')
      z = int(input('Seleccione una herramienta:'))
    while z == 2:
      menu_prin(z,lienzo,colores,nativo)
      print('1)Dibujar un punto')
      print('2)Volver al menú principal')
      z = int(input('Seleccione una herramienta:'))
  return ''

    
print('1)Crear nuevo dibujo')
print('2)Salir')
a = int(input('Seleccione una opción:'))
if a == 1:
  dibujar_lienzo(lienzo,colores,nativo)
  print('1)Dibujar un punto')
  print('2)Volver al menú principal')
  z = int(input('Seleccione una herramienta:'))
  while z == 1:
    y = int(input('Ingrese fila:'))
    x = int(input('Ingrese columna:'))
    colour = input('Ingrese color:')
    dibujar_lienzo(pintar_lienzo(lienzo,y,x,colour),colores,nativo)
    print('1)Dibujar un punto')
    print('2)Volver al menú principal')
    z = int(input('Seleccione una herramienta:'))
  while z == 2:
    menu_prin(z,lienzo,colores,nativo)
    if a == 2:
      input()
    else:
      print('1)Dibujar un punto')
      print('2)Volver al menú principal')
      z = int(input('Seleccione una herramienta:'))
      if z == 1:
        ciclo_infinito(z,lienzo,colores,nativo)        
elif a == 2:
  input()
else:
  while a != 1 and a != 2:
    print('¡Opción invalida!')
    print('1)Crear nuevo dibujo')
    print('2)Salir')
    a = int(input('Seleccione una opción:'))
    if a == 1:
      dibujar_lienzo(lienzo,colores,nativo)
      print('1)Dibujar un punto')
      print('2)Volver al menú principal')
      z = int(input('Seleccione una herramienta:'))
      while z == 1:
        y = int(input('Ingrese fila:'))
        x = int(input('Ingrese columna:'))
        colour = input('Ingrese color:')
        dibujar_lienzo(pintar_lienzo(lienzo,y,x,colour),colores,nativo)
        print('1)Dibujar un punto')
        print('2)Volver al menú principal')
        z = int(input('Seleccione una herramienta:'))
      while z == 2:
        menu_prin(z,lienzo,colores,nativo)
        print('1)Dibujar un punto')
        print('2)Volver al menú principal')
        z = int(input('Seleccione una herramienta:'))
        if z == 1:
          ciclo_infinito(z,lienzo,colores,nativo) 
    else:
      input()
