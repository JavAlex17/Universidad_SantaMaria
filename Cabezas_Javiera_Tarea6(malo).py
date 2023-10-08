'''
Incluya sus funciones a continuación
'''
def horas_ingresos(ingresos, nombre, fecha):
  horas = ''
  a = 0
  while a <= len(nombre)-1 :
    if nombre == ingresos[a : a + len(nombre)]:
      if fecha == ingresos[len(nombre) + 1 + a : len(nombre) + 11 + a]: 
        horas += ingresos[len(nombre) + 12 + a : len(nombre) + 17 + a] + ''
    a += 1
  return('Ingresos de '+ nombre + ' en ' + fecha + ' : ' + horas)

def ingresos_en_dia(ingresos, dia):
  x = 0
  y = 0
  nombres = ''
  while x <= len(ingresos)-1:
    if dia == ingresos[x:10+x]:
      while y < len(ingresos):
#Ya no sé cómo seguir :(
        y += 1
    x += 1
  return(nombres)

'''
No modifique nada de aquí en adelante
'''

'''
Ejemplos con string del enunciado. Salida esperada (incluida la línea en blanco):
Ingresos de Juan Gallardo en 2020-04-01: 08:30 10:15
Ingresos de Ana Carmona en 2020-04-05: Sin ingresos

Juan Gallardo;Ana Carmona;
'''
ingresos = 'Juan Gallardo,2020-04-01,08:30;Ana Carmona,2020-04-01,08:35;Juan Gallardo,2020-04-01,10:15'
print(horas_ingresos(ingresos, 'Juan Gallardo', '2020-04-01'))
print(horas_ingresos(ingresos, 'Ana Carmona', '2020-04-05'))
print(ingresos_en_dia(ingresos,'2020-04-05'))
print(ingresos_en_dia(ingresos,'2020-04-01'))

'''
Pruebas adicionales. Salida esperada (incluida la línea en blanco):
Ingresos de Ada Lovelace en 2020-05-11: 11:30 15:30
Ingresos de Leonhard Euler en 2020-05-05: Sin ingresos
Ingresos de Alan Turing en 2020-05-10: 09:30
Ada Lovelace;Pythonio Algoritmio;Guido van Rossum;

Ada Lovelace;
'''
ingresos = 'Perico de los Palotes,2020-05-10,08:30;Ada Lovelace,2020-05-11,11:30;Pythonio Algoritmio,2020-05-11,08:35;Alan Turing,2020-05-10,09:30;Covidio Pandemio,2020-05-08,10:15;Ada Lovelace,2020-05-12,08:30;Guido van Rossum,2020-05-10,15:30;Leonhard Euler,2020-05-10,08:45;Ada Lovelace,2020-05-11,15:30;Pythonio Algoritmio,2020-05-02,17:35;Guido van Rossum,2020-05-11,20:30'
print(horas_ingresos(ingresos, 'Ada Lovelace', '2020-05-11'))
print(horas_ingresos(ingresos, 'Leonhard Euler', '2020-05-05'))
print(horas_ingresos(ingresos, 'Alan Turing', '2020-05-10'))
print(ingresos_en_dia(ingresos,'2020-05-11'))
print(ingresos_en_dia(ingresos,'2020-05-15'))
print(ingresos_en_dia(ingresos,'2020-05-12'))
