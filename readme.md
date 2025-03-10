# Adivina la Palabra

Este repositorio contiene dos versiones del juego "Adivina la Palabra":

* `consola/adivina.py`: Versión para consola.
* `gui/adivina2.py`: Versión con interfaz gráfica (GUI).

## Tecnologías Utilizadas

* **Python:** Lenguaje de programación principal utilizado en ambas versiones.
* **Tkinter (para la versión GUI):** Librería estándar de Python para crear interfaces gráficas de usuario.

## Versión de Consola (`consola/adivina.py`)

### Descripción

Esta versión del juego se ejecuta en la terminal. El jugador intenta adivinar una palabra oculta ingresando letras.

### Imports Utilizados

* **`random`**: Se utiliza para generar palabras aleatorias de una lista predefinida.
* **`os`**: Se utiliza para interactuar con el sistema operativo, como limpiar la pantalla de la consola.
* **`from termcolor import colored`**: Se utiliza para agregar color al texto mostrado en la consola.

### Métodos/Habilidades Utilizadas

* **Generación de palabras aleatorias:** Se utiliza la librería `random` para seleccionar una palabra al azar de una lista predefinida.
* **Manipulación de cadenas:** Se utilizan operaciones básicas de cadenas para mostrar la palabra oculta y actualizarla a medida que el jugador adivina letras.
* **Lógica de juego:** Se implementa la lógica principal del juego, incluyendo el seguimiento de intentos y la verificación de letras adivinadas.
* **Interacción con el sistema operativo:** Se utiliza la librería `os` para limpiar la pantalla de la consola y mejorar la experiencia de usuario.
* **Texto con color:** Se utiliza la librería `termcolor` para hacer que el texto en la consola sea más legible y atractivo.

## Versión GUI (`gui/adivina2.py`)

### Descripción

Esta versión del juego proporciona una interfaz gráfica interactiva. El jugador interactúa con botones y campos de entrada para adivinar la palabra.

### Imports Utilizados

* **`tkinter as tk`**: Se utiliza para crear la interfaz gráfica de usuario.
* **`random`**: Se utiliza para generar palabras aleatorias.
* **`time`**: Se utiliza para implementar pausas y temporizadores.
* **`subprocess`**: Se utiliza para ejecutar comandos del sistema y reiniciar el juego.
* **`sys`**: Se utiliza para acceder a parámetros y funciones del sistema.

### Métodos/Habilidades Utilizadas

* **Creación de interfaz gráfica:** Se utiliza la librería `Tkinter` para crear la ventana principal, etiquetas, botones y campos de entrada.
* **Manejo de eventos:** Se utilizan funciones de devolución de llamada para manejar eventos como clics de botones y entradas de teclado.
* **Actualización dinámica de la interfaz:** Se actualizan las etiquetas y otros widgets para reflejar el estado actual del juego.
* **Reiniciar juego:** se implementa la funcionalidad de reiniciar el juego despues de 5 seg con la libreria subprocess y sys
* **Temporizadores:** Se utiliza la función `after()` de Tkinter para programar la ejecución de funciones después de un cierto período de tiempo.
* **Diseño de interfaz:** Se aplican conceptos básicos de diseño de interfaz para crear una experiencia de usuario agradable.

## Cómo ejecutar

### Versión de consola

1.  Abre una terminal.
2.  Navega a la carpeta `consola`.
3.  Ejecuta `python adivina.py`.

### Versión GUI

1.  Abre una terminal.
2.  Navega a la carpeta `gui`.
3.  Ejecuta `python adivina2.py`.

## Licencia

Este proyecto está bajo la licencia [Nombre de la licencia, si aplica].