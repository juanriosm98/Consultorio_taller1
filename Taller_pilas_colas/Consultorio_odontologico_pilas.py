
from collections import deque
from datetime import datetime, timedelta



# CONSULTORIO ODONTOLOGICO
# TALLER: PILAS Y COLAS



# Lista general de pacientes
pacientes = []



# PARTE 1: REGISTRO DE PACIENTES



def registrar_pacientes():
    print("\n=== REGISTRO DE PACIENTES ===")

    while True:

        # VALIDAR CEDULA: SOLO NUMEROS
        while True:
            cedula = input("Cedula: ").strip()

            if cedula.isdecimal():
                break
            else:
                print("ERROR: La cedula solo permite numeros.")
                print("Intente nuevamente.\n")

        # VALIDAR NOMBRE: SOLO LETRAS Y ESPACIOS
        while True:
            nombre = input("Nombre completo: ").strip()

            if (
                nombre != ""
                and all(
                    caracter.isalpha() or caracter.isspace()
                    for caracter in nombre
                )
                and any(caracter.isalpha() for caracter in nombre)
            ):
                break
            else:
                print("ERROR: El nombre solo permite letras y espacios.")
                print("Intente nuevamente.\n")

        # VALIDAR TELEFONO: SOLO NUMEROS
        while True:
            telefono = input("Telefono: ").strip()

            if telefono.isdecimal():
                break
            else:
                print("ERROR: El telefono solo permite numeros.")
                print("Intente nuevamente.\n")

        
        # SELECCIONAR TIPO DE ATENCION
        while True:
            print("\n=== TIPO DE ATENCION ===")
            print("1. Limpieza")
            print("2. Calzas")
            print("3. Extraccion")
            print("4. Diagnostico")

            opcion_atencion = input(
                "Seleccione el tipo de atencion (1-4): "
            ).strip()

            if opcion_atencion == "1":
                tipo_atencion = "limpieza"
                break
            elif opcion_atencion == "2":
                tipo_atencion = "calzas"
                break
            elif opcion_atencion == "3":
                tipo_atencion = "extraccion"
                break
            elif opcion_atencion == "4":
                tipo_atencion = "diagnostico"
                break
            else:
                print("ERROR: Opcion no valida.")
                print("Ingrese un numero del 1 al 4.\n")


        # SELECCIONAR PRIORIDAD DE ATENCION
        while True:
            print("\n=== PRIORIDAD DE ATENCION ===")
            print("1. Normal")
            print("2. Urgente")

            opcion_prioridad = input(
                "Seleccione la prioridad (1-2): "
            ).strip()

            if opcion_prioridad == "1":
                prioridad = "normal"
                break
            elif opcion_prioridad == "2":
                prioridad = "urgente"
                break
            else:
                print("ERROR: Opcion no valida.")
                print("Ingrese 1 para Normal o 2 para Urgente.\n")



        


  # MOSTRAR HORARIOS DISPONIBLES PARA LOS PROXIMOS 7 DIAS
        while True:
            ahora = datetime.now()
            hoy = ahora.date()
            fecha_limite = hoy + timedelta(days=7)

            print("\n=== AGENDA DISPONIBLE ===")
            print(
                f"Desde {hoy.strftime('%d/%m/%Y')} "
                f"hasta {fecha_limite.strftime('%d/%m/%Y')}"
            )

            horarios_disponibles = []
            fecha_dia = hoy

            # Revisar cada dia de la agenda
            while fecha_dia <= fecha_limite:

                # Horarios de inicio de cada cita
                horas = [6, 7, 8, 9, 10, 11, 14, 15, 16, 17, 18]

                for hora in horas:
                    fecha_hora = datetime(
                        fecha_dia.year,
                        fecha_dia.month,
                        fecha_dia.day,
                        hora,
                        0
                    )

                    # No ofrecer horarios que ya pasaron
                    if fecha_hora <= ahora:
                        continue

                    # Comprobar si el horario ya esta ocupado
                    horario_ocupado = False

                    for paciente_registrado in pacientes:
                        if paciente_registrado["fecha"] == fecha_hora:
                            horario_ocupado = True
                            break

                    # Agregar unicamente los horarios libres
                    if horario_ocupado == False:
                        horarios_disponibles.append(fecha_hora)

                fecha_dia += timedelta(days=1)

            if not horarios_disponibles:
                print("No hay horarios disponibles en estos 7 dias.")
                return

            # Mostrar solamente las citas disponibles
            print("\n=== HORARIOS LIBRES ===")
            fecha_mostrada = None

            for numero, horario in enumerate(
                horarios_disponibles, start=1
            ):
                if horario.date() != fecha_mostrada:
                    fecha_mostrada = horario.date()
                    print(
                        f"\nFecha: "
                        f"{fecha_mostrada.strftime('%d/%m/%Y')}"
                    )

                print(
                    f"{numero}. "
                    f"{horario.strftime('%I:%M %p')}"
                )

            # Seleccionar una cita de la lista
            while True:
                opcion = input(
                    "\nSeleccione el numero de la cita: "
                ).strip()

                if opcion.isdecimal():
                    numero = int(opcion)

                    if 1 <= numero <= len(horarios_disponibles):
                        fecha = horarios_disponibles[numero - 1]
                        break

                print("Opcion invalida. Elija un numero de la lista.")

             # Verificar que la cita no haya sido asignada
            horario_ocupado = False

            for paciente_registrado in pacientes:
                if paciente_registrado["fecha"] == fecha:
                    horario_ocupado = True
                    break

            if horario_ocupado:
                print("\nERROR: Esa cita ya esta ocupada.")
                print("Se mostrara nuevamente la agenda disponible.")
                continue

            break


        # GUARDAR PACIENTE DESPUES DE VALIDAR LOS DATOS
        paciente = {
            "cedula": cedula,
            "nombre": nombre,
            "telefono": telefono,
            "tipo_atencion": tipo_atencion,
            "prioridad": prioridad,
            "fecha": fecha
        }

        pacientes.append(paciente)

        print("\nPaciente registrado correctamente.")

        continuar = input(
            "Desea registrar otro paciente? (s/n): "
        ).strip().lower()

        if continuar != "s":
            break





