""" ============================================================
 Archivo: ejercicio1Proyecto.py
 Curso: SOFT-01 Principios de Programación 1 - Sección SCV3
 Integrante: Jehidam Araya Chaves
 Fecha: 29/09/2026
 Versión: 1.1
 Descripción: Calcula los recursos necesarios para una misión.
============================================================"""

# Declaración de constantes
TRAYECTO_VUELTA = 2
RESERVA_COMBUSTIBLE = 10
CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO_TRIPULANTE_DIA = 2
RESERVA_OXIGENO = 5
CONSUMO_ENERGIA_DIA = 5
RESERVA_ENERGIA = 10
CONSUMO_PROVISION_TRIPULANTE_DIA = 1
RESERVA_PROVISIONES = 3

# Entrada de datos
nombreMision = input("Ingrese el nombre de la misión: ")
cantidadTripulantes = int(input("Ingrese la cantidad de tripulantes: "))
diasViaje = int(input("Ingrese la cantidad de días de viaje para llegar al destino: "))

# Procesamiento
# Se calcula el combustible necesario para la ida y el regreso.
combustibleIda = diasViaje * CONSUMO_COMBUSTIBLE_DIA
combustibleRegreso = diasViaje * CONSUMO_COMBUSTIBLE_DIA
combustibleTotal = combustibleIda + combustibleRegreso + RESERVA_COMBUSTIBLE

# Se calculan los recursos necesarios para la tripulación y la misión.
oxigenoRequerido = ( (diasViaje * TRAYECTO_VUELTA ) * cantidadTripulantes * CONSUMO_OXIGENO_TRIPULANTE_DIA + RESERVA_OXIGENO) 
energiaRequerida = (diasViaje * TRAYECTO_VUELTA ) * CONSUMO_ENERGIA_DIA + RESERVA_ENERGIA
provisionesRequeridas = (diasViaje * TRAYECTO_VUELTA )* cantidadTripulantes * CONSUMO_PROVISION_TRIPULANTE_DIA + RESERVA_PROVISIONES

# Salida de resultados
print(f"""
===== RESUMEN DE LA MISIÓN =====

Nombre de la misión: {nombreMision}
Cantidad de tripulantes: {cantidadTripulantes}
Días de viaje: {diasViaje}
Combustible para ida: {combustibleIda} unidades
Combustible para regreso: {combustibleRegreso} unidades
Reserva de combustible: {RESERVA_COMBUSTIBLE} unidades
Combustible total requerido: {combustibleTotal} unidades
Oxígeno requerido: {oxigenoRequerido} unidades
Energía requerida: {energiaRequerida} unidades
Provisiones requeridas: {provisionesRequeridas} unidades
""")
