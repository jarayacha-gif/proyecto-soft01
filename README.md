<h1 align="center">🚀 Misión Órbita</h1>

<h2>📌 Descripción del proyecto</h2>

<p>
<strong>Misión Órbita</strong> es un proyecto desarrollado en Python para el curso
<strong>Principios de Programación 1 (SOFT-01)</strong>.
</p>

<p>
El proyecto consiste en desarrollar un simulador básico de preparación de una
misión de exploración espacial. En este primer avance se implementan cuatro
programas independientes relacionados con la preparación y verificación de
una misión.
</p>

<p>
Los ejercicios trabajan conceptos fundamentales de programación como:
variables, constantes, entrada y salida de datos, cálculos, estructuras
secuenciales y estructuras condicionales.
</p>

<hr>

<h2>🎯 Objetivo</h2>

<p>
El objetivo del proyecto es aplicar el pensamiento lógico-computacional para
resolver problemas de baja complejidad mediante el paradigma imperativo y el
lenguaje de programación Python.
</p>

<p>
Cada ejercicio sigue el proceso:
</p>

<ul>
    <li>Entrada de datos</li>
    <li>Procesamiento</li>
    <li>Decisión, cuando corresponde</li>
    <li>Salida de resultados</li>
</ul>

<hr>

<h2>📂 Estructura del repositorio</h2>

<pre>
mision-orbita/
│
├── README.md
│
├── avance1/
│   ├── ejercicio1_recursos.py
│   ├── ejercicio2_combustible.py
│   ├── ejercicio3_soporte_tripulacion.py
│   └── ejercicio4_autorizacion.py
│
└── documentacion/
    └── avance1.pdf
</pre>

<hr>

<h2>🧩 Ejercicios del proyecto</h2>

<h3>1️⃣ Cálculo de recursos necesarios para una misión</h3>

<p>
Archivo:
<strong>avance1/ejercicio1_recursos.py</strong>
</p>

<p>
Este programa calcula los recursos necesarios para realizar una misión,
considerando la cantidad de tripulantes y los días estimados de viaje.
</p>

<ul>
    <li>Combustible para el viaje de ida.</li>
    <li>Combustible para el viaje de regreso.</li>
    <li>Reserva de combustible.</li>
    <li>Oxígeno necesario.</li>
    <li>Energía necesaria.</li>
    <li>Provisiones necesarias.</li>
</ul>

<h3>2️⃣ Verificación de combustible</h3>

<p>
Archivo:
<strong>avance1/ejercicio2_combustible.py</strong>
</p>

<p>
Este programa verifica si la nave dispone del combustible necesario para
realizar el viaje de ida, regresar al punto de partida y mantener una reserva
de emergencia.
</p>

<ul>
    <li>Combustible disponible.</li>
    <li>Combustible requerido para llegar.</li>
    <li>Combustible requerido para regresar.</li>
    <li>Reserva de emergencia.</li>
    <li>Combustible total requerido.</li>
    <li>Combustible adicional disponible.</li>
</ul>

<p>
Si el combustible adicional es menor que 10 unidades, el programa muestra una
advertencia indicando que el margen adicional de combustible es bajo.
</p>

<h3>3️⃣ Verificación del soporte para la tripulación</h3>

<p>
Archivo:
<strong>avance1/ejercicio3_soporte_tripulacion.py</strong>
</p>

<p>
Este programa determina si existen suficientes recursos para mantener a la
tripulación durante el viaje.
</p>

<ul>
    <li>Oxígeno disponible.</li>
    <li>Oxígeno requerido.</li>
    <li>Provisiones disponibles.</li>
    <li>Provisiones requeridas.</li>
</ul>

<p>
La nave posee recursos suficientes únicamente cuando el oxígeno disponible y
las provisiones disponibles son mayores o iguales a las cantidades requeridas.
</p>

<h3>4️⃣ Autorización inicial de lanzamiento</h3>

<p>
Archivo:
<strong>avance1/ejercicio4_autorizacion.py</strong>
</p>

<p>
Este programa realiza una verificación general para determinar si una misión
puede ser autorizada para el lanzamiento.
</p>

<p>Para autorizar la misión deben cumplirse todas las condiciones:</p>

<ul>
    <li>El combustible disponible debe cubrir ida, regreso y reserva.</li>
    <li>El oxígeno disponible debe ser suficiente.</li>
    <li>La energía disponible debe ser suficiente.</li>
    <li>Las provisiones disponibles deben ser suficientes.</li>
</ul>

<p>
Cuando todas las condiciones se cumplen, se muestra:
</p>

<blockquote>
Lanzamiento autorizado.
</blockquote>

<p>
En caso contrario, se muestra:
</p>

<blockquote>
Lanzamiento no autorizado. La misión debe ser revisada.
</blockquote>

<hr>

<h2>🛠️ Tecnologías utilizadas</h2>

<ul>
    <li><strong>Python 3</strong></li>
    <li><strong>Visual Studio Code</strong></li>
    <li><strong>Git</strong></li>
    <li><strong>GitHub</strong></li>
</ul>

<hr>

<h2>📋 Convenciones y estilos</h2>

<ul>
    <li>Uso de nombres de variables descriptivos.</li>
    <li>Uso de <strong>snake_case</strong> o <strong>camelCase</strong>.</li>
    <li>Las constantes se escriben en mayúsculas.</li>
    <li>Indentación uniforme de 4 espacios.</li>
    <li>Espacios alrededor de los operadores.</li>
    <li>Mensajes de consola claros y ordenados.</li>
    <li>Comentarios para identificar los principales bloques lógicos.</li>
</ul>

<h3>📌 Restricciones del avance</h3>

<p>
De acuerdo con las reglas establecidas para este avance, los programas no
utilizan:
</p>

<ul>
    <li>Ciclos <code>for</code> o <code>while</code>.</li>
    <li>Listas, tuplas, diccionarios u otras colecciones.</li>
    <li>Funciones propias mediante <code>def</code>.</li>
    <li>Librerías externas o módulos importados.</li>
    <li>Archivos, JSON u orientación a objetos.</li>
    <li>Condicionales anidadas ni múltiples <code>elif</code>.</li>
</ul>

<hr>

<h2>▶️ Cómo ejecutar los programas</h2>

<p>
Para ejecutar los programas se necesita tener instalado
<strong>Python 3</strong>.
</p>

<p>
Desde la carpeta principal del repositorio se puede ejecutar cada ejercicio
utilizando los siguientes comandos:
</p>

<pre>
python avance1/ejercicio1_recursos.py
</pre>

<pre>
python avance1/ejercicio2_combustible.py
</pre>

<pre>
python avance1/ejercicio3_soporte_tripulacion.py
</pre>

<pre>
python avance1/ejercicio4_autorizacion.py
</pre>

<p>
Los programas utilizan la consola para solicitar los datos de entrada y
mostrar los resultados.
</p>

<hr>

<h2>🧪 Casos de prueba</h2>

<p>
Cada ejercicio cuenta con casos de prueba destinados a comprobar diferentes
comportamientos del programa.
</p>

<ul>
    <li>Casos normales.</li>
    <li>Casos límite.</li>
    <li>Casos donde las condiciones no se cumplen.</li>
    <li>Casos con recursos suficientes.</li>
    <li>Casos con recursos insuficientes.</li>
</ul>

<p>
Los casos de prueba incluyen los datos de entrada, el resultado esperado,
el resultado obtenido y el estado de la prueba.
</p>

<hr>

<h2>📚 Documentación</h2>

<p>
La carpeta <strong>documentacion/</strong> contiene el documento PDF
correspondiente al primer avance:
</p>

<ul>
    <li><strong>avance1.pdf</strong> — Documentación del proyecto.</li>
</ul>

<p>
El documento contiene la información de los ejercicios, tablas de variables,
diagramas de flujo, código y casos de prueba.
</p>

<hr>

<h2>👤 Integrante</h2>

<ul>
    <li><strong>Jehidam Araya Chaves</strong></li>
</ul>

<p>
<strong>Curso:</strong> Principios de Programación 1<br>
<strong>Código:</strong> SOFT-01<br>
<strong>Sección:</strong> SCV3<br>
<strong>Docente facilitador:</strong> Verónica Mora Lezcano<br>
<strong>Periodo:</strong> C3-2026
</p>

<hr>

<h2>📅 Avance 1</h2>

<p>
Este repositorio corresponde al primer avance del proyecto
<strong>Misión Órbita</strong>, enfocado en la preparación de la misión.
</p>

<p align="center">
    🚀 <strong>Misión Órbita — Principios de Programación 1</strong> 🚀
</p>
