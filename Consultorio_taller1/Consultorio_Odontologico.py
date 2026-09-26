from datetime import datetime
clientes = []

print("CONSULTORIO ODONTOLÓGICO")

# CICLO PRINCIPAL PARA REGISTRAR VARIOS CLIENTES
while True:

    print("\n===== REGISTRO DE CLIENTE =====")

    # VALIDAR CEDULA
    while True:
        cedula = input("Ingrese la cedula: ").strip()
        

        if cedula.isdecimal():
            print("Cedula ingresada:", cedula)
            break
        else:
            print("ERROR: La cedula solo debe contener numeros.")
            print("Intente nuevamente.")

    # VALIDAR NOMBRE
    while True:
        nombre = input("Ingrese el nombre: ")

        if nombre.replace(" ", "").isalpha():
            break
        else:
            print("ERROR: El nombre solo debe contener letras.")
            print("Intente nuevamente.")

    # VALIDAR TELEFONO
    while True:
        telefono = input("Ingrese el telefono: ")

        if telefono.isdigit():
            break
        else:
            print("ERROR: El telefono solo debe contener numeros.")
            print("Intente nuevamente.")
 # PRIORIDAD DE ATENCION
    print("\n===== PRIORIDAD DE ATENCION =====")
    print("1. Normal")
    print("2. Urgente")

    while True:
        prioridad_opcion = input("Seleccione la prioridad (1-2): ")

        if prioridad_opcion == "1":
            prioridad = "Normal"
            break
        elif prioridad_opcion == "2":
            prioridad = "Urgente"
            break
        else:
            print("ERROR: Seleccione 1 o 2.")

    print("Prioridad seleccionada:", prioridad)
     # FECHA DE LA CITA
    # FECHA Y HORA DE LA CITA
    while True:
        fecha_cita = input(
            "Ingrese fecha y hora (DD/MM/AAAA HH:MM): "
        )

        try:
            fecha_objeto = datetime.strptime(
                fecha_cita, "%d/%m/%Y %H:%M"
            )

            ahora = datetime.now().replace(
                second=0, microsecond=0
            )

            if fecha_objeto < ahora:
                print("ERROR: La cita no puede ser en el pasado.")
            else:
                break

        except ValueError:
            print(
                "ERROR: Formato incorrecto. "
                "Use DD/MM/AAAA HH:MM."
            )

    # MOSTRAR DATOS DEL CLIENTE
    print("\n===== DATOS DEL CLIENTE =====")
    print("Cedula:", cedula)
    print("Nombre:", nombre)
    print("Telefono:", telefono)

    # SELECCIONAR TIPO DE CLIENTE
    print("\n===== TIPO DE CLIENTE =====")
    print("1. Particular")
    print("2. EPS")
    print("3. Prepagada")

    while True:
        opcion = input("Seleccione una opcion (1-3): ")

        if opcion == "1":
            tipo_cliente = "Particular"
            break
        elif opcion == "2":
            tipo_cliente = "EPS"
            break
        elif opcion == "3":
            tipo_cliente = "Prepagada"
            break
        else:
            print("ERROR: Seleccione una opcion valida.")

    print("Cliente seleccionado:", tipo_cliente)

    # SELECCIONAR TIPO DE ATENCION
    print("\n===== TIPO DE ATENCION =====")
    print("1. Limpieza")
    print("2. Calzas")
    print("3. Extraccion")
    print("4. Diagnostico")

    while True:
        opcion_atencion = input("Seleccione una opcion (1-4): ")

        if opcion_atencion == "1":
            tipo_atencion = "Limpieza"
            break
        elif opcion_atencion == "2":
            tipo_atencion = "Calzas"
            break
        elif opcion_atencion == "3":
            tipo_atencion = "Extraccion"
            break
        elif opcion_atencion == "4":
            tipo_atencion = "Diagnostico"
            break
        else:
            print("ERROR: Seleccione una opcion valida.")

    print("Tipo de atencion seleccionado:", tipo_atencion)

    # VALIDAR CANTIDAD
    if tipo_atencion == "Limpieza" or tipo_atencion == "Diagnostico":
        cantidad = 1
        print("La cantidad es:", cantidad)

    else:
        while True:
            cantidad = input("Ingrese la cantidad: ")

            if cantidad.isdigit():
                cantidad = int(cantidad)

                if cantidad > 0:
                    break
                else:
                    print("ERROR: La cantidad debe ser mayor que cero.")
            else:
                print("ERROR: Ingrese solamente numeros.")

    print("Cantidad seleccionada:", cantidad)

    # VALOR DE LA CITA
    if tipo_cliente == "Particular":
        valor_cita = 80000

    elif tipo_cliente == "EPS":
        valor_cita = 5000

    elif tipo_cliente == "Prepagada":
        valor_cita = 30000

    # CALCULAR VALOR DE LA ATENCION

    if tipo_cliente == "Particular":

        if tipo_atencion == "Limpieza":
            valor_atencion = 6000

        elif tipo_atencion == "Calzas":
            valor_atencion = 8000

        elif tipo_atencion == "Extraccion":
            valor_atencion = 100000

        elif tipo_atencion == "Diagnostico":
            valor_atencion = 50000

    elif tipo_cliente == "EPS":

        if tipo_atencion == "Limpieza":
            valor_atencion = 0

        elif tipo_atencion == "Calzas":
            valor_atencion = 40000

        elif tipo_atencion == "Extraccion":
            valor_atencion = 40000

        elif tipo_atencion == "Diagnostico":
            valor_atencion = 0

    elif tipo_cliente == "Prepagada":

        if tipo_atencion == "Limpieza":
            valor_atencion = 0

        elif tipo_atencion == "Calzas":
            valor_atencion = 10000

        elif tipo_atencion == "Extraccion":
            valor_atencion = 10000

        elif tipo_atencion == "Diagnostico":
            valor_atencion = 0

    # CALCULAR TOTAL A PAGAR
    total_pagar = valor_cita + (valor_atencion * cantidad)

    # MOSTRAR VALORES
    print("\n===== VALOR DE LA CITA =====")
    print("Valor de la cita: $", valor_cita)
    print("Valor de la atencion: $", valor_atencion)
    print("Cantidad:", cantidad)
    print("TOTAL A PAGAR: $", total_pagar)

    # GUARDAR DATOS DEL CLIENTE EN UN DICCIONARIO
    cliente = {
        "cedula": cedula,
        "nombre": nombre,
        "telefono": telefono,
        "tipo_cliente": tipo_cliente,
        "tipo_atencion": tipo_atencion,
        "cantidad": cantidad,
        "valor_cita": valor_cita,
        "valor_atencion": valor_atencion,
        "total_pagar": total_pagar,
        "prioridad": prioridad,
        "fecha_cita": fecha_cita
    }

    # AGREGAR CLIENTE A LA LISTA
    clientes.append(cliente)

    print("\nCliente registrado correctamente.")

    # PREGUNTAR SI DESEA REGISTRAR OTRO CLIENTE
    while True:
        continuar = input(
            "¿Desea registrar otro cliente? (S/N): "
        ).strip().upper()

        if continuar == "S":
            break
        elif continuar == "N":
            break
        else:
            print("ERROR: Escriba S para continuar o N para terminar.")

    if continuar == "N":
        break

# RESUMEN FINAL
print("\n===== RESUMEN FINAL =====")
print("Cantidad de clientes registrados:", len(clientes))

print("\n===== LISTA DE CLIENTES =====")

for cliente in clientes:
    print("-----------------------------")
    print("Cedula:", cliente["cedula"])
    print("Nombre:", cliente["nombre"])
    print("Telefono:", cliente["telefono"])
    print("Tipo de cliente:", cliente["tipo_cliente"])
    print("Tipo de atencion:", cliente["tipo_atencion"])
    print("Cantidad:", cliente["cantidad"])
    print("Total a pagar: $", cliente["total_pagar"])
    print("Prioridad:", cliente["prioridad"])
    print("Fecha y hora:", cliente["fecha_cita"])

print("\nPrograma finalizado.")

print("\n===== RESUMEN GENERAL =====")

total_clientes = len(clientes)

ingresos_totales = sum(
    cliente["total_pagar"] for cliente in clientes
)

cantidad_extracciones = sum(
    1 for cliente in clientes
    if cliente["tipo_atencion"] == "Extraccion"
)

print("Total de clientes:", total_clientes)
print("Ingresos totales: $", ingresos_totales)
print("Clientes para extracción:", cantidad_extracciones)
# ORDENAR CLIENTES POR VALOR DE ATENCION
clientes_ordenados = sorted(
    clientes,
    key=lambda cliente: cliente["valor_atencion"],
    reverse=True
)

print("\n===== CLIENTES ORDENADOS POR VALOR DE ATENCION =====")

for cliente in clientes_ordenados:
    print("-----------------------------")
    print("Cedula:", cliente["cedula"])
    print("Nombre:", cliente["nombre"])
    print("Tipo de atencion:", cliente["tipo_atencion"])
    print("Valor de atencion: $", cliente["valor_atencion"])
    # BUSCAR CLIENTE POR CEDULA
print("\n===== BUSCAR CLIENTE =====")

cedula_buscar = input(
    "Ingrese la cedula del cliente que desea buscar: "
).strip()

encontrado = False

for cliente in clientes_ordenados:

    if cliente["cedula"] == cedula_buscar:

        print("\n===== CLIENTE ENCONTRADO =====")
        print("Cedula:", cliente["cedula"])
        print("Nombre:", cliente["nombre"])
        print("Telefono:", cliente["telefono"])
        print("Tipo de cliente:", cliente["tipo_cliente"])
        print("Tipo de atencion:", cliente["tipo_atencion"])
        print("Cantidad:", cliente["cantidad"])
        print("Valor de la cita: $", cliente["valor_cita"])
        print("Valor de la atencion: $", cliente["valor_atencion"])
        print("Total a pagar: $", cliente["total_pagar"])
        print("Prioridad:", cliente["prioridad"])
        print("Fecha y hora:", cliente["fecha_cita"])

        encontrado = True
        break

if encontrado == False:
    print("No se encontro un cliente con esa cedula.")

print("\nPrograma finalizado.")