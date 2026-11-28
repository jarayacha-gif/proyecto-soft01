# Misión Órbita — Simulador de exploración espacial

## Descripción del proyecto

Misión Órbita es un simulador desarrollado en Python para gestionar una misión de exploración espacial. Permite planificar el lanzamiento, seleccionar un destino, calcular y verificar los recursos necesarios, simular el viaje, realizar actividades científicas, evaluar el regreso y consultar el historial de misiones.

El sistema utiliza valores ficticios de combustible, oxígeno, energía y provisiones con fines académicos.

## Información general

- **Universidad:** Universidad CENFOTEC
- **Curso:** SOFT-01 · Principios de Programación 1
- **Sección:** SCV6
- **Periodo:** C3-2026
- **Docente facilitadora:** Verónica Mora Lezcano
- **Integrante:** Jehidam Araya Chaves

## Archivos de la entrega — Avance 3

La entrega final se organiza con los nombres y las ubicaciones solicitadas:

- **Programa:** `avance3/mision_orbita.py`
- **Documentación PDF:** `documentacion/avance3_mision_orbita.pdf`

## Funcionalidades principales

| Componente | Funcionalidad |
| --- | --- |
| A. Preparación y autorización | Solicita los datos de la misión, calcula los recursos necesarios y determina si se autoriza el lanzamiento. |
| B. Viaje de ida | Calcula y descuenta el consumo de recursos durante el trayecto al destino. |
| C. Exploración y bitácora | Permite realizar actividades científicas, valida sus costos, registra los resultados y acumula puntos. |
| D. Regreso y supervivencia | Comprueba los recursos disponibles para el regreso y estima la supervivencia si la tripulación queda varada. |
| E. Reporte final | Presenta los datos de la misión y la bitácora ordenada por puntaje. |
| F. Menú e historial | Permite ejecutar misiones, consultar el historial ordenado por puntos y salir del sistema. |

**Destinos:** Luna, Marte y Europa.

**Actividades científicas:** analizar terreno, recolectar muestra, realizar observación y sobrevolar la zona.

## Convenciones y estilos de programación

El proyecto utiliza programación imperativa y sigue estas convenciones:

- Los nombres de variables y funciones utilizan `snake_case`, con palabras descriptivas en español.
- Las constantes se escriben en mayúsculas y separan palabras con guion bajo, por ejemplo `CONSUMO_COMBUSTIBLE_DIA`.
- La indentación utiliza cuatro espacios por nivel.
- Las funciones agrupan tareas específicas y emplean parámetros y valores de retorno cuando corresponde.
- Se utilizan comentarios y cadenas de documentación para explicar la intención de las funciones y las partes relevantes de la lógica.
- Las estructuras de control incluyen condicionales `if/elif/else` y ciclos `for` y `while`.
- Las estructuras de datos principales son listas, tuplas y listas anidadas para representar bitácoras e historial.
- Se emplean contadores y acumuladores para registrar actividades, puntos y misiones.

## Requisitos

- Python 3.
- Terminal o consola.
- Visual Studio Code u otro editor de código (opcional).

El programa utiliza módulos de la biblioteca estándar de Python y no requiere instalar dependencias externas.

## Instrucciones para ejecutar el sistema

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/jarayacha-gif/proyecto-soft01.git
   cd proyecto-soft01
   ```

2. Ejecutar el programa desde la carpeta raíz del repositorio:

   **Windows:**

   ```bash
   py avance3/mision_orbita.py
   ```

   **Linux, macOS o sistemas con el comando python:**

   ```bash
   python avance3/mision_orbita.py
   ```

Al iniciar, el sistema muestra el menú principal. Seleccione la opción para planificar y ejecutar una misión, consultar el historial o salir del programa.

## Organización del repositorio

```text
proyecto-soft01/
├── README.md
├── .gitignore
├── avance3/
│   └── mision_orbita.py
├── documentacion/
│   └── avance3_mision_orbita.pdf
├── codigo de ejercicios/
│   ├── avance_1/
│   └── avance_2/
└── documentacion del proyecto/
    ├── avance_1/
    └── avance_2/
```

Las carpetas de los avances anteriores se conservan como referencia del desarrollo. Los archivos de entrega del tercer avance se encuentran en `avance3/` y `documentacion/`.

## Corrección del reporte final

El reporte muestra los valores correspondientes al nombre, destino, resultado y puntos científicos de cada misión mediante interpolación de cadenas. El encabezado de la bitácora se presenta por separado.

---

**Misión Órbita — SOFT-01 · Universidad CENFOTEC · C3-2026**