# PARTE 2: IMPLEMENTACION DE LA PILA


def generar_pila_urgentes():
    # Filtrar solo extracciones con prioridad urgente
    urgentes = [
        paciente for paciente in pacientes
        if paciente["tipo_atencion"] == "extraccion"
        and paciente["prioridad"] == "urgente"
    ]

    # Ordenar de la fecha mas lejana a la mas cercana
    # para que la fecha mas cercana quede en la cima.
    urgentes.sort(
        key=lambda paciente: paciente["fecha"],
        reverse=True
    )

    # La cima de la pila es el final de la lista.
    pila = urgentes

    return pila

def mostrar_pila_urgentes():
    # Generar la pila de pacientes urgentes
    pila = generar_pila_urgentes()

    print("\n=== INFORME DE PILA DE URGENCIAS ===")

    # Verificar si existen pacientes urgentes
    if not pila:
        print("No hay pacientes con extraccion y prioridad urgente.")
        input("\nPresione Enter para regresar al menu...")
        return

    print("Orden de atencion: fecha mas cercana primero.\n")

    # Mostrar los pacientes desde la cima de la pila
    for posicion, paciente in enumerate(reversed(pila), start=1):
        print(f"\nPrioridad de llamada: {posicion}")
        print("Cedula:", paciente["cedula"])
        print("Nombre:", paciente["nombre"])
        print("Telefono:", paciente["telefono"])
        print("Atencion:", paciente["tipo_atencion"].title())
        print("Prioridad:", paciente["prioridad"].title())
        print(
            "Fecha de cita:",
            paciente["fecha"].strftime("%d/%m/%Y %I:%M %p")
        )
        print("-" * 40)

    input("\nPresione Enter para regresar al menu...")

