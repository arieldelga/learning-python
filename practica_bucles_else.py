correo = input("introduce tu correo: ")
for i in correo:
	if i== "@":
		arroba = True
		break;
else:
	arroba = False
print(arroba)		
