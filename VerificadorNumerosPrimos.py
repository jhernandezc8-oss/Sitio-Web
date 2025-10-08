#-----------------------------Grupo 4------------------------------
# ------- PROGRAMA QUE VERIFICA SI UN NUMERO ES PRIMO O NO --------


#Función que retorna True si n es primo, False si no lo es
def es_primo(n):
    if n <= 1:
        return False
    #bucle que prueba divisores desde el 2 hasta el n-1
    for i in range(2, n):
        if n % i == 0:
            return False
    #si no se encontraron divisores entonces es primo
    return True

#Funcion pricipal, maneja la interaccion con el usuario y la salida del programa
def main():
    print(">>>>>>>>>> Verificador de número primo <<<<<<<<<<")
    #Convierte el input en entero y si hay un error lo notifica y sale de main()
    try:
        num = int(input("-Ingrese un número entero: "))
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")
        return

    #usa la funcion es_primo para determinar si es primo o no, y emite el mensaje de salida al usuario
    if es_primo(num):
        print(f"El número {num} ES primo.")
    else:
        print(f"El número {num} NO es primo.")

main()