def atender_pila_urgentes():
    pila = generar_pila_urgentes()

    print("\n=== ATENCION DE URGENCIAS ===")

    if not pila:
        print("No hay pacientes pendientes en la pila.")
        return

    while pila:
        # pop() retira el paciente que esta en la cima
        paciente = pila.pop()

        print("\nLlamando al paciente:")
        print("Nombre:", paciente["nombre"])
        print("Cedula:", paciente["cedula"])
        print(
            "Fecha de cita:",
            paciente["fecha"].strftime("%d/%m/%Y %H:%M")
        )

        respuesta = input(
            "Presione Enter para continuar con el siguiente "
            "paciente o escriba 's' para detener: "
        ).strip().lower()

        if respuesta == "s":
            print("Atencion de urgencias detenida.")
            break



# PARTE 3: IMPLEMENTACION DE LA COLA


def generar_cola():
    # Ordenar los pacientes por fecha y hora de agenda
    agenda = sorted(
        pacientes,
        key=lambda paciente: paciente["fecha"]
    )

    # deque permite agregar al final y retirar al principio
    cola = deque(agenda)

    return cola


def mostrar_agenda():
    cola = generar_cola()

    print("\n=== AGENDA DIARIA DEL CONSULTORIO ===")

    if not cola:
        print("No hay pacientes registrados.")
        return

    for posicion, paciente in enumerate(cola, start=1):
        print(f"\nTurno: {posicion}")
        print("Nombre:", paciente["nombre"])
        print("Cedula:", paciente["cedula"])
        print(
            "Fecha y hora:",
            paciente["fecha"].strftime("%d/%m/%Y %H:%M")
        )
        print("Atencion:", paciente["tipo_atencion"].title())
        print("Prioridad:", paciente["prioridad"].title())


def mostrar_agenda():
    cola = generar_cola()

    print("\n=== AGENDA DIARIA DEL CONSULTORIO ===")

    if not cola:
        print("No hay pacientes registrados.")
        return

    for posicion, paciente in enumerate(cola, start=1):
        print(f"\nTurno: {posicion}")
        print("Nombre:", paciente["nombre"])
        print("Cedula:", paciente["cedula"])
        print(
            "Fecha y hora:",
            paciente["fecha"].strftime("%d/%m/%Y %H:%M")
        )
        print("Atencion:", paciente["tipo_atencion"].title())
        print("Prioridad:", paciente["prioridad"].title())

    input("\nPresione Enter para regresar al menu...")

def atender_cola():
    cola = generar_cola()

    print("\n=== ATENCION POR COLA ===")

    if not cola:
        print("No hay pacientes en la cola.")
        return

    while cola:
        # popleft() retira al primero que ingreso a la cola
        paciente = cola.popleft()

        print("\nSiguiente paciente:")
        print("Nombre:", paciente["nombre"])
        print("Cedula:", paciente["cedula"])
        print(
            "Cita:",
            paciente["fecha"].strftime("%d/%m/%Y %H:%M")
        )

        print("Paciente atendido.")

        print("Pacientes pendientes:", len(cola))

        if cola:
            continuar = input(
                "Presione Enter para continuar o 's' para salir: "
            ).strip().lower()

            if continuar == "s":
                print("Atencion detenida.")
                print("Pacientes que siguen pendientes:")

                for pendiente in cola:
                    print(
                        pendiente["nombre"],
                        "-",
                        pendiente["fecha"].strftime(
                            "%d/%m/%Y %H:%M"
                        )
                    )
                break



# 4: MENU PRINCIPAL


def menu():
    while True:
        print("\n================================")
        print(" CONSULTORIO ODONTOLOGICO")
        print("================================")
        print("1. Registrar pacientes")
        print("2. Generar informe de pila urgente")
        print("3. Atender pacientes de la pila")
        print("4. Generar agenda diaria")
        print("5. Atender pacientes por cola")
        print("6. Salir")

        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            registrar_pacientes()
        elif opcion == "2":
            mostrar_pila_urgentes()
        elif opcion == "3":
            atender_pila_urgentes()
        elif opcion == "4":
            mostrar_agenda()
        elif opcion == "5":
            atender_cola()
        elif opcion == "6":
            print("Programa finalizado.")
            break
        else:
            print("Opcion invalida. Intente nuevamente.")


# Iniciar el programa
if __name__ == "__main__":
    menu()
