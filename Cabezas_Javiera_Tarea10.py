#producto=[[Id_modelo, marca, pulgadas, GB de RAM, DD o SSD, GB de DD o SSD, procesador, tarjeta de video], ...]
productos=[
['8475HD','HP',15.6,'8GB','DD','1T','Intel Core i5','Nvidia GTX1050'],
['2175HD','lenovo',14,'4GB','SSD','512GB','Intel Core i5','Nvidia GTX1050'],
['JjfFHD','Asus',14,'16GB','SSD','256GB','Intel Core i7','Nvidia RTX2080Ti'],
['fgdxFHD','HP',15.6,'8GB','DD','1T','Intel Core i3','integrada'],
['GF75HD','Asus',15.6,'8GB','DD','1T','Intel Core i7','Nvidia GTX1050'],
['123FHD','lenovo',14,'6GB','DD','1T','AMD Ryzen 5','integrada'],
['342FHD','lenovo',15.6,'8GB','DD','1T','AMD Ryzen 7','Nvidia GTX1050'],
['UWU131HD','Dell',15.6,'8GB','DD','1T','AMD Ryzen 3','Nvidia GTX1050']]

#stock=[ [ Id_modelo, precio, stock], ...]
stock=[
['8475HD',387990,10],['2175HD',327990,4],['JjfFHD',424990,1],
['fgdxFHD',664990,21],['123FHD',290890,32],['342FHD',444990,7],
['GF75HD',749990,2],['UWU131HD',349990,1],['FS1230HD',249990,0]]

#a)
def stock_marca(marca, lista_productos, lista_stock):
	modelo = []
	marc = marca.lower()
	suma = 0
	i = 0
	for mod in lista_productos:
		if marc in mod[1].lower():
			modelo.append(mod[0])
	for fila in lista_stock:
		for mode in fila:
			if mode in modelo:
				suma += fila[2]
	return suma


#b)
def filtrar_equipos(caracteristicas, lista_productos, lista_stock):
	modelos = []
	for mod in lista_productos:
		if caracteristicas[0] in mod:
			mod.remove(caracteristicas[0])
			mod.insert(0,mod[1])
			del mod[2]
			modelos.append(mod)
			modelos.sort()
	for mod2 in modelos:
		if caracteristicas[1] not in mod2:
			modelos.remove(mod2)
	for mod3 in modelos:
		if caracteristicas[2] not in mod3:
			modelos.remove(mod3)
	for mod4 in modelos:
		if caracteristicas[1] in mod4:
			mod4.remove(caracteristicas[1])
		else:
			return []
		if caracteristicas[2] in mod4:
			mod4.remove(caracteristicas[2])
		else:
			return []
	for fila in lista_stock:
		for mod in modelos:
			if mod[1] in fila:
				mod.extend(fila[1:])
	return modelos	

# Prueba de las funciones
print('Probando funcion stock_marca (parte a)...')
print(stock_marca('hp', productos, stock))
print(stock_marca('LENOVO', productos, stock))
print(stock_marca('Huawei', productos, stock))

print('Probando funcion filtrar_equipos (parte b)...')
print(filtrar_equipos([15.6, '8GB', '1T'],productos,stock))
print(filtrar_equipos([14, '16GB', '256GB'],productos,stock))
print(filtrar_equipos([15.6, '16GB', '512GB'],productos,stock))

input()
