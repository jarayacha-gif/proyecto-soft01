# Misión Órbita — Actualizaciones del segundo avance

## Información del proyecto

- **Curso:** Principios de Programación 1
- **Código:** SOFT-01
- **Estudiante:** Jehidam Araya Chaves
- **Docente:** Verónica Mora Lezcano

## Descripción

Este repositorio contiene el desarrollo del proyecto **Misión Órbita**, realizado en Python para el curso Principios de Programación 1.

En esta versión se incorporan **actualizaciones correspondientes al segundo avance del proyecto**. Se conserva el trabajo del primer avance y se agrega el desarrollo de nuevas funcionalidades relacionadas con la exploración científica de la misión. De esta manera, el proyecto continúa ampliándose a partir de los ejercicios iniciales de planificación y verificación de recursos.

El primer avance permite calcular los recursos necesarios para el viaje y comprobar si la nave cuenta con las condiciones para autorizar el lanzamiento. Como parte de las actualizaciones del segundo avance, se incorpora una simulación interactiva que permite a la tripulación realizar actividades científicas, administrar los recursos disponibles y obtener puntos según las tareas completadas.

## Estructura del repositorio

```text
proyecto-soft01/
├── README.md
├── Avance1/
│   ├── ejercicio1Proyecto.py
│   ├── ejercicio2Proyecto.py
│   ├── ejercicio3Proyecto.py
│   └── ejercicio4Proyecto.py
├── Avance 2/
│   └── ejercicio7_exploracion.py
└── Documentacion/
    ├── Documentacion Proyecto _ Avance 1 .pdf
    └── Avance2/
        └── Ejercicio7_Avance2.pdf
```

## Avance 1: planificación y verificación de la misión

Los programas de este avance permiten calcular los recursos y comprobar si la nave cuenta con las condiciones necesarias para realizar el viaje.

1. **Cálculo de recursos necesarios para una misión:** solicita el nombre de la misión, la cantidad de tripulantes y los días de viaje. Calcula el combustible para ida y regreso, la reserva de combustible, el oxígeno, la energía y las provisiones requeridas.
2. **Verificación de combustible:** compara el combustible disponible con el combustible necesario para la ida, el regreso y la reserva. Muestra una advertencia cuando el combustible excedente es menor que 10 unidades.
3. **Verificación del soporte para la tripulación:** comprueba si la nave dispone de suficiente oxígeno y provisiones para cubrir las necesidades del viaje.
4. **Autorización inicial de lanzamiento:** evalúa conjuntamente el combustible, el oxígeno, la energía y las provisiones. El lanzamiento se autoriza solamente cuando todos los recursos alcanzan las cantidades requeridas.

## Actualizaciones del segundo avance: exploración científica

El archivo `Avance 2/ejercicio7_exploracion.py` incorpora una simulación interactiva de las actividades que puede realizar la tripulación al llegar al destino.

Al iniciar, el programa solicita la energía y las provisiones disponibles. Después presenta un menú con las siguientes actividades:

| Opción | Actividad | Energía consumida | Provisiones consumidas | Puntos científicos |
| --- | --- | ---: | ---: | ---: |
| 1 | Analizar terreno | 8 | 0 | 10 |
| 2 | Recolectar muestra | 12 | 2 | 20 |
| 3 | Realizar observación | 5 | 0 | 8 |
| 4 | Finalizar exploración | 0 | 0 | 0 |

Durante la exploración, el programa verifica que existan recursos suficientes antes de realizar cada actividad. Cuando una actividad se completa, actualiza la energía y las provisiones restantes, suma los puntos científicos y registra las actividades realizadas. También lleva el conteo de las muestras recolectadas.

La exploración termina cuando la tripulación selecciona la opción de finalizar o cuando no existen recursos suficientes para completar una actividad. Al final se presenta un resumen con las actividades realizadas, las muestras recolectadas, los puntos científicos obtenidos y los recursos restantes.

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

Ejecuta cada archivo desde la raíz del repositorio:

```bash
python Avance1/ejercicio1Proyecto.py
python Avance1/ejercicio2Proyecto.py
python Avance1/ejercicio3Proyecto.py
python Avance1/ejercicio4Proyecto.py
python "Avance 2/ejercicio7_exploracion.py"
```

En Windows también puedes utilizar el comando `py` en lugar de `python`.

Cada ejercicio se ejecuta de forma independiente y solicita la información directamente por consola.

## Conceptos de programación utilizados

- **Variables y constantes:** almacenamiento de datos de entrada, resultados y valores definidos para los cálculos.
- **Entradas y salidas:** interacción con el usuario mediante `input()` y `print()`.
- **Operadores aritméticos:** realización de cálculos de consumo, recursos y puntuaciones.
- **Estructuras condicionales:** comparación de recursos y toma de decisiones mediante `if`, `elif` y `else`.
- **Ciclos de repetición:** uso de `while` para mantener el menú de exploración activo mientras la tripulación continúe.
- **Contadores y acumuladores:** registro de actividades, muestras recolectadas y puntos científicos.

## Documentación

Los documentos de cada avance se encuentran en la carpeta `Documentacion`:

- [Documentación del Avance 1](Documentacion/Documentacion%20Proyecto%20_%20Avance%201%20.pdf)
- [Documentación del segundo avance — Ejercicio 7](Documentacion/Avance2/Ejercicio7_Avance2.pdf)

## Estado del proyecto

El repositorio reúne el trabajo inicial y las actualizaciones incorporadas en el segundo avance del proyecto **Misión Órbita**. La estructura permite consultar la documentación y ejecutar cada ejercicio de manera independiente.
