
print("Solicitud de becas 2020.")

distanciaDomCol = int(input("Introduzca la dstancia de su domicilio al colegio en km: "))
cantHermanos = int(input("Introduzca el número de hermanos en la escuela: "))
salarioFamiliar = int(input("Introduzca el salario familiar anual bruto: "))

if distanciaDomCol>40 and cantHermanos>=2 or salarioFamiliar<=20000:
 	print("Tiene derecho a beca.")
else:
	print("No tiene dereho a beca.")