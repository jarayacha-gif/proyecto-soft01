""" ============================================================
Archivo: ejercicio2Proyecto.py
Curso: SOFT-01 Principios de Programación 1 - Sección SCV3
Integrante: Jehidam Araya Chaves
Fecha: 29/09/2026
Versión: 1.0
Descripción: Verifica si la nave posee suficiente combustible
para realizar el viaje de ida, regreso y mantener la reserva.
============================================================"""

# Declaración de constantes
RESERVA_COMBUSTIBLE = 10

# Entradas de datos
combustibleDisponible = int(input("Ingrese la cantidad de combustible disponible en la nave: "))

combustibleIda = int(input("Ingrese la cantidad de combustible necesario para el viaje de ida: "))

combustibleRegreso = int(input("Ingrese la cantidad de combustible necesario para el viaje de regreso: "))

# Procesamiento
combustibleTotal = combustibleIda + combustibleRegreso + RESERVA_COMBUSTIBLE 
combustibleExcedente = combustibleDisponible - combustibleTotal

# Advertencia si el margen adicional de combustible es bajo
if combustibleExcedente < 10:
    print("Advertencia: el margen adicional de combustible es bajo.")

# Salida de resultados
print(f"""
===== VERIFICACIÓN DE COMBUSTIBLE =====

Combustible disponible: {combustibleDisponible} unidades
Combustible necesario para el viaje de ida: {combustibleIda} unidades
Combustible necesario para el viaje de regreso: {combustibleRegreso} unidades
Reserva de combustible: {RESERVA_COMBUSTIBLE} unidades
Combustible total requerido: {combustibleTotal} unidades
Combustible adicional disponible: {combustibleExcedente} unidades
""")