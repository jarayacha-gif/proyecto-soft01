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

> **Rama de trabajo:** `Proyecto`. Esta es la rama principal utilizada para el desarrollo y la entrega del proyecto.

## Descripción general

**Misión Órbita** es un simulador desarrollado en Python que integra las etapas principales de una misión de exploración espacial. El sistema permite planificar una misión, seleccionar un destino, calcular y comprobar los recursos necesarios, ejecutar el viaje, realizar actividades científicas y gestionar el regreso de la tripulación.

La versión final reúne estos procesos en un solo programa con un menú principal. También permite consultar un historial de las misiones realizadas y visualizar un reporte con el resultado y los puntos científicos obtenidos.

Los destinos y los recursos utilizan valores ficticios definidos para el contexto académico del proyecto.

## Estado del proyecto

**Proyecto culminado — versión integrada final.**

El proyecto reúne los componentes trabajados durante los avances. Se conserva la documentación de las entregas anteriores y se incorpora una carpeta específica para el código y la documentación del proyecto terminado.

### Versión final — Sistema integrado

**Código principal:** `codigo de ejercicios/Proyecto_Terminado/Proyecto_terminado.py`

El programa integra los siguientes componentes:

| Componente | Funcionalidad |
| --- | --- |
| A. Preparación y autorización | Solicita los datos de la misión, muestra los destinos, calcula los recursos requeridos y determina si se puede autorizar el lanzamiento. |
| B. Viaje de ida | Calcula el consumo diario y descuenta los recursos correspondientes al trayecto hacia el destino. |
| C. Exploración y bitácora | Presenta actividades científicas, verifica los recursos necesarios, registra las actividades realizadas y acumula los puntos obtenidos. |
| D. Regreso y supervivencia | Comprueba si hay combustible para regresar, simula el trayecto de vuelta y estima la supervivencia cuando la tripulación queda varada. |
| E. Reporte final | Resume el resultado de la misión y muestra la bitácora de exploración ordenada de mayor a menor puntaje. |
| F. Menú e historial | Permite ejecutar nuevas misiones, consultar el historial ordenado por puntos y salir del sistema. |

**Destinos disponibles:** Luna, Marte y Europa.

**Actividades científicas:** analizar terreno, recolectar muestra, realizar observación y sobrevolar la zona. Cada actividad tiene un consumo de recursos y una puntuación definidos.

### Avance 1 — Planificación de la misión

Los ejercicios originales de planificación se encuentran en `codigo de ejercicios/avance_1/`:

| Archivo | Función |
| --- | --- |
| `ejercicio1Proyecto.py` | Calcula combustible para ida y regreso, reserva, oxígeno, energía y provisiones. |
| `ejercicio2Proyecto.py` | Calcula el combustible total requerido y advierte cuando el excedente es bajo. |
| `ejercicio3Proyecto.py` | Comprueba si el oxígeno y las provisiones cubren las necesidades de la tripulación. |
| `ejercicio4Proyecto.py` | Autoriza o rechaza el lanzamiento según la disponibilidad de los recursos. |

### Avance 2 — Ejecución de la misión

Los ejercicios documentados de este avance se encuentran en `codigo de ejercicios/avance_2/`:

| Archivo | Función |
| --- | --- |
| `ejercicio7_exploracion.py` | Administra las actividades científicas, descuenta energía y provisiones y acumula actividades, muestras y puntos. |
| `ejercicio8_regreso.py` | Evalúa el combustible para el regreso, simula el consumo durante el trayecto y calcula la supervivencia si la tripulación queda varada. |

Los ejercicios y componentes trabajados en las entregas se integran como parte del desarrollo que culmina en el sistema final.

## Organización del repositorio

```text
proyecto-soft01/
├── README.md
├── .gitignore
├── codigo de ejercicios/
│   ├── Proyecto_Terminado/
│   │   ├── Proyecto_Terminado.py
│   │   └── Proyecto_terminado.py
│   ├── avance_1/
│   │   ├── ejercicio1Proyecto.py
│   │   ├── ejercicio2Proyecto.py
│   │   ├── ejercicio3Proyecto.py
│   │   └── ejercicio4Proyecto.py
│   └── avance_2/
│       ├── ejercicio7_exploracion.py
│       └── ejercicio8_regreso.py
└── documentacion del proyecto/
    ├── Proyecto_Terminado/
    │   └── Proyecto_Terminado_Documentacion.pdf
    ├── avance_1/
    │   └── documentacion_proyecto_avance_1.pdf
    └── avance_2/
        ├── Ejercicio7_Avance2.pdf
        └── Ejercicio8_Avance2.pdf
```

> **Nota:** el repositorio contiene dos archivos con nombres muy similares dentro de la carpeta de la versión final. El archivo con la implementación integrada es `Proyecto_terminado.py`. El archivo `Proyecto_Terminado.py` aparece en el repositorio con un contenido prácticamente vacío.

## Requisitos

- Python 3.
- Visual Studio Code u otro editor de texto.
- Terminal o consola.

El sistema utiliza características incluidas en Python y no requiere instalar dependencias externas.

## Cómo clonar y ejecutar

Clonar el repositorio y entrar en su carpeta:

```bash
git clone https://github.com/jarayacha-gif/proyecto-soft01.git
cd proyecto-soft01
```

Para ejecutar la versión integrada desde la carpeta raíz:

```bash
python "codigo de ejercicios/Proyecto_Terminado/Proyecto_terminado.py"
```

En Windows también se puede utilizar `py`:

```bash
py "codigo de ejercicios/Proyecto_Terminado/Proyecto_terminado.py"
```

Los ejercicios de los avances pueden ejecutarse individualmente. Por ejemplo:

```bash
python "codigo de ejercicios/avance_1/ejercicio1Proyecto.py"
python "codigo de ejercicios/avance_2/ejercicio7_exploracion.py"
```

## Uso general del sistema final

Al iniciar, se presenta el menú principal de **Misión Órbita**:

1. **Planificar y ejecutar una misión:** solicita el nombre de la misión, la cantidad de tripulantes, el destino y los recursos disponibles. Si cumple los requisitos, continúa con el viaje, la exploración y el regreso.
2. **Ver historial de misiones:** muestra las misiones ejecutadas durante la sesión, ordenadas de mayor a menor según sus puntos científicos.
3. **Salir:** finaliza la ejecución del sistema.

Durante una misión, el programa muestra la disponibilidad de recursos, informa si el lanzamiento es autorizado, registra el consumo y las actividades científicas y presenta el resultado final. El historial se mantiene durante la ejecución actual del programa; no se almacena de forma permanente entre sesiones.

## Documentación académica

La documentación del proyecto se encuentra organizada junto con los archivos de código:

- [Documentación del proyecto terminado](documentacion%20del%20proyecto/Proyecto_Terminado/Proyecto_Terminado_Documentacion.pdf)
- [Documentación del Avance 1](documentacion%20del%20proyecto/avance_1/documentacion_proyecto_avance_1.pdf)
- [Documentación del Ejercicio 7 — Avance 2](documentacion%20del%20proyecto/avance_2/Ejercicio7_Avance2.pdf)
- [Documentación del Ejercicio 8 — Avance 2](documentacion%20del%20proyecto/avance_2/Ejercicio8_Avance2.pdf)

## Convenciones y enfoque de programación

El proyecto aplica los fundamentos de programación imperativa desarrollados durante el curso. En la versión integrada se utilizan variables descriptivas, constantes, estructuras condicionales, ciclos, listas, tuplas y funciones para organizar las responsabilidades del programa.

También se emplean acumuladores y contadores para registrar puntos, actividades y misiones, así como operaciones de ordenamiento para presentar la bitácora y el historial.

## Historial de desarrollo

El repositorio conserva los archivos de los avances y la versión integrada final, permitiendo consultar la evolución del proyecto mediante sus carpetas y el historial de commits de Git.

---

**Misión Órbita — SOFT-01, CENFOTEC · C3-2026**
