# NOMBRE   : JUAN DIEGO TORO MONSALVE
# GRUPO    : 213022_186
# PROGRAMA : INGENERIA ELECTRONICA
# CODIGO FUENTE : AUTORIA PROPIA

inventario = [# MATRIZ
    ["01", "Resistencias 1k", 50, 100],#CODIGO ARTICULO, NOMBRE ARTICULO, STOCK ACTUAL, STOCK MINIMO 
    ["02", "Capacitores 10uF", 120, 50],
    ["03", "Transistores 2N3904", 10, 30],
    ["04", "Diodos LED", 200, 200],
    ["05", "Placas de pruebas", 5, 15]
]
def calcular_pedido(stock_actual, stock_minimo):    
    if stock_actual < stock_minimo:#    Lógica: Si el Stock Actual es menor que el Stock Mínimo, la cantidad a pedir es la diferencia entre ambos.
        cantidad = stock_minimo - stock_actual
        return cantidad    
    else:#si el Stock Actual es igual o mayor que el Stock Mínimo, no se necesita pedir nada, por lo que la cantidad a pedir es 0.
        return 0

# Salida: Imprimir una lista de pedidos que muestre el nombre del artículo y la cantidad exacta.
print("\n")
print("="*150)
print(" "*35 + "----------------- LISTA DE PEDIDOS DE INVENTARIO -----------------")

# Recorremos cada artículo dentro de la matriz inventario
for articulo in inventario:
    
    nombre = articulo[1]#estoy llamando el nombre del articulo que esta en la posicion 1 de cada fila de la matriz inventario
    stock_actual = articulo[2]#estoy llamando el stock actual del articulo que esta en la posicion 2 de cada fila de la matriz inventario
    stock_minimo = articulo[3]#estoy llamando el stock minimo del articulo que esta en la posicion 3 de cada fila de la matriz inventario    
    
    cantidad_a_pedir = calcular_pedido(stock_actual, stock_minimo)#estoy llamando la funcion    
    
    print(" "*35 + f"ARTICULO: {nombre}" + f" | Stock Actual: {stock_actual}" + f" | Stock Mínimo: {stock_minimo}" + f" | Cantidad a solicitar: {cantidad_a_pedir}")
    
