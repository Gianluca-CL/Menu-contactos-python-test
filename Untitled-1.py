
contactos = {}


def validar_correo(correo):
    return "@" in correo and "." in correo and correo.index("@") < correo.rindex(".")

def mostrar_menu():
    print("\n=== MENU SISTEMA DE GESTIÓN DE CONTACTOS ===")
    print("1. Crear Contacto")
    print("2. Modificar Contacto")
    print("3. Eliminar Contacto")
    print("4. Listar Contactos")
    print("5. Buscar Contactos")
    print("6. Salir")

def crear_contacto():
    nombre = input("Nombre (máx 50 caracteres): ")[:50]
    telefono = input("Teléfono (11 dígitos internacionales): ")
    direccion = input("Dirección (máx 60 caracteres): ")[:60]
    correo = input("Correo electrónico: ")[:50]

    if not validar_correo(correo):
        print("Correo electrónico no válido.")
        return

    if len(telefono) != 11 or not telefono.isdigit():
        print("Teléfono inválido. Debe contener 11 dígitos.")
        return

    contactos[nombre] = {
        "teléfono": telefono,
        "dirección": direccion,
        "correo": correo
    }
    print(f"Contacto '{nombre}' creado con éxito.")

def modificar_contacto():
    nombre = input("Ingrese el nombre del contacto a modificar: ")
    if nombre in contactos:
        print("Deje en blanco para mantener el dato actual.")
        nuevo_telefono = input(f"Teléfono [{contactos[nombre]['teléfono']}]: ") or contactos[nombre]['teléfono']
        nueva_direccion = input(f"Dirección [{contactos[nombre]['dirección']}]: ") or contactos[nombre]['dirección']
        nuevo_correo = input(f"Correo [{contactos[nombre]['correo']}]: ") or contactos[nombre]['correo']

        if not validar_correo(nuevo_correo):
            print("Correo electrónico no válido.")
            return

        contactos[nombre] = {
            "teléfono": nuevo_telefono,
            "dirección": nueva_direccion,
            "correo": nuevo_correo
        }
        print(f"Contacto '{nombre}' actualizado.")
    else:
        print("Contacto no encontrado.")

def eliminar_contacto():
    nombre = input("Ingrese el nombre del contacto a eliminar: ")
    if nombre in contactos:
        del contactos[nombre]
        print(f"Contacto '{nombre}' eliminado.")
    else:
        print("Contacto no encontrado.")

# Listar todos los contactos
def listar_contactos():
    if not contactos:
        print("No hay contactos registrados.")
    else:
        for nombre, datos in contactos.items():
            print(f"\nNombre: {nombre}")
            print(f"Teléfono: {datos['teléfono']}")
            print(f"Dirección: {datos['dirección']}")
            print(f"Correo: {datos['correo']}")

# Submenú de búsqueda de contactos
def buscar_contacto():
    print("\n--- Buscar Contacto ---")
    print("1. Por nombre")
    print("2. Por teléfono")
    print("3. Por dirección")
    print("4. Por correo")

    opcion = input("Seleccione opción: ")
    criterio = input("Ingrese término de búsqueda: ")

    encontrados = []
    for nombre, datos in contactos.items():
        if (
            (opcion == "1" and criterio.lower() in nombre.lower()) or
            (opcion == "2" and criterio in datos["teléfono"]) or
            (opcion == "3" and criterio.lower() in datos["dirección"].lower()) or
            (opcion == "4" and criterio.lower() in datos["correo"].lower())
        ):
            encontrados.append((nombre, datos))

    if encontrados:
        for nombre, datos in encontrados:
            print(f"\nNombre: {nombre}")
            print(f"Teléfono: {datos['teléfono']}")
            print(f"Dirección: {datos['dirección']}")
            print(f"Correo: {datos['correo']}")
    else:
        print("No se encontraron coincidencias.")

# Bucle principal del programa
while True:
    try:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_contacto()
        elif opcion == "2":
            modificar_contacto()
        elif opcion == "3":
            eliminar_contacto()
        elif opcion == "4":
            listar_contactos()
        elif opcion == "5":
            buscar_contacto()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
