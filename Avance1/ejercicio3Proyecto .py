""" ============================================================
Archivo: ejercicio3_soporte_tripulacion.py
Curso: SOFT-01 Principios de Programación 1 - Sección SCV3
Integrante: Jehidam Araya Chaves
Fecha: 29/09/2026
Versión: 1.0
Descripción: Verifica si existen suficientes recursos de oxígeno
y provisiones para mantener a toda la tripulación durante el viaje.
============================================================"""

# Entradas de datos
oxigenoDisponible = int(input("Ingrese la cantidad de oxígeno disponible en la nave: "))
oxigenoNecesario = int(input("Ingrese la cantidad de oxígeno requerido para el viaje: "))
provisionesDisponibles = int(input("Ingrese la cantidad de provisiones disponibles en la nave: "))
provisionesNecesarias = int(input("Ingrese la cantidad de provisiones requeridas para el viaje: "))

# Verificación de recursos
if oxigenoDisponible >= oxigenoNecesario and provisionesDisponibles >= provisionesNecesarias:
    mensajeResultado = "La nave posee recursos suficientes para la tripulación."
else:
    mensajeResultado = "La nave no posee recursos suficientes para la tripulación."

# Salida de resultados
print(f"""
===== VERIFICACIÓN DEL SOPORTE PARA LA TRIPULACIÓN =====

Oxígeno disponible: {oxigenoDisponible} unidades
Oxígeno requerido: {oxigenoNecesario} unidades
Provisiones disponibles: {provisionesDisponibles} unidades
Provisiones requeridas: {provisionesNecesarias} unidades

{mensajeResultado}
""")