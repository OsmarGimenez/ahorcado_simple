import random  # Importa la librería random para generar números aleatorios
import os      # Importa la librería os para interactuar con el sistema operativo
from termcolor import colored  # Importa la función colored de termcolor para dar color al texto

def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')  # Ejecuta 'cls' en Windows o 'clear' en otros sistemas

def mostrar_intentos(intentos):
    """Muestra los intentos restantes con corazones rojos."""
    intentos_visuales = colored('♥', 'red') * intentos  # Crea una cadena de corazones rojos
    print(colored("Intentos restantes: ", 'yellow') + intentos_visuales)  # Imprime el mensaje y los corazones

# Definimos una lista de palabras para el juego
banco_de_palabras = ['hola', 'adios', 'paraguay', 'gato', 'perro', 'cama', 'habitacion', 'familia']

# Con la librería random y su método choice elegimos una palabra de la lista
palabra = random.choice(banco_de_palabras)  # Selecciona una palabra al azar

# Escondemos las letras de la palabra según la cantidad de letras
palabra_misteriosa = ['_'] * len(palabra)  # Crea una lista de guiones bajos

# Definimos la cantidad de intentos que tiene para adivinar la palabra
intentos = 10

# Iniciamos el bucle del juego
while intentos > 0:  # Mientras queden intentos
    limpiar_pantalla()  # Limpia la pantalla
    print(colored("Adivina la palabra:", 'cyan'))  # Imprime el título
    print(' '.join(palabra_misteriosa))  # Imprime la palabra misteriosa con espacios
    mostrar_intentos(intentos)  # Muestra los intentos restantes

    # Almacenamos una letra de la palabra que adivine el usuario
    adivina = input(colored('Adivina la letra: ', 'green')).lower()  # Pide una letra y la convierte a minúscula

    if len(adivina) != 1 or not adivina.isalpha():  # Si no es una sola letra o no es una letra
        print(colored("Por favor, ingresa una sola letra válida.", 'red'))  # Muestra un mensaje de error
        input(colored("Presione enter para continuar...", 'blue'))  # Espera a que el usuario presione Enter
        continue  # Vuelve al inicio del bucle

    if adivina in palabra:  # Si la letra está en la palabra
        for i in range(len(palabra)):  # Recorre la palabra
            if palabra[i] == adivina:  # Si la letra coincide
                palabra_misteriosa[i] = adivina  # Revela la letra
        print(colored('¡Bien hecho!', 'green'))  # Muestra un mensaje de éxito
        input(colored("Presione enter para continuar...", 'blue'))  # Espera a que el usuario presione Enter
    else:  # Si la letra no está en la palabra
        intentos -= 1  # Reduce los intentos
        print(colored('¡Incorrecto! Intentos restantes: ' + str(intentos), 'red'))  # Muestra un mensaje de error
        input(colored("Presione enter para continuar...", 'blue'))  # Espera a que el usuario presione Enter

    # Cuando ya no quedan letras que adivinar de la palabra
    if '_' not in palabra_misteriosa:  # Si no hay guiones bajos
        limpiar_pantalla()  # Limpia la pantalla
        print(colored('\n¡Felicitaciones adivinaste! la palabra es: ' + palabra, 'green'))  # Muestra un mensaje de felicitación
        break  # Sale del bucle

if intentos == 0:  # Si se acabaron los intentos
    limpiar_pantalla()  # Limpia la pantalla
    print(colored('\nTe quedaste sin intentos. La palabra era: ' + palabra, 'red'))  # Muestra un mensaje de derrota