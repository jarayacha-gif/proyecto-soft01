#============================================================
# Archivo: ejercicio8_regreso.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrantes: Jehidam Araya Chaves
# Fecha: 31/10/2026         Versión: 1.0
#
# Descripción: Evalúa el regreso de la tripulación a la Tierra
# y calcula la supervivencia cuando la nave queda varada.
# ============================================================

# Declaración de constantes
CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO_TRIPULANTE = 2
CONSUMO_ENERGIA_DIA = 5
CONSUMO_PROVISIONES_TRIPULANTE = 1

# Entrada de datos
tripulantes = int(input("Ingrese el número de tripulantes: "))
viajeIda = int(input("Ingrese la duración del viaje de ida en días: "))
combustibleDisponible = int(input("Ingrese la cantidad de combustible disponible en la nave: "))
oxigenoDisponible = int(input("Ingrese la cantidad de oxígeno disponible en la nave: "))
energiaDisponible = int(input("Ingrese la cantidad de energía disponible en la nave: "))
provisionesDisponibles = int(input("Ingrese la cantidad de provisiones disponibles en la nave: "))

# Procesamiento
combustibleNecesario = viajeIda * CONSUMO_COMBUSTIBLE_DIA

diasCompletados = 0
continuarRegreso = True

# Decisión: verificar si existe combustible para regresar
if combustibleDisponible >= combustibleNecesario:

    # Caso A: simular el regreso
    for dia in range(viajeIda):

        if continuarRegreso:

            # Verificar si todos los recursos alcanzan
            if combustibleDisponible >= CONSUMO_COMBUSTIBLE_DIA and oxigenoDisponible >= (tripulantes * CONSUMO_OXIGENO_TRIPULANTE) and energiaDisponible >= CONSUMO_ENERGIA_DIA and provisionesDisponibles >= tripulantes * CONSUMO_PROVISIONES_TRIPULANTE:

                # Descontar el consumo diario
                combustibleDisponible -= CONSUMO_COMBUSTIBLE_DIA
                oxigenoDisponible -= tripulantes * CONSUMO_OXIGENO_TRIPULANTE
                energiaDisponible -= CONSUMO_ENERGIA_DIA
                provisionesDisponibles -= tripulantes * CONSUMO_PROVISIONES_TRIPULANTE

                diasCompletados += 1

                print(f"Día {diasCompletados} | Combustible: {combustibleDisponible} | Oxígeno: {oxigenoDisponible} | Energía: {energiaDisponible} | Provisiones: {provisionesDisponibles}")

            else:

                print(f"El regreso se interrumpió en el día {dia + 1}.")

                # Identificar todos los recursos insuficientes
                if oxigenoDisponible < tripulantes * CONSUMO_OXIGENO_TRIPULANTE:
                    print("Recurso insuficiente: oxígeno")

                if energiaDisponible < CONSUMO_ENERGIA_DIA:
                    print("Recurso insuficiente: energía")

                if provisionesDisponibles < tripulantes * CONSUMO_PROVISIONES_TRIPULANTE:
                    print("Recurso insuficiente: provisiones")

                continuarRegreso = False

    # Resultados del regreso
    if continuarRegreso:
        print(f"""
        La tripulación regresó exitosamente a la Tierra.
        Combustible restante: {combustibleDisponible} unidades
        Oxígeno restante: {oxigenoDisponible} unidades
        Energía restante: {energiaDisponible} unidades
        Provisiones restantes: {provisionesDisponibles} unidades
        """)

    else:
        print("La tripulación no completó el regreso.")

else:

    # Caso B: tripulación varada por falta de combustible
    print("La tripulación quedó varada en el destino.")

    # Calcular los días de supervivencia por recurso
    diasOxigeno = oxigenoDisponible // (tripulantes * CONSUMO_OXIGENO_TRIPULANTE)
    diasEnergia = energiaDisponible // CONSUMO_ENERGIA_DIA
    diasProvisiones = provisionesDisponibles // tripulantes

    print(f"""
    Días por oxígeno: {diasOxigeno}
    Días por energía: {diasEnergia}
    Días por provisiones: {diasProvisiones}
    """)

    # Determinar el menor valor mediante condicionales
    supervivencia = diasOxigeno

    if diasEnergia < supervivencia:
        supervivencia = diasEnergia

    if diasProvisiones < supervivencia:
        supervivencia = diasProvisiones

    print(f"Supervivencia estimada: {supervivencia} días")

    # Identificar todos los recursos limitantes
    print("Recurso(s) limitante(s):", end=" ")

    if diasOxigeno == supervivencia:
        print("oxígeno", end="")

    if diasEnergia == supervivencia:
        if diasOxigeno == supervivencia:
            print(", energía", end="")
        else:
            print("energía", end="")

    if diasProvisiones == supervivencia:
        if diasOxigeno == supervivencia or diasEnergia == supervivencia:
            print(", provisiones", end="")
        else:
            print("provisiones", end="")

    print()
