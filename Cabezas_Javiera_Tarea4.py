import math
menor = float('inf')
cant = int(input('Cantidad de rondas:'))
j = 1
ronda = 1
best = ''
while ronda <= cant :
 print('Ronda', ronda)
 while j <= 3 :
    nomb = input('Nombre:')
    coordx = int(input('Coordenada x:'))
    coordy = int(input('Coordenada y:'))
    if -20<=coordx<=20 and -20<=coordy<=20:
      distancia = math.sqrt((coordx**2)+(coordy**2))
      print(round(distancia, 4))
      if distancia < menor:
        menor = distancia
        best = nomb
    else:
      print('Disparo inválido.', nomb, 'pierde el turno')
    j += 1
 print('Mejor de la ronda:', best, '- Distancia:', round(menor, 4))
 ronda += 1
 j = 1
print('Ganador(a):', best, '- Disparo:', round(menor, 4))