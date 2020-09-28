cargo0 = input("Introduzca su cargo: ")
salario0 = int(input("Introduzca su salario: "))
cargo1 = input("Introduzca su cargo: ")
salario1 = int(input("Introduzca su salario: "))
cargo2 = input("Introduzca su cargo: ")
salario2 = int(input("Introduzca su salario: "))
cargo3 = input("Introduzca su cargo: ")
salario3 = int(input("Introduzca su salario: "))
print()
print("Salario " + cargo0 + " = " + str(salario0))
print("Salario " + cargo1 + " = " + str(salario1))
print("Salario " + cargo2 + " = " + str(salario2))
print("Salario " + cargo3 + " = " + str(salario3))

if salario0 > salario1 > salario2 > salario3:
	print("Todo en orden.")
else:
	print("Algo anda mal en la empresa.")