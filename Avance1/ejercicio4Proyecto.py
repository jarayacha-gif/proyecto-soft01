""" ============================================================
Archivo: ejercicio4Proyecto.py
Curso: SOFT-01 Principios de Programación 1 - Sección SCV3
Integrante: Jehidam Araya Chaves
Fecha: 29/09/2026
Versión: 1.0
Descripción: Verifica si una misión cumple con todos los recursos
necesarios para autorizar el lanzamiento.
============================================================"""

# Constantes
RESERVA_COMBUSTIBLE = 10

# Entrada de datos
combustibleDisponible = int(input("Ingrese la cantidad de combustible disponible en la nave: "))
combustibleIda = int(input("Ingrese la cantidad de combustible necesario para el viaje de ida: "))
combustibleRegreso = int(input("Ingrese la cantidad de combustible necesario para el viaje de regreso: "))
oxigenoDisponible = int(input("Ingrese la cantidad de oxígeno disponible en la nave: "))
oxigenoNecesario = int(input("Ingrese la cantidad de oxígeno requerido para el viaje: "))
energiaDisponible = int(input("Ingrese la cantidad de energía disponible en la nave: "))
energiaNecesaria = int(input("Ingrese la cantidad de energía requerida para el viaje: "))
provisionesDisponibles = int(input("Ingrese la cantidad de provisiones disponibles en la nave: "))
provisionesNecesarias = int(input("Ingrese la cantidad de provisiones requeridas para el viaje: "))

# Procesamiento
combustibleNecesario = combustibleIda + combustibleRegreso + RESERVA_COMBUSTIBLE

# Verificación de recursos
if combustibleDisponible >= combustibleNecesario and oxigenoDisponible >= oxigenoNecesario and energiaDisponible >= energiaNecesaria and provisionesDisponibles >= provisionesNecesarias:
    print("Lanzamiento autorizado.")
else:
    print("Lanzamiento no autorizado. La misión debe ser revisada.")