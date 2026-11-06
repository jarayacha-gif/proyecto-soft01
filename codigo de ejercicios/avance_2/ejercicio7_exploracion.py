# ============================================================
# Archivo: ejercicio7_exploracion.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrante registrado: Jehidam Araya Chaves
# Fecha: 31/10/2026         Versión: 1.0
# ============================================================

# Declaración de constantes
# Cantidad de energía, provisiones y puntos que se consumen o ganan por cada actividad
ENERGIA_ANALIZAR = 8
ENERGIA_MUESTRA = 12
ENERGIA_OBSERVACION = 5

PROVISIONES_ANALIZAR = 0
PROVISIONES_MUESTRA = 2
PROVISIONES_OBSERVACION = 0

PUNTOS_ANALIZAR = 10
PUNTOS_MUESTRA = 20
PUNTOS_OBSERVACION = 8

# Entrada de datos
energiaDisponible = int(input("Ingrese la energía disponible al llegar al destino: "))
provisionesDisponibles = int(input("Ingrese la cantidad de provisiones disponibles al llegar al destino: "))

# Inicialización de contadores y acumuladores
puntosCientificos = 0
actividadesRealizadas = 0
muestrasRecolectadas = 0

# Inicialización de la variable de control
continuarExploracion = True

# Procesamiento: menú de actividades
while continuarExploracion:

    opcion = int(input("""
        ----- Menú de actividades -----

1. Analizar terreno     | E: -8  | p: 0 | Pts: +10 |

2. Recolectar muestra   | E: -12 | p: 2 | Pts: +20 |

3. Realizar observación | E: -5  | p: 0 | Pts: +8  |

4. Finalizar exploración|   Resultados Obtenidos   |

Seleccione una actividad: """))

    # Decisión: analizar terreno
    if opcion == 1:

        if energiaDisponible >= ENERGIA_ANALIZAR and provisionesDisponibles >= PROVISIONES_ANALIZAR:

            energiaDisponible -= ENERGIA_ANALIZAR
            provisionesDisponibles -= PROVISIONES_ANALIZAR
            puntosCientificos += PUNTOS_ANALIZAR
            actividadesRealizadas += 1

            print(f"Actividad realizada: Analizar terreno. Puntos obtenidos: {PUNTOS_ANALIZAR}")

        else:
            print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
            continuarExploracion = False

    # Decisión: recolectar muestra
    elif opcion == 2:

        if energiaDisponible >= ENERGIA_MUESTRA and provisionesDisponibles >= PROVISIONES_MUESTRA:

            energiaDisponible -= ENERGIA_MUESTRA
            provisionesDisponibles -= PROVISIONES_MUESTRA
            puntosCientificos += PUNTOS_MUESTRA
            actividadesRealizadas += 1
            muestrasRecolectadas += 1

            print(f"Actividad realizada: Recolectar muestra. Puntos obtenidos: {PUNTOS_MUESTRA}")

        else:
            print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
            continuarExploracion = False

    # Decisión: realizar observación
    elif opcion == 3:

        if energiaDisponible >= ENERGIA_OBSERVACION and provisionesDisponibles >= PROVISIONES_OBSERVACION:

            energiaDisponible -= ENERGIA_OBSERVACION
            provisionesDisponibles -= PROVISIONES_OBSERVACION
            puntosCientificos += PUNTOS_OBSERVACION
            actividadesRealizadas += 1

            print(f"Actividad realizada: Realizar observación. Puntos obtenidos: {PUNTOS_OBSERVACION}")

        else:
            print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
            continuarExploracion = False

    # Decisión: finalizar exploración
    elif opcion == 4:

        print("Exploración finalizada por la tripulación.")
        continuarExploracion = False

    # Validación de opciones del menú
    else:
        print("Opción no válida.")

# Salida de resultados
print(f"""

----- Resultados de la exploración -----


Actividades realizadas: {actividadesRealizadas}

Muestras recolectadas: {muestrasRecolectadas}

Puntos científicos: {puntosCientificos}

Energía restante: {energiaDisponible} unidades

Provisiones restantes: {provisionesDisponibles} unidades

""")