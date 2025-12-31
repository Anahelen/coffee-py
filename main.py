from menu import mostrar_menu
from pedidos import pedir_cafe
from historial import ver_historial


def main():
    while True:
        mostrar_menu()
        opcion  = input("Selecciona una opción: ")
        
        if opcion == "1":
            pedir_cafe()
            pass
        elif opcion == "2":
            ver_historial()
            pass
        elif opcion == "3":
            print("\n Muchas gracias por haber tomado nuestros cafés")
            break
        else:
            print("Opción invalida, por favor elegir una de las opciones sugeridas ")
            
if __name__ == "__main__":
    main()
        