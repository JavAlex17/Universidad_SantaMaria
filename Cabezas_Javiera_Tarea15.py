x  = ''
while x != 'SALIR':
    x = input('Ingrese una asignatura:')
    if x == 'FIS100':
        archivofis = open('FIS100.txt','r')
        for linea in archivofis:
            rol = linea.strip()[0:12].replace(':','')
            notas = linea[-len(linea)+12:-1].replace(':','')
            total = 0
            for i in notas.split(','):
                i = int(i)
                total += i
            prom = total//len(notas.split(','))
            if prom >= 55:
                condicion = 'A'
            elif prom < 55:
                condicion = 'R'
            r = open(rol+'.txt','w')
            r.write(x+' '+str(prom)+' '+condicion)
            r.close()
            
    elif x in 'INF391':
        archivoinf = open('INF391.txt','r')
        for linea in archivoinf:
            rol = linea.strip()[0:12].replace(':','')
            notas = linea[-len(linea)+12:-1].replace(':','')
            total = 0
            notas = notas.replace('','')
            for i in notas.split(','):
                i = int(i)
                total += i
            prom = total//len(notas.split(','))
            if prom >= 55:
                condicion = 'A'
            elif prom < 55:
                condicion = 'R'
            r = open(rol+'.txt','w')
            r.write(x+' '+str(prom)+' '+condicion)
            r.close()
            
    elif x in 'IWI131':
        archivoiwi = open('IWI131.txt','r')
        for linea in archivoiwi:
            rol = linea.strip()[0:12].replace(':','')
            notas = linea[-len(linea)+12:-1].replace(':','')
            total = 0
            for i in notas.split(','):
                i = int(i)
                total += i
            prom = total//len(notas.split(','))
            if prom >= 55:
                condicion = 'A'
            elif prom < 55:
                condicion = 'R'
            r = open(rol+'.txt','w')
            r.write(x+' '+str(prom)+' '+condicion)
            r.close()
            
    elif x in 'MAT021':
        archivomat = open('MAT021.txt','r')
        for linea in archivomat:
            rol = linea.strip()[0:12].replace(':','')
            notas = linea[-len(linea)+12:-1].replace(':','')
            total = 0
            for i in notas.split(','):
                i = int(i)
                total += i
            prom = total//len(notas.split(','))
            if prom >= 55:
                condicion = 'A'
            elif prom < 55:
                condicion = 'R'
            r = open(rol+'.txt','w')
            r.write(x+' '+str(prom)+' '+condicion)
            r.close()
            
