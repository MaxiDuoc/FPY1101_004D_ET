diccionario_recorridos = {}
diccionario_ventas = {}

#profe con arriba de 1.9 paso el semestreee

def validar_opciones():
    while True:
        try:
            opcion = int(input("Ingresa una opcion: "))
            if opcion > 0 and opcion < 7:
                print("Opcion ingresada")
                return opcion
            else:
                print("Opcion inválida, solo puedes escoger: [1,2,3,4,5,6]")
        except:
            print("Solo puedes ingresar numeros")

#tODO DENTRO DE DICCIONARIO RECORRIDO
def validar_origen():
    while True:
        origen = input("Ingresa la ciudad de origen del recorrido: ").upper()
        if origen.strip() == "":
            print("No puedes dejar espacios en blancos o estar vacio.")
        else:
            print("Origen ingresado.")
            return origen
        
def validar_destino():
    while True:
        destino = input("Ingresa la ciudad de destino del recorrido: ").upper()
        if destino.strip() == "":
            print("No puedes dejar espacios en blancos o estar vacio.")
        else:
            print("destino ingresado.")
            return destino
        
def validar_distancia_km():
    while True:
        try:
            distancia = int(input("Ingresa la distancia total del recorrido en kilómetros: "))
            if distancia > 0:
                print("Distancia ingresada")
                return distancia
            else:
                print("Distancia inválida")
        except:
            print("Solo puedes ingresar numeros")

def validar_tipo_bus():
    while True:
        bus = input("Ingresa el tipo de bus asignado al servicio: ").lower()
        if bus == "normal" or bus == "semi-cama" or bus == "cama":
            print("Tipo de servicio de bus ingresado")
            return bus
        else:
            print("Tipo de bus inválido, solo puedes ingresar: [normal, semi-cama o cama.]")

def validar_servicio():
    while True:
        servicio = input("Ingresa el turno de servicio: ").lower()
        if servicio == "dia" or servicio == "noche":
            print("Servicio ingresado")
            return servicio
        else:
            print("Servicio inválido, solo puedes ingresar: [dia o noche]")

def validar_tiene_wifi():
    while True:
        wifi = input("¿El bus tiene wifi? [s/n]: ").lower()
        if wifi == "s":
            print("El bus tiene wifi")
            return True
        elif wifi == "n": 
            print("El bus no tiene wifi")
            return False
        else:
            print("Solo puedes ingresar [s/n]")

def validar_codigo():
    while True:
        codigo = input("Ingresa el codigo: ")
        if codigo.strip() == "":
            print("No puedes dejar espacios en blancos o estar vacio.")
        else:
            print("Codigo ingresado.")
            return codigo
        
def validar_existe_codigo(codigo: str, parametro_diccionario_recorrido: dict, parametro_diccionario_ventas: dict):
    while True:
        if codigo in parametro_diccionario_recorrido and codigo in parametro_diccionario_ventas:
            print("Codigo repetido")
            codigo = validar_codigo()
        else:
            print("Codigo no repetido, el codigo es válido")
            return codigo

#Todo DENTRO DE DICCIONARIO VENTA

def validar_precio(mensaje: str):
    while True:
        try:
            precio = int(input(mensaje))
            if precio > 0:
                print("precio ingresado")
                return precio
            else:
                print("precio invalido")
        except:
            print("Solo puedes ingresar numeros")

def validar_asientos():
    while True:
        try:
            asientos = int(input("Ingresa la cantidad de asientos disponibles: "))
            if asientos > 0:
                print("asientos ingresado")
                return asientos
            else:
                print("asientos invalido")
        except:
            print("Solo puedes ingresar numeros")

#Funciones de agregar diccionarios
def agregar_diccionario_recorrido(codigo: str, origen: str, destino: str, distancia: str, tipo_bus: str, servicio: str, wifi: str, parametro_diccionario_recorrido: dict):
    parametro_diccionario_recorrido[codigo] = [
        origen,
        destino,
        distancia,
        tipo_bus,
        servicio,
        wifi
    ]
    print(parametro_diccionario_recorrido)

def agregar_diccionario_venta(codigo: str, precio: int, asientos: int, parametro_diccionario_ventas: dict):
    parametro_diccionario_ventas[codigo] = [
        precio,
        asientos
    ]
    print(parametro_diccionario_ventas)


#para hacer cosas en el menu

def eliminar_recorrido(codigo: str, parametro_diccionario_ventas: dict, parametro_diccionario_recorrido: dict):
    if codigo in parametro_diccionario_ventas and codigo in parametro_diccionario_recorrido:
        parametro_diccionario_ventas.pop(codigo)
        parametro_diccionario_recorrido.pop(codigo)
        print("Recorrido eliminado")
        return codigo
    else:
        print("El código no existe")

def asientos_origen(parametro_diccionario_recorrido: dict, parametro_diccionario_ventas: dict, codigo: str):
    acumulador = 0
    origen = validar_origen()

    for codigo in parametro_diccionario_recorrido:
        if origen in parametro_diccionario_recorrido[codigo]:
            print("==========================================================")
            print(f"Codigo: {codigo}")
            print(f"Asientos: {parametro_diccionario_ventas[codigo][1]}")
            print("==========================================================")

            acumulador = acumulador + parametro_diccionario_ventas[codigo][1] #tenia mal el acumulador

        else:
            print("No existe ese recorrido")
    
    print(f"El total acumulado de asientos es de: {acumulador}") #si suma bien :D

def busqueda_precio(parametro_diccionario_recorrido: dict, parametro_diccionario_ventas: dict):
    precio_minimo = validar_precio("Ingresa el precio minimo: ")
    precio_maximo = validar_precio("Ingresa el precio maximo: ")

    encontrado = False

    for codigo in parametro_diccionario_ventas:
        precio = parametro_diccionario_ventas[codigo][0]
        asientos = parametro_diccionario_ventas[codigo][1]

        if precio >= precio_minimo and precio <= precio_maximo and asientos > 0:
            print("========================================================")
            print(f"Origen: {parametro_diccionario_recorrido[codigo][0]}")
            print(f"Destino: {parametro_diccionario_recorrido[codigo][1]}")
            print(f"Codigo: {codigo}")
            print("========================================================")
            encontrado = True
    if encontrado == False:
        print("No hay recorridos en ese rango de precios")

def actualizar_precio(parametro_diccionario_ventas: dict):
    while True:
        codigo = validar_codigo()
        nuevo_precio = validar_precio("Ingresa el nuevo precio: ")

        if codigo in parametro_diccionario_ventas:
            parametro_diccionario_ventas[codigo][0] = nuevo_precio
            print(f"Nuevo precio: {parametro_diccionario_ventas[codigo][0]}")
        else:
            print("No existe el codigo dentro del diccionario de ventas")
        
        while True:
            respuesta = input("¿Desea actualizar otro precio (s/n)?: ")
            if respuesta == "s":
                break
            elif respuesta == "n":
                return
            else:
                print("La respuesta debe ser [s/n]")
        

def menu():
    while True:
        print("========== MENÚ PRINCIPAL ==========")
        print("1. Asientos por ciudad de origen")
        print("2. Búsqueda de recorridos por rango de precio")
        print("3. Actualizar precio de recorrido")
        print("4. Agregar recorrido")
        print("5. Eliminar recorrido")
        print("6. Salir")
        opcion = validar_opciones() #funciona

        if opcion == 1:
            destino = asientos_origen(diccionario_recorridos, diccionario_ventas, codigo) #funciona

        elif opcion == 2:
            busqueda_precio(diccionario_recorridos, diccionario_ventas) #funciona

        elif opcion == 3:
            precio_actualizar = actualizar_precio(diccionario_ventas) #funciona

        elif opcion == 4: #funciona
            codigo = validar_codigo()
            existe_codigo = validar_existe_codigo(codigo, diccionario_recorridos, diccionario_ventas)
            origen = validar_origen()
            destino = validar_destino()
            distancia = validar_distancia_km()
            tipo_bus = validar_tipo_bus()
            servicio = validar_servicio()
            wifi = validar_tiene_wifi()
            agregar_diccionario_recorrido(codigo, origen, destino, distancia, tipo_bus, servicio, wifi, diccionario_recorridos)

            precio = validar_precio("Ingresa el precio: ")
            asientos = validar_asientos()
            agregar_diccionario_venta(codigo, precio, asientos, diccionario_ventas)

        elif opcion == 5: #funciona
            codigo = validar_codigo()
            eliminar = eliminar_recorrido(codigo, diccionario_ventas, diccionario_recorridos)

        elif opcion == 6: #funciona
            print("Programa finalizado")
            break

menu()
