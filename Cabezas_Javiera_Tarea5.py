#II-A
from random import randint
def es_cara():
  x = randint(1,2) 
  if x == 1:
    return True
  else:
    return False 
#II-B
def lanzamiento(n):
  contador = 0
  cara = 0
  while contador < n :
    if es_cara() == True:
      cara += 1
    contador += 1     
  return(cara)
#II-C
def maquina(n):
  ronda = 0
  while n > 0:
    n -= lanzamiento(n)
    ronda += 1
  return(ronda)
#II-D
def intentos(n,pruebas):
  prom = 0
  veces = 0
  while veces < pruebas:
    prom += maquina(n)
    veces += 1
  prom_f = round(prom/pruebas, 3)
  return(prom_f)

pruebas = 100
n = 1000

print('Monedas: 1000')
print('Pruebas: 100')
print('Cara:', es_cara())
print('Lanzamientos:', lanzamiento(n))
print('Rondas:', maquina(n))
print('Promedio de rondas:', intentos(n,pruebas))

#El promedio de intentos para 100 pruebas, en 10 monedas es 4.78, en 100 monedas son 8.13, en 1000 monedas son 11.31 y en 10000 monedas son 14.31