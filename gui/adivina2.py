import tkinter as tk  # Importa la librería Tkinter para crear interfaces gráficas
import random  # Importa la librería random para generar números aleatorios
import time  # Importa la librería time para manejar pausas y temporizadores
import subprocess  # Importa la librería subprocess para ejecutar comandos del sistema
import sys  # Importa la librería sys para acceder a parámetros y funciones del sistema

def generar_palabra():
    """
    Genera una palabra aleatoria de un banco de palabras predefinido.

    Returns:
        str: Palabra aleatoria seleccionada.
    """
    banco_de_palabras = ['hola', 'adios', 'paraguay', 'gato', 'perro', 'cama', 'habitacion', 'familia']  # Lista de palabras posibles
    return random.choice(banco_de_palabras)  # Selecciona una palabra al azar y la devuelve

def actualizar_palabra_misteriosa(letra):
    """
    Actualiza la palabra misteriosa mostrando las letras adivinadas.

    Args:
        letra (str): Letra adivinada por el usuario.
    """
    global palabra, palabra_misteriosa  # Indica que estamos usando variables globales
    for i in range(len(palabra)):  # Recorre cada letra de la palabra
        if palabra[i] == letra:  # Si la letra adivinada coincide con la letra en la posición i
            palabra_misteriosa[i] = letra  # Reemplaza el guión bajo por la letra adivinada
    palabra_label.config(text=' '.join(palabra_misteriosa))  # Actualiza la etiqueta con la palabra misteriosa

def adivinar_letra():
    """
    Procesa la letra ingresada por el usuario y actualiza el juego.
    """
    global intentos, palabra, palabra_misteriosa, corazones  # Indica que estamos usando variables globales
    adivina = letra_entry.get().lower()  # Obtiene la letra ingresada, la convierte a minúscula
    letra_entry.delete(0, tk.END)  # Limpia el campo de entrada

    if len(adivina) != 1 or not adivina.isalpha():  # Si no se ingresa una letra o se ingresa más de una letra
        resultado_label.config(text="Por favor, ingresa una sola letra válida.", fg='red')  # Muestra un mensaje de error
        return  # Sale de la función

    if adivina in palabra:  # Si la letra adivinada está en la palabra
        actualizar_palabra_misteriosa(adivina)  # Actualiza la palabra misteriosa
        resultado_label.config(text='¡Bien hecho!', fg='green')  # Muestra un mensaje de éxito
    else:  # Si la letra no está en la palabra
        intentos -= 1  # Reduce el número de intentos
        intentos_label.config(text='Intentos restantes: ' + str(intentos), fg='#FF4500')  # Actualiza la etiqueta de intentos
        resultado_label.config(text='¡Incorrecto!', fg='red')  # Muestra un mensaje de error
        corazones[intentos].config(text=' ')  # Elimina un corazón
    if '_' not in palabra_misteriosa:
        resultado_label.config(text='\n¡Felicitaciones adivinaste! la palabra es: ' + palabra, fg='green')
        letra_entry.config(state=tk.DISABLED)
        ventana.after(5000, reiniciar_juego)  # Reiniciar después de 5 segundos
    elif intentos == 0:
        resultado_label.config(text='\nTe quedaste sin intentos. La palabra era: ' + palabra, fg='red')
        letra_entry.config(state=tk.DISABLED)
        ventana.after(5000, reiniciar_juego)  # Reiniciar después de 5 segundos
def cerrar_juego():
    """Cierra la aplicación."""
    ventana.destroy()

def reiniciar_juego():
    """Reinicia la aplicación."""
    ventana.destroy()  # Cierra la ventana actual
    subprocess.Popen([sys.executable, sys.argv[0]])  # Inicia un nuevo proceso con el mismo script

# Configuración inicial
palabra = generar_palabra()  # Genera la palabra a adivinar
palabra_misteriosa = ['_'] * len(palabra)  # Crea la palabra misteriosa con guiones bajos
intentos = 10  # Establece el número de intentos inicial

# Configuración de la ventana principal
ventana = tk.Tk()  # Crea la ventana principal
ventana.title("Adivina la Palabra")  # Establece el título de la ventana
ventana.configure(bg='#a9a9a9')  # Establece el color de fondo de la ventana

# Establecer el ancho y alto de la ventana
ancho = 750
alto = 600  # Alto de 600 píxeles

# Obtener el ancho y alto de la pantalla
ancho_pantalla = ventana.winfo_screenwidth()
alto_pantalla = ventana.winfo_screenheight()

# Calcular las coordenadas para centrar la ventana
x = (ancho_pantalla - ancho) // 2
y = (alto_pantalla - alto) // 2

# Establecer el tamaño y la posición de la ventana
ventana.geometry(f"{ancho}x{alto}+{x}+{y}")

# Título del juego más grande
titulo_label = tk.Label(ventana, text="Adivina la Palabra", font=('Helvetica', 36, 'bold'), bg='#a9a9a9', fg='#000040')  # Crea la etiqueta del título
titulo_label.pack(pady=20)  # Coloca la etiqueta en la ventana

# Etiquetas y campos de entrada
palabra_label = tk.Label(ventana, text=' '.join(palabra_misteriosa), font=('Helvetica', 36, 'bold'), bg='#a9a9a9', fg='#000040')  # Crea la etiqueta de la palabra misteriosa
intentos_label = tk.Label(ventana, text='Intentos restantes: ' + str(intentos), font=('Arial', 18), bg='#a9a9a9', fg='#FF4500')  # Crea la etiqueta de intentos
letra_label = tk.Label(ventana, text="Ingresa una letra:", font=('Arial', 16), bg='#a9a9a9', fg='#000040')  # Crea la etiqueta para ingresar letras
letra_entry = tk.Entry(ventana, font=('Arial', 16))  # Crea el campo de entrada para letras
adivinar_button = tk.Button(ventana, text="Adivinar", command=adivinar_letra, font=('Arial', 16, 'bold'), bg='#2e8b57', fg='white', relief=tk.RAISED, borderwidth=3,height=1)  # Crea el botón "Adivinar"
cerrar_button = tk.Button(ventana, text="Cerrar juego", command=cerrar_juego, font=('Arial', 16, 'bold'), bg='red', fg='white',borderwidth=3,height=1)# Crea el botón "Cerrar juego"
resultado_label = tk.Label(ventana, text="", font=('Arial', 18), bg='#a9a9a9', fg='#000040')  # Crea la etiqueta para mostrar resultados

# Corazones
corazones = []  # Lista para almacenar las etiquetas de corazones
corazones_frame = tk.Frame(ventana, bg='#a9a9a9')  # Crea un marco para los corazones
corazones_frame.pack(pady=15)  # Coloca el marco en la ventana
for i in range(10):  # Crea 10 corazones
    corazon = tk.Label(corazones_frame, text='♥', font=('Arial', 20), fg='red', bg='#a9a9a9')  # Crea la etiqueta del corazón
    corazon.pack(side=tk.LEFT)  # Coloca el corazón en el marco
    corazones.append(corazon)  # Agrega el corazón a la lista

# Colocación de elementos en la ventana
palabra_label.pack(pady=30)  # Coloca la etiqueta de la palabra misteriosa en la ventana
intentos_label.pack()  # Coloca la etiqueta de intentos en la ventana
corazones_frame.pack()  # Coloca el marco de corazones en la ventana
letra_label.pack(pady=10)  # Coloca la etiqueta para ingresar letras en la ventana
letra_entry.pack()  # Coloca el campo de entrada de letras en la ventana
adivinar_button.pack(pady=25)  # Coloca el botón "Adivinar" en la ventana
resultado_label.pack(pady=20)  # Coloca la etiqueta de resultados en la ventana
cerrar_button.place(x=ancho -200, y=alto - 120)# Coloca el botón en la esquina inferior derecha


ventana.mainloop()  # Inicia el bucle principal de la aplicación