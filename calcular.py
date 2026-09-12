#Pseudocódigo
#FUNCION calcularTotal(precio, cantidad)
        #total <- precio * cantidad
        #RETORNAR total
    #FIN FUNCION
 
    #precio <- 10
    #cantidad <- 3
    #resultado <- calcularTotal(precio, cantidad)
   # IMPRIMIR resultado

def calcular_total(precio, cantidad):
    
    #Calcula el total a pagar por una compra.
 
    #Parámetros:
     #   precio (float): precio unitario del producto.
      #  cantidad (int): cantidad de unidades compradas.
 
    #Retorna:
        #float: el total de la compra (precio * cantidad).
    
    total = precio * cantidad
    return total
 
 
if __name__ == "__main__":
    print("=== CÁLCULO TOTAL DE COMPRA ")
    precio = 10
    cantidad = 3
 
    resultado = calcular_total(precio, cantidad)

    print(f"Produnto : Camiseta")
    print(f"Precio unitario: ${precio}")
    print(f"Cantidad de producto: {cantidad}")
    print(f"Total a pagar: ${resultado}")
