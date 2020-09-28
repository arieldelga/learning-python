def generarPares(lim):
	num = 1
	while num<lim:
		yield num*2
		num = num+1

pares = generarPares(10)

print(next(pares))
print("Aca puede ir mas código...")

print(next(pares))
print("Aca puede ir mas código...")

print(next(pares))
print("Aca puede ir mas código...")