# Misión Órbita — Simulador de exploración espacial

## Información del proyecto

- **Universidad:** CENFOTEC
- **Escuela:** Ingeniería del Software
- **Curso:** Principios de Programación 1
- **Código:** SOFT-01
- **Sección:** SCV6
- **Periodo:** C3-2026
- **Docente:** Verónica Mora Lezcano
- **Integrante registrado:** Jehidam Araya Chaves

> **Rama de revisión:** `Proyecto`. Esta es la rama principal de trabajo del repositorio; no confundir con `main`.

## Descripción

**Misión Órbita** es un proyecto académico desarrollado en Python que representa, mediante programas independientes, la planificación y ejecución de una misión de exploración espacial. El simulador calcula recursos, verifica condiciones para el lanzamiento, registra el consumo de recursos durante el viaje, administra actividades científicas y evalúa el regreso o la supervivencia de la tripulación.

Los valores de combustible, oxígeno, energía y provisiones son unidades ficticias establecidas por la consigna del curso. El proyecto se desarrolla progresivamente en entregas separadas.

## Estado de los avances

### Avance 1 — Planificación de la misión

Los programas del primer avance están en `codigo de ejercicios/avance_1/`:

| Archivo | Función |
| --- | --- |
| `ejercicio1Proyecto.py` | Calcula combustible para ida y regreso, reserva, oxígeno, energía y provisiones. |
| `ejercicio2Proyecto.py` | Calcula el combustible total requerido y muestra una advertencia cuando el excedente es bajo. |
| `ejercicio3Proyecto.py` | Verifica si el oxígeno y las provisiones cubren las necesidades de la tripulación. |
| `ejercicio4Proyecto.py` | Autoriza o rechaza el lanzamiento según la disponibilidad de los cuatro recursos. |

### Avance 2 — Ejecución de la misión

Los programas disponibles de este avance están en `codigo de ejercicios/avance_2/`:

| Ejercicio | Archivo | Función |
| --- | --- | --- |
| 7 | `ejercicio7_exploracion.py` | Presenta un menú de actividades científicas, descuenta energía y provisiones, y acumula actividades, muestras y puntos. |
| 8 | `ejercicio8_regreso.py` | Evalúa si hay combustible para iniciar el regreso, simula el consumo diario y calcula la supervivencia cuando la tripulación queda varada. |

**Pendiente de incorporar al repositorio:** los ejercicios 5 (selección del destino y autorización) y 6 (simulación del viaje hacia el destino). La consigna asigna los ejercicios 5, 6, 7 y 8 a grupos de tres integrantes; los ejercicios 7 y 8 por sí solos corresponden al alcance individual.

## Organización del repositorio

```text
proyecto-soft01/
├── README.md
├── .gitignore
├── codigo de ejercicios/
│   ├── avance_1/
│   │   ├── ejercicio1Proyecto.py
│   │   ├── ejercicio2Proyecto.py
│   │   ├── ejercicio3Proyecto.py
│   │   └── ejercicio4Proyecto.py
│   └── avance_2/
│       ├── ejercicio7_exploracion.py
│       └── ejercicio8_regreso.py
└── documentacion del proyecto/
    ├── avance_1/
    │   └── documentacion_proyecto_avance_1.pdf
    └── avance_2/
        ├── ejercicio7_avance_2.pdf
        └── Ejercicio8_Avance2.pdf
```

## Requisitos

- Python 3.
- Visual Studio Code u otro editor de texto.
- Terminal o consola.

No se requieren dependencias externas. Los programas se ejecutan individualmente y leen los datos mediante consola.

## Cómo clonar y ejecutar

Clonar el repositorio:

```bash
git clone https://github.com/jarayacha-gif/proyecto-soft01.git
cd proyecto-soft01
```

Ejecutar los programas disponibles desde la carpeta raíz:

```bash
python "codigo de ejercicios/avance_1/ejercicio1Proyecto.py"
python "codigo de ejercicios/avance_1/ejercicio2Proyecto.py"
python "codigo de ejercicios/avance_1/ejercicio3Proyecto.py"
python "codigo de ejercicios/avance_1/ejercicio4Proyecto.py"
python "codigo de ejercicios/avance_2/ejercicio7_exploracion.py"
python "codigo de ejercicios/avance_2/ejercicio8_regreso.py"
```

En Windows también se puede utilizar `py` en lugar de `python`. Por ejemplo:

```bash
py "codigo de ejercicios/avance_2/ejercicio8_regreso.py"
```

## Convenciones y restricciones de programación

El proyecto sigue el enfoque imperativo y los contenidos trabajados en el curso:

- Variables descriptivas en `snake_case` o `camelCase`.
- Constantes en mayúsculas con guion bajo.
- Indentación uniforme de cuatro espacios.
- Entrada y salida mediante `input()` y `print()`.
- Decisiones con `if`, `elif` y `else`.
- Ciclos `while` y `for` con `range()`, contadores, acumuladores y variables de control.
- Sin funciones propias (`def`), colecciones, librerías externas, archivos, JSON ni programación orientada a objetos, según las restricciones del avance.

## Documentación académica

- [Documentación del Avance 1](documentacion%20del%20proyecto/avance_1/documentacion_proyecto_avance_1.pdf)
- [Documentación del Ejercicio 7 — Avance 2](documentacion%20del%20proyecto/avance_2/ejercicio7_avance_2.pdf)
- [Documentación del Ejercicio 8 — Avance 2](documentacion%20del%20proyecto/avance_2/Ejercicio8_Avance2.pdf)

La consigna del segundo avance solicita, para cada ejercicio asignado, tabla de variables, diagrama de flujo, código Python, al menos tres casos de prueba documentados y evidencia de ejecución en consola. Se recomienda revisar esos elementos en cada PDF antes de entregar.

## Historial de versiones

El desarrollo se registra mediante commits en Git. La consigna solicita al menos ocho commits significativos distribuidos en tres días diferentes, mensajes descriptivos y participación de todos los integrantes. El historial de esta rama muestra actividad progresiva en septiembre, octubre y noviembre de 2026.

## Alcance y estado de entrega

Este README documenta los archivos que actualmente están versionados en la rama `Proyecto`. No declara como completados entregables que todavía no aparecen en el árbol del repositorio. Antes de la entrega final se debe:

1. Incorporar los ejercicios 5 y 6 si el equipo es de tres integrantes.
2. Confirmar que cada PDF del avance 2 incluya tablas de variables, diagramas completos, código, casos de prueba y capturas legibles.
3. Sustituir los marcadores de integrantes en los encabezados de los ejercicios 7 y 8 por los nombres reales del equipo.
4. Indicar esta rama (`Proyecto`) en la portada del PDF que se subirá a Moodle.
