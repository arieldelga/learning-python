def devuelveCiudades(*ciudades):
	for elemento in ciudades:
		yield from elemento

lisCiudades = devuelveCiudades("Cochabamba", "Oruro", "La Paz")

for i in "tre":
	print(next(lisCiudades))