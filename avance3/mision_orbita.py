# ============================================================
# Archivo: proyecto_terminado.py
# Curso: SOFT-01 Principios de Programacion 1 - Seccion SCV6
# Integrantes: Jehidam Araya Chaves
# Fecha: 17/11/2026 - Version: 1.0
# Descripción: Sistema integrado Misión Órbita.
# Alcance: Grupos de 1 o 2 personas.
# ============================================================


# ------------------------------------------------------------
# CONSTANTES DEL SISTEMA
# ------------------------------------------------------------

# Cada destino contiene: (nombre, días de viaje de ida).
DESTINOS = (("Luna", 3), ("Marte", 5), ("Europa", 7))

# Cada actividad contiene: (nombre, combustible, energia, provisiones, puntos).
ACTIVIDADES = (
    ("Analizar terreno", 0, 8, 0, 10),
    ("Recolectar muestra", 0, 12, 2, 20),
    ("Realizar observación", 0, 5, 0, 8),
    ("Sobrevolar la zona", 15, 3, 0, 25)
)

RECURSOS = ("combustible", "oxígeno", "energía", "provisiones")
RECURSOS_VITALES = ("oxígeno", "energía", "provisiones")
RESULTADOS = (
    "Regreso exitoso",
    "Regreso interrumpido",
    "Tripulación varada",
    "No autorizada",
    "No planificada"
)

# Columnas de DESTINOS: (nombre, dias).
DES_NOMBRE = 0
DES_DIAS = 1

# Columnas de ACTIVIDADES: (nombre, combustible, energia, provisiones, puntos).
ACT_NOMBRE = 0
ACT_COMBUSTIBLE = 1
ACT_ENERGIA = 2
ACT_PROVISIONES = 3
ACT_PUNTOS = 4

# Posicion de cada recurso en las listas recursos, requeridos y consumo.
COMBUSTIBLE = 0
OXIGENO = 1
ENERGIA = 2
PROVISIONES = 3

# Columnas de la matriz bitacora: [numero, actividad, puntos].
BIT_NUMERO = 0
BIT_ACTIVIDAD = 1
BIT_PUNTOS = 2

# Columnas de la matriz historial: [numero, nombre, destino, resultado, puntos].
MIS_NUMERO = 0
MIS_NOMBRE = 1
MIS_DESTINO = 2
MIS_RESULTADO = 3
MIS_PUNTOS = 4

# Constantes numericas utilizadas en las formulas.
TRAYECTO_VUELTA = 2
RESERVA_COMBUSTIBLE = 10
CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO_TRIPULANTE_DIA = 2
RESERVA_OXIGENO = 5
CONSUMO_ENERGIA_DIA = 5
RESERVA_ENERGIA = 10
CONSUMO_PROVISIONES_TRIPULANTE_DIA = 1
RESERVA_PROVISIONES = 3
MARGEN_MINIMO_COMBUSTIBLE = 10


# ------------------------------------------------------------
# COMPONENTE A: PREPARACION Y AUTORIZACION
# ------------------------------------------------------------

def mostrar_destinos():
    """Muestra los destinos disponibles y la duracion de cada viaje."""
    print("Destinos disponibles:")

    for i in range(len(DESTINOS)):
        print(
            f"{i + 1}. {DESTINOS[i][DES_NOMBRE]} "
            f"({DESTINOS[i][DES_DIAS]} días)")


def leer_recursos():
    """Solicita y devuelve los cuatro recursos disponibles de la nave."""
    recursos = []

    for nombre_recurso in RECURSOS:
        cantidad = int(input(f"Cantidad disponible de {nombre_recurso}: "))
        recursos.append(cantidad)

    return recursos


def calcular_requeridos(dias_viaje, tripulantes):
    """Calcula los recursos necesarios para la ida, el regreso y las reservas."""
    # El combustible se calcula para la ida y la vuelta; por eso se multiplica por 2.
    # Al final se suma una reserva para cubrir un margen adicional.
    combustible_requerido = (dias_viaje * CONSUMO_COMBUSTIBLE_DIA * TRAYECTO_VUELTA + RESERVA_COMBUSTIBLE)

    # El oxígeno depende de los días y de la cantidad de tripulantes.
    # La misma fórmula contempla ambos trayectos y agrega una reserva.
    oxigeno_requerido = ( dias_viaje * CONSUMO_OXIGENO_TRIPULANTE_DIA * TRAYECTO_VUELTA * tripulantes + RESERVA_OXIGENO)

    # La energía se calcula por día de viaje, sin multiplicarla por tripulantes.
    energia_requerida = ( dias_viaje * CONSUMO_ENERGIA_DIA * TRAYECTO_VUELTA + RESERVA_ENERGIA )

    # Las provisiones sí aumentan según el número de personas a bordo.
    provisiones_requeridas = ( dias_viaje * tripulantes * TRAYECTO_VUELTA + RESERVA_PROVISIONES )

    # Este orden debe coincidir con las posiciones definidas en RECURSOS.
    requeridos = [ combustible_requerido, oxigeno_requerido, energia_requerida, provisiones_requeridas]

    return requeridos


def mostrar_resumen(nombre_mision, nombre_destino, dias_viaje, tripulantes, disponibles, requeridos):
    """Muestra los datos de la mision y compara recursos disponibles y requeridos."""
    # El margen muestra cuánto combustible queda por encima del mínimo calculado.
    margen_combustible = disponibles[COMBUSTIBLE] - requeridos[COMBUSTIBLE]

    print(f""" Misión: {nombre_mision}
    Destino: {nombre_destino}
    Duración del viaje de ida: {dias_viaje} días
    Tripulantes: {tripulantes}""")

    for i in range(len(RECURSOS)):
        print(
            f"""{RECURSOS[i].capitalize()}: disponible {disponibles[i]} | requerido {requeridos[i]}""")

    print(f"Margen adicional de combustible: {margen_combustible} unidades")

    if margen_combustible < MARGEN_MINIMO_COMBUSTIBLE:
        print("Advertencia: el margen adicional de combustible es bajo.")


def autorizar_lanzamiento(disponibles, requeridos):
    """Devuelve True solo cuando todos los recursos alcanzan para la mision."""
    # La misión comienza autorizada; basta que un recurso sea insuficiente para rechazarla.
    autorizado = True

    for i in range(len(RECURSOS)):
        if disponibles[i] < requeridos[i]:
            autorizado = False

    if autorizado:
        print("Lanzamiento autorizado.")
    else:
        print("Lanzamiento no autorizado. La misión debe ser revisada.")

    return autorizado


# ------------------------------------------------------------
# COMPONENTE B: VIAJE DE IDA
# ------------------------------------------------------------

def calcular_consumo_diario(tripulantes):
    """Devuelve el consumo de un dia para combustible, oxigeno, energia y provisiones."""
    # Se construye el consumo diario en el mismo orden de la lista RECURSOS.
    # Oxígeno y provisiones se multiplican por la cantidad de tripulantes.
    consumo = [
        CONSUMO_COMBUSTIBLE_DIA,
        CONSUMO_OXIGENO_TRIPULANTE_DIA * tripulantes,
        CONSUMO_ENERGIA_DIA,
        CONSUMO_PROVISIONES_TRIPULANTE_DIA * tripulantes
    ]

    return consumo


def viajar_al_destino(recursos, dias_viaje, tripulantes):
    """Descuenta directamente el consumo de todos los dias del viaje de ida."""

    consumo = calcular_consumo_diario(tripulantes)

    # Se descuenta de una vez el consumo de todos los días de ida.
    for i in range(len(RECURSOS)):
        recursos[i] -= consumo[i] * dias_viaje

    return recursos


def recursos_alcanzan(recursos, consumo):
    """Indica si cada recurso disponible alcanza para un dia de trayecto."""
    # Se revisan todos los recursos antes de permitir que avance un día.
    alcanza = True

    for i in range(len(RECURSOS)):
        if recursos[i] < consumo[i]:
            alcanza = False

    return alcanza


def simular_trayecto(recursos, dias, tripulantes):
    """Simula un trayecto dia por dia y devuelve los dias completados."""
    consumo = calcular_consumo_diario(tripulantes)
    dias_completados = 0
    puede_continuar = True

    # El trayecto avanza mientras falten días y todos los recursos permitan continuar.
    while dias_completados < dias and puede_continuar:
        if recursos_alcanzan(recursos, consumo):
            # Solo después de comprobar los recursos se descuenta el consumo del día.
            for i in range(len(RECURSOS)):
                recursos[i] -= consumo[i]

            dias_completados += 1

            print( f"Día {dias_completados} | Combustible: {recursos[COMBUSTIBLE]} | Oxígeno: {recursos[OXIGENO]} | Energía: {recursos[ENERGIA]} | Provisiones: {recursos[PROVISIONES]}")
        else:
            # Si algún recurso no alcanza, se detiene el trayecto sin descontar ese día.
            puede_continuar = False

    return dias_completados


def mostrar_recursos(recursos):
    """Muestra los recursos que quedan en la nave."""
    print("Recursos restantes:")

    for i in range(len(RECURSOS)):
        print(f"- {RECURSOS[i].capitalize()}: {recursos[i]} unidades")


# ------------------------------------------------------------
# COMPONENTE C: EXPLORACION CON BITACORA
# ------------------------------------------------------------

def mostrar_menu_actividades():
    """Muestra las cuatro actividades y la opcion para finalizar."""
    for i in range(len(ACTIVIDADES)):
        print(f"{i + 1}. {ACTIVIDADES[i][ACT_NOMBRE]}")

    print(f"{len(ACTIVIDADES) + 1}. Finalizar exploración")


def explorar(recursos):
    """Permite realizar actividades, descontar recursos y registrar la bitacora."""
    # La bitácora guarda únicamente las actividades realizadas durante esta exploración.
    bitacora = []
    continuar = True

    print("=== EXPLORACIÓN ===")

    while continuar:
        mostrar_menu_actividades()
        opcion = int(input("Seleccione una actividad: "))

        if opcion == len(ACTIVIDADES) + 1:
            print("Exploración finalizada por la tripulación.")
            continuar = False

        elif opcion < 1 or opcion > len(ACTIVIDADES):
            print("Opción no válida.")

        else:
            # El menú muestra opciones desde 1, pero las posiciones de una tupla comienzan en 0.
            actividad = ACTIVIDADES[opcion - 1]

            # Se comprueban solo los recursos que consume la actividad seleccionada.
            recursos_suficientes = (
                recursos[COMBUSTIBLE] >= actividad[ACT_COMBUSTIBLE]
                and recursos[ENERGIA] >= actividad[ACT_ENERGIA]
                and recursos[PROVISIONES] >= actividad[ACT_PROVISIONES] )

            if recursos_suficientes:
                recursos[COMBUSTIBLE] -= actividad[ACT_COMBUSTIBLE]
                recursos[ENERGIA] -= actividad[ACT_ENERGIA]
                recursos[PROVISIONES] -= actividad[ACT_PROVISIONES]

                # Se registra el número consecutivo, el nombre y los puntos de la actividad.
                bitacora.append([
                    len(bitacora) + 1,
                    actividad[ACT_NOMBRE],
                    actividad[ACT_PUNTOS] ])

                print( f"Actividad realizada: {actividad[ACT_NOMBRE]}. Puntos obtenidos: {actividad[ACT_PUNTOS]}")
            else:
                # No se registra la actividad porque no llegó a ejecutarse.
                print("Recursos insuficientes para realizar la actividad. La exploración finaliza.")
                continuar = False

    return bitacora


def contar_actividad(bitacora, nombre_actividad):
    """Cuenta las filas de la bitacora que coinciden con una actividad."""
    cantidad = 0

    # Se compara el nombre de cada fila para contar solo la actividad solicitada.
    for fila in bitacora:
        if fila[BIT_ACTIVIDAD] == nombre_actividad:
            cantidad += 1

    return cantidad


def calcular_puntos(bitacora):
    """Suma los puntos de todas las actividades registradas en la bitacora."""
    puntos_totales = 0

    # Se acumulan los puntos almacenados en la columna correspondiente de cada fila.
    for fila in bitacora:
        puntos_totales += fila[BIT_PUNTOS]

    return puntos_totales


def mostrar_resumen_exploracion(bitacora, recursos):
    """Muestra actividades, muestras, puntos y recursos restantes."""
    muestras = contar_actividad(bitacora, "Recolectar muestra")
    puntos = calcular_puntos(bitacora)

    print(f"""Actividades realizadas: {len(bitacora)}
    Muestras recolectadas: {muestras}
    Puntos científicos: {puntos}""")

    mostrar_recursos(recursos)


# ------------------------------------------------------------
# COMPONENTE D: REGRESO Y SUPERVIVENCIA
# ------------------------------------------------------------

def puede_regresar(recursos, dias_viaje):
    """Comprueba si hay combustible para iniciar el viaje de regreso."""
    combustible_suficiente = (
        recursos[COMBUSTIBLE]
        >= dias_viaje * CONSUMO_COMBUSTIBLE_DIA )

    return combustible_suficiente


def calcular_supervivencia(recursos, tripulantes):
    """Calcula los dias completos de supervivencia por cada recurso vital."""
    dias_por_recurso = []

    # La división entera // calcula días completos de supervivencia, sin contar fracciones.
    dias_oxigeno = (recursos[OXIGENO] // (tripulantes * CONSUMO_OXIGENO_TRIPULANTE_DIA) )
    dias_energia = recursos[ENERGIA] // CONSUMO_ENERGIA_DIA
    dias_provisiones = (recursos[PROVISIONES] // (tripulantes * CONSUMO_PROVISIONES_TRIPULANTE_DIA) )

    dias_por_recurso.append(dias_oxigeno)
    dias_por_recurso.append(dias_energia)
    dias_por_recurso.append(dias_provisiones)

    return dias_por_recurso


def obtener_limitantes(dias_por_recurso, minimo):
    """Devuelve los recursos vitales que tienen el menor numero de dias."""
    limitantes = []

    # Puede haber empate: se conservan todos los recursos que limitan la supervivencia.
    for i in range(len(dias_por_recurso)):
        if dias_por_recurso[i] == minimo:
            limitantes.append(RECURSOS_VITALES[i])

    return limitantes


def regresar(recursos, dias_viaje, tripulantes):
    """Ejecuta el regreso o calcula la supervivencia si no hay combustible."""
    print("=== REGRESO ===")

    # Primero se verifica el combustible total necesario para iniciar el regreso.
    if puede_regresar(recursos, dias_viaje):
        dias_completados = simular_trayecto(recursos, dias_viaje, tripulantes)

        if dias_completados == dias_viaje:
            print("La tripulación regresó exitosamente a la Tierra.")
            mostrar_recursos(recursos)
            resultado = "Regreso exitoso"
        else:
            print(f"El regreso se interrumpió en el día {dias_completados + 1}.")

            consumo = calcular_consumo_diario(tripulantes)

            # Se identifican los recursos que impidieron completar el siguiente día.
            for i in range(len(RECURSOS)):
                if recursos[i] < consumo[i]:
                    print(f"Recurso insuficiente: {RECURSOS[i]}")

            print("La tripulación no completó el regreso.")
            resultado = "Regreso interrumpido"
    else:
        print("La tripulación quedó varada en el destino.")

        # Sin combustible suficiente, se estima cuánto tiempo puede sobrevivir la tripulación.
        dias_por_recurso = calcular_supervivencia(recursos, tripulantes)

        for i in range(len(RECURSOS_VITALES)):
            print(f"Días por {RECURSOS_VITALES[i]}: {dias_por_recurso[i]}")

        # El recurso con menos días disponibles determina el límite de supervivencia.
        minimo = min(dias_por_recurso)
        limitantes = obtener_limitantes(dias_por_recurso, minimo)
        nombres_limitantes = ", ".join(limitantes)

        print(f""""Supervivencia estimada: {minimo} días
        Recurso(s) limitante(s): {nombres_limitantes}""")

        resultado = "Tripulación varada"

    return resultado


# ------------------------------------------------------------
# COMPONENTE E: REPORTE FINAL ORDENADO
# ------------------------------------------------------------

def obtener_puntos_actividad(fila):
    """Devuelve el puntaje almacenado en una fila de la bitacora."""
    puntos = fila[BIT_PUNTOS]

    return puntos


def ordenar_bitacora(bitacora):
    """Devuelve una copia de la bitacora ordenada por puntos, de mayor a menor."""
    # sorted() crea una copia ordenada y conserva intacta la bitácora original.
    bitacora_ordenada = sorted(
        bitacora,
        key=obtener_puntos_actividad,
        reverse=True
    )

    return bitacora_ordenada


def mostrar_reporte(mision, bitacora):
    """Muestra el resultado de la mision y su bitacora ordenada."""
    print(f"""=== REPORTE FINAL ===
    Misión: {mision[MIS_NOMBRE]}
    Destino: {mision[MIS_DESTINO]}
    Resultado: {mision[MIS_RESULTADO]}
    Puntos científicos: {mision[MIS_PUNTOS]}""")

    print("Bitácora de exploración (de mayor a menor puntaje):")

    # Si no hubo exploración, se informa y se evita intentar ordenar una lista vacía.
    if len(bitacora) == 0:
        print("Sin actividades registradas.")
    else:
        bitacora_ordenada = ordenar_bitacora(bitacora)

        for fila in bitacora_ordenada:
            print(f"#{fila[BIT_NUMERO]} {fila[BIT_ACTIVIDAD]} - {fila[BIT_PUNTOS]} puntos")


# ------------------------------------------------------------
# FUNCION QUE COORDINA LA MISION COMPLETA
# ------------------------------------------------------------

def ejecutar_mision(numero):
    """Coordina planificacion, autorizacion, viaje, exploracion y regreso."""
    print("=== PLANIFICACIÓN ===")

    nombre_mision = input("Nombre de la misión: ")
    tripulantes = int(input("Cantidad de tripulantes: "))

    mostrar_destinos()
    opcion_destino = int(input("Seleccione un destino: "))

    # Se inicializan estos datos para cubrir misiones no planificadas.
    nombre_destino = "Ninguno"
    resultado = "No planificada"
    bitacora = []

    # Se valida la opción antes de acceder a la tupla de destinos.
    if opcion_destino < 1 or opcion_destino > len(DESTINOS):
        print("Opción de destino no válida. La misión no puede planificarse.")
    else:
        # Se resta 1 porque la opción del menú comienza en 1 y el índice en 0.
        destino = DESTINOS[opcion_destino - 1]
        nombre_destino = destino[DES_NOMBRE]
        dias_viaje = destino[DES_DIAS]

        disponibles = leer_recursos()
        requeridos = calcular_requeridos(dias_viaje, tripulantes)
        autorizado = autorizar_lanzamiento(disponibles, requeridos)
       
        mostrar_resumen(nombre_mision,nombre_destino,dias_viaje,tripulantes,disponibles,requeridos )
        

        if autorizado:
            # El alcance de grupos de 1 o 2 personas descuenta la ida directamente.
            print("=== VIAJE DE IDA ===")
            # A partir de aquí se trabaja con los recursos ya descontados por el viaje de ida.
            recursos_actualizados = viajar_al_destino(disponibles,dias_viaje,tripulantes)

            print(f"La nave llegó a {nombre_destino} en {dias_viaje} días.")
            mostrar_recursos(recursos_actualizados)

            # La exploracion modifica la misma lista de recursos.
            # La exploración recibe la misma lista para conservar los descuentos de recursos.
            bitacora = explorar(recursos_actualizados)
            mostrar_resumen_exploracion(bitacora, recursos_actualizados)

            # El resultado de regresar se conserva para el reporte final.
            resultado = regresar(recursos_actualizados,dias_viaje,tripulantes)
        else:
            resultado = "No autorizada"

    # Componente E: se crea y devuelve una fila para el historial.
    # Aunque la misión no se autorice, se genera un registro con los datos que sí existen.
    puntos_totales = calcular_puntos(bitacora)
    mision = [numero, nombre_mision, nombre_destino, resultado, puntos_totales]

    mostrar_reporte(mision, bitacora)

    return mision


# ------------------------------------------------------------
# COMPONENTE F: MENU PRINCIPAL E HISTORIAL DE MISIONES
# ------------------------------------------------------------

def mostrar_menu_principal():
    """Muestra el menu principal para grupos de una o dos personas."""
    print("""===== MISIÓN ÓRBITA =====
    1. Planificar y ejecutar una misión
    2. Ver historial de misiones
    3. Salir""")


def obtener_puntos_mision(mision):
    """Devuelve los puntos de una fila del historial."""
    puntos = mision[MIS_PUNTOS]

    return puntos


def ordenar_historial(historial):
    """Devuelve una copia del historial ordenada por puntos, de mayor a menor."""
    # Se ordena una copia para mostrar el ranking sin cambiar el historial de registro.
    historial_ordenado = sorted(
        historial,
        key=obtener_puntos_mision,
        reverse=True
    )

    return historial_ordenado


def linea_mision(mision):
    """Devuelve la representacion de una mision en una sola linea."""
    linea = (
        f"#{mision[MIS_NUMERO]} {mision[MIS_NOMBRE]} | "
        f"{mision[MIS_DESTINO]} | {mision[MIS_RESULTADO]} | "
        f"{mision[MIS_PUNTOS]} puntos"
    )

    return linea


def mostrar_historial(historial):
    """Muestra las misiones registradas, ordenadas por puntaje descendente."""
    print("=== HISTORIAL DE MISIONES ===")

    # Se verifica si hay misiones antes de recorrer el historial.
    if len(historial) == 0:
        print("No hay misiones registradas.")
    else:
        historial_ordenado = ordenar_historial(historial)

        for mision in historial_ordenado:
            print(linea_mision(mision))


# ------------------------------------------------------------
# FUNCION PRINCIPAL: ADMINISTRA EL CICLO DEL SISTEMA
# ------------------------------------------------------------

def main():
    """Crea el historial y controla las opciones del menu principal."""
    historial = []
    continuar = True

    # El menú se repite hasta que la persona seleccione la opción de salir.
    while continuar:
        mostrar_menu_principal()
        opcion = int(input("Seleccione una opción: "))

        if opcion == 1:
            # El número de misión se calcula con el tamaño actual del historial.
            mision = ejecutar_mision(len(historial) + 1)
            historial.append(mision)
        elif opcion == 2:
            mostrar_historial(historial)
        elif opcion == 3:
            continuar = False
            print("Fin del sistema Misión Órbita.")
        else:
            print("Opción no válida.")


# Llamada al programa principal: debe ser la ultima linea del archivo.
main()
