# Misión Órbita — Actualizaciones del segundo avance

## Información del proyecto

- **Curso:** Principios de Programación 1
- **Código:** SOFT-01
- **Estudiante:** Jehidam Araya Chaves
- **Docente:** Verónica Mora Lezcano

## Descripción

Este repositorio contiene el desarrollo del proyecto **Misión Órbita**, realizado en Python para el curso Principios de Programación 1.

En esta versión se incorporan **actualizaciones correspondientes al segundo avance del proyecto**. Se conserva el trabajo inicial de planificación y verificación de recursos de la misión, y se agrega una simulación de exploración científica en la que la tripulación administra sus recursos y realiza distintas actividades.

## Organización del repositorio

```text
proyecto-soft01/
├── README.md
├── .gitignore
├── src/
│   ├── avance_1/
│   │   ├── ejercicio1Proyecto.py
│   │   ├── ejercicio2Proyecto.py
│   │   ├── ejercicio3Proyecto.py
│   │   └── ejercicio4Proyecto.py
│   └── avance_2/
│       └── ejercicio7_exploracion.py
└── docs/
    ├── avance_1/
    │   └── documentacion_proyecto_avance_1.pdf
    └── avance_2/
        └── ejercicio7_avance_2.pdf
```

- **`src/`** contiene los programas de Python, separados por avance.
- **`docs/`** reúne los documentos PDF de cada avance.
- **`.gitignore`** excluye archivos temporales y entornos virtuales que no deben formar parte del repositorio.

## Avance 1: planificación y verificación de la misión

Los primeros cuatro ejercicios permiten calcular los recursos necesarios y comprobar si la nave cuenta con las condiciones para realizar el viaje.

1. **Cálculo de recursos necesarios:** solicita el nombre de la misión, la cantidad de tripulantes y los días de viaje. Calcula el combustible para ida y regreso, la reserva de combustible, el oxígeno, la energía y las provisiones.
2. **Verificación de combustible:** compara el combustible disponible con el necesario para la ida, el regreso y la reserva. Muestra una advertencia cuando el excedente es menor que 10 unidades.
3. **Soporte para la tripulación:** comprueba si el oxígeno y las provisiones disponibles son suficientes para cubrir las necesidades del viaje.
4. **Autorización de lanzamiento:** evalúa el combustible, el oxígeno, la energía y las provisiones. El lanzamiento se autoriza solamente cuando todos los recursos cumplen con las cantidades requeridas.

## Actualizaciones del segundo avance: exploración científica

El archivo `src/avance_2/ejercicio7_exploracion.py` incorpora una simulación interactiva de las actividades que puede realizar la tripulación al llegar al destino.

Al iniciar, el programa solicita la energía y las provisiones disponibles. Después presenta un menú con estas actividades:

| Opción | Actividad | Energía consumida | Provisiones consumidas | Puntos científicos |
| --- | --- | ---: | ---: | ---: |
| 1 | Analizar terreno | 8 | 0 | 10 |
| 2 | Recolectar muestra | 12 | 2 | 20 |
| 3 | Realizar observación | 5 | 0 | 8 |
| 4 | Finalizar exploración | 0 | 0 | 0 |

Antes de completar una actividad, el programa verifica que existan recursos suficientes. Cuando la actividad se realiza, actualiza la energía y las provisiones restantes, suma los puntos científicos y registra las actividades realizadas. También lleva el conteo de las muestras recolectadas.

La exploración termina cuando la tripulación selecciona la opción de finalizar o cuando no existen recursos suficientes para completar una actividad. Al final se muestra un resumen con las actividades realizadas, las muestras recolectadas, los puntos científicos y los recursos restantes.

## Requisitos

- Python 3.
- Un editor de código, como Visual Studio Code.
- Terminal o consola para ejecutar los archivos.

Los ejercicios utilizan funcionalidades incluidas en Python y no requieren instalar librerías externas.

## Cómo ejecutar los programas

Clona el repositorio y entra en su carpeta:

```bash
git clone https://github.com/jarayacha-gif/proyecto-soft01.git
cd proyecto-soft01
```

Ejecuta los programas desde la raíz del repositorio:

```bash
python src/avance_1/ejercicio1Proyecto.py
python src/avance_1/ejercicio2Proyecto.py
python src/avance_1/ejercicio3Proyecto.py
python src/avance_1/ejercicio4Proyecto.py
python src/avance_2/ejercicio7_exploracion.py
```

En Windows también puedes utilizar `py` en lugar de `python`. Por ejemplo:

```bash
py src/avance_2/ejercicio7_exploracion.py
```

Cada ejercicio se ejecuta de forma independiente y solicita la información directamente por consola.

## Conceptos de programación utilizados

- **Variables y constantes:** almacenamiento de datos de entrada, resultados y valores definidos para los cálculos.
- **Entradas y salidas:** interacción con el usuario mediante `input()` y `print()`.
- **Operadores aritméticos:** cálculos de consumo de recursos y puntuaciones.
- **Estructuras condicionales:** comparación de recursos y toma de decisiones mediante `if`, `elif` y `else`.
- **Ciclos de repetición:** uso de `while` para mantener activo el menú de exploración.
- **Contadores y acumuladores:** registro de actividades, muestras recolectadas y puntos científicos.

## Documentación

- [Documentación del Avance 1](docs/avance_1/documentacion_proyecto_avance_1.pdf)
- [Documentación del segundo avance — Ejercicio 7](docs/avance_2/ejercicio7_avance_2.pdf)

## Estado del proyecto

El repositorio conserva el trabajo del primer avance e incorpora las actualizaciones correspondientes al segundo avance de **Misión Órbita**. Cada ejercicio se encuentra separado para facilitar su consulta y ejecución.
