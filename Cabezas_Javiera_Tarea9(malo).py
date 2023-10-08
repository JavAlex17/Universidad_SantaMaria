emails = {
'2020735010':['h@gmail.com','h@usm.cl'],
'202034234k':['k@usm.cl'],
'2020987992':['lost@usm.cl']
}
respuestas = [('2020735010', 1, '1 2 3'), ('202034234k', 2, '3 1 2'),
('2020735010', 2, '1 2 3'), ('202034234k', 1, '1,3,2')]
soluciones = {1:[('1 2 3',50),('1 3 2',100)],2:[('3 1 2',70),('1 2 3',100)]}
def calificar(emails,respuestas,soluciones):
  n = 0
  i = 0
  x = 0
  c = 0
  a = 0
  nota = 0
  calif = 0
  ema = {}
  email = []
  for rol in emails:
    while n<len(emails[rol]):
      for sol in soluciones:
        if c<len(soluciones[sol]):
          if respuestas[x][2] in soluciones[sol][c]:
            calif = soluciones[sol][c]
            nota += calif[1]//2
            email = respuestas[i][0]
            ema[emails[email][a]] = email,nota
      n += 1
      i += 1
      c += 1
      x += 1 
    c = 0
    n = 0
    x = 0
    i = 0
  return ema

print(calificar(emails,respuestas,soluciones))
