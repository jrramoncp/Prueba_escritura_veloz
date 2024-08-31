import tkinter as tk
import timeit
import random

# Lista de frases

frases = ["El sol se ocultó tras las montañas, tiñendo el cielo de un naranja profundo.",
         "El gato negro saltó ágilmente sobre el tejado, desapareciendo en la oscuridad de la noche.",
         "En la biblioteca, el silencio solo era interrumpido por el suave pasar de las páginas.",
         "La brisa marina traía consigo el aroma salado del océano y la promesa de una nueva aventura.",
         "Las luces de la ciudad brillaban como estrellas en un firmamento de asfalto.",
         "El reloj marcaba la medianoche cuando un susurro misterioso rompió el silencio en la casa vacía.",
         "Una gota de lluvia cayó sobre la ventana, seguida de muchas más, creando un ritmo constante y relajante.",
         "La fragancia de las flores primaverales llenaba el aire, evocando recuerdos de tiempos pasados.",
         "El niño observaba fascinado cómo las mariposas volaban libremente entre las flores del jardín.",
         "En el corazón del bosque, el canto de los pájaros se mezclaba con el crujir de las hojas bajo sus pies.",
         "El viento soplaba fuerte, haciendo bailar las hojas en el aire.",
         "Las olas rompían con fuerza contra las rocas, creando una espuma blanca.",
         "El viejo reloj en la pared marcaba cada segundo con un tic-tac constante.",
         "El perro ladró alegremente al ver a su dueño llegar a casa.",
         "La luna llena iluminaba el camino mientras caminaba por el bosque.",
         "Los niños corrían por el parque, riendo y jugando sin preocupaciones.",
         "Una mariposa revoloteaba entre las flores, sus alas brillando al sol.",
         "El aroma del café recién hecho llenaba la cocina en la mañana tranquila.",
         "Las estrellas brillaban intensamente en el cielo despejado de la noche.",
         "El tren avanzaba por la vía, su sonido resonando en la distancia.",
         ]

# Variables 
frase = random.choice(frases) # Frase aleatoria
tiempo_inicio = None # Variable para almacenar el tiempo

# Ventana de la app
ventana = tk.Tk()
ventana.title("Prueba de escritura veloz")

# Etiqueta con la frase a escribir

label = tk.Label(font=("Arial, 14"))
label.config(text=frase)
label.pack(pady=20)

# Entrada texto

entrada = tk.Entry(ventana, font=("Arial", 14), width=50)
entrada.pack(pady=20)

# Función para contar el tiempo
def iniciar_tiempo(event):
    ''' Función que inicia el contador de tiempo'''
    global tiempo_inicio
    if tiempo_inicio is None:
        tiempo_inicio = timeit.default_timer() #Empieza a contar el tiempo

def verificar(event):
    ''' Funcion que comprueba la frase y hace la resta entre el tiempo de inicio y el tiempo final'''
    global tiempo_inicio

    texto_ingresado = entrada.get()

    if texto_ingresado == frase: 
        tiempo_fin = timeit.default_timer()
        tiempo_total = tiempo_fin - tiempo_inicio
        tiempo.config(text=f"Correcto, tiempo total: {tiempo_total:.2f} segundos")


entrada.bind("<KeyPress>", iniciar_tiempo) # Asignamos el inicio del temporizador a pulsar cualquier tecla 
entrada.bind("<Return>", verificar) # Asignamos la funcion verificadora a pulsar enter

# Etiqueta para mostrar el tiempo
tiempo = tk.Label(ventana, text="", font=("Arial, 14"))
tiempo.pack(pady=20)


# Bucle principal
ventana.mainloop()