ARCHIVO_PEDIDOS = "pedidos.txt"

def pedir_cafe():
    print("\n Elige el cafe que prefieres: ")
    print("1. Espresso")    
    print("2. Capuccino")    
    print("3. Latte")    
    print("4. Americano")    
    print("5. Chocolate")
    
    opcion = input("Opción: ")
    
    cafes = {
        "1": "Espresso",
        "2": "Capuccino",
        "3": "Latte",
        "4": "Americano",
        "5": "Chocolate"
    }
    
    if opcion in cafes: 
        cafe_elegido = cafes[opcion]
        print("Has pedido un " + cafe_elegido + ".¡Preparando tu café!")
        
        with open(ARCHIVO_PEDIDOS, "a", encoding="utf-8") as archivo:
            archivo.write(cafe_elegido + "\n")
    else:
        print("Opción no es válida, Por favor intenta de nuevo")