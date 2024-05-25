import random
print("Con este programa podras generar una contraseña aleatoria.")
print("")
print("Ingresa un numero para poder generar una contraseña aleatoria utilizando X cantidad de digitos.")
contra="" #Utilizando esta linea podremos almacenar datos.
Opciones="/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890" #Aqui estan todas las opciones.
Contraseña=int(input("ingrese un numero:"))
for i in range(Contraseña): #en vez de i se pueden poner cualquier letra, pero normalmente se usa la letra i
    # en este codigo nos dice que for i se va a repetir la cantidad de veces que pongamos en contraseña
    # i ira contando para que coloque la cantidad correcta de caracteres.
    contra+=random.choice(Opciones) #aqui nos dice que va a generar caracteres del grupo de opciones y los va a agregar al grupo de contra.
print(contra) #por ultimo, ya almacenado los nuevos caracteres generados, el programa va a imprimir el resultado.