"""Ejericio 1 - Python - Numero Positvo - If...Else...Elif"""
numero = int(input("Ingrese numero: "))

if numero > 0:
    print("El numero",numero,"es positivo")
elif numero == 0:
    print("El numero", numero, "es cero")
else:
    print("El numero", numero,"es negativo")