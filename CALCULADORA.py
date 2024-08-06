#inicio de ciclo while
while True:
    print("Selecciona una opcion: ") #iniciar
    print("1. Suma") #sumar
    print("2. Resta") #restar
    print("3. Multiplicar") #multiplicar
    print("4. Dividir") #dividir
    print("5. Raíz") #raíz
    print("6. Fin") #fin


    opcion = input("ingrese el número de la opción deseada: ") #ingresa el numero
 
    if opcion == "1" : # if es para sumar 
        print("suma")
        num1 = float(input("Ingrese el primer número: ")) # el primer numero
        num2 = float(input("Ingrese el segumdo número: ")) #el segundo numero
        resultado = num1 + num2 # hacer la suma
        print(resultado)
    elif opcion == "2"  : # if es para restar
        print("resta")
        num1 = float(input("ingrese el primer número: ")) # primer numero
        num2 = float(input("ingrese el segumdo número: ")) #segundo numero
        resultado = num1 - num2 # realizar la resta 
        print(resultado)
    elif opcion == "3"  : # if es para multiplicar
        print("multiplicar")
        num1 = float(input("ingrese el primer número: ")) #primer numero
        num2 = float(input("ingrese el segumdo número: ")) #segundo numero
        resultado = num1 * num2 # hacer la multiplicacion
        print(resultado)
    elif opcion == "4"  : # if es para dividir
        print("dividir.")
        num1 = float(input("ingrese el primer número: ")) #primer numero
        num2 = float(input("ingrese el segumdo número: ")) #segundo numero
        resultado = num1 / num2 # realizar la division
        print(resultado)
    elif opcion == "5"  : # if es para raiz
        print("raíz")
        num1 = float(input("ingrese el primer número a sacar raíz: ")) #primer numero
        num2 = float(input("ingrese el segumdo número: ")) # segundo numero el tipo de raiz
        resultado = pow(num1, 1/num2) # realizar la raiz
        print(resultado)
    elif opcion == "6"  : # if para final
        break # fin
    else:
        print("opción no Valida.") # mensaje de error al no haber opción