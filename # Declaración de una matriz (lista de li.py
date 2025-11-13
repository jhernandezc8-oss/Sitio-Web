# Declaración de una matriz (lista de listas) de 5 filas y 6 columnas
# Inicializamos con algunos valores para ejemplo
matriz1 = [
    [1, 2, 3, 4, 5, 6],      # Fila 0
    [7, 8, 9, 10, 11, 12],    # Fila 1
    [13, 14, 15, 16, 17, 18], # Fila 2
    [19, 20, 21, 22, 23, 24], # Fila 3
    [25, 26, 27, 28, 29, 30]  # Fila 4
]

# Mostrar la matriz original
print("Matriz original (5x6):")
for fila in matriz1:
    print(fila)

# Acceder al elemento en la fila 2, columna 4 (índices 0-based)
X = matriz1[2][4]  # Valor esperado: 17
print(f"\nElemento en fila 2, columna 4: {X}")

# Modificar el elemento en la fila 2, columna 4
matriz1[2][4] = 99

# Mostrar la matriz modificada
print("\nMatriz modificada:")
for fila in matriz1:
    print(fila)
