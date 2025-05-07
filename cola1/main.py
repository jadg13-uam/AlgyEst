from banco import Banco

def mostrar_menu():
    print("\n----- MENÚ DEL BANCO -----")
    print("1. Llegada de cliente")
    print("2. Atender cliente")
    print("3. Mostrar clientes en espera")
    print("4. Salir")

def main():
    banco = Banco()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del cliente: ")
            banco.llega_cliente(nombre)
        elif opcion == "2":
            banco.atender_cliente()
        elif opcion == "3":
            clientes = banco.obtener_clientes_en_espera()
            if clientes:
                print("Clientes en espera:", ", ".join(clientes))
            else:
                print("No hay clientes en espera.")
        elif opcion == "4":
            print("Gracias por usar el sistema del banco.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
