class Coche(object):
	def __init__(self):
		self.__largoChasis=350
		self.__anchoChasis=120
		self.__ruedas=4
		self.__encendido=False
		self.__gasolina=70
		self.__aceite=93
		self.__estadoPuertas="cerradas"

	def arrancar(self,prender):
		self.__encendido=prender
		res = ""
		if self.__encendido:
			chequeo = self.__chequeoInterno()
			if chequeo:
				res = "El coche esta encendido"
			else:
				res ="No es posible encender el coche. Revise gsolina, aceite y puertas."
		else:
			res = "El coche esta apagado"
		return res

	def estado(self):
		print("El coche tiene un largo de ",self.__largoChasis,", un ancho de ",self.__anchoChasis," y ",self.__ruedas," ruedas.")
		print("Nivel de gasolina: ",self.__gasolina,"%")
		print("Nivel de aceite: ",self.__aceite,"%")

	def __chequeoInterno(self):
		res = False
		print("Realizando chequeo interno...")
		if(self.__gasolina>=80 and self.__aceite>=80 and self.__estadoPuertas=="cerradas"):
			res = True
		return res



print("------------------Instanciamos nuestro primer coche------------------------")

miCoche=Coche()
print(miCoche.arrancar(True))
miCoche.estado()

print("------------A continuación instanciamos nuestro segundo coche--------------")

miCoche2=Coche()
print(miCoche2.arrancar(False))
miCoche2.estado()