MASTER MIND



Este divertido juego de mesa, adaptado para ejecutarse en una consola. El jugador debe adivinar una secuencia de colores que la computadora ha seleccionado al azar.
incluye colores y tematica Star Wars

Clases y Funcionalidad
UserColors
Esta clase se encarga de capturar las entradas de colores del usuario.

Atributos:
length: La cantidad de colores que el usuario debe adivinar.
Métodos:
get_colors(): Solicita al usuario que ingrese sus colores y devuelve una lista con estos.
SecretColors
Genera la secuencia secreta de colores que el jugador debe adivinar.

Atributos:
colors: Lista de posibles colores.
length: Número de colores en la secuencia secreta.
Métodos:
get_secret_colors: Propiedad que devuelve la secuencia secreta generada aleatoriamente.
PrintColors
Convierte los nombres de los colores en representaciones de texto coloreadas.

Métodos:
print_colors(colors): Recibe una lista de nombres de colores y devuelve una lista de cadenas de texto con formato de color usando colorama.
MasterMind
Clase principal que coordina las otras clases para ejecutar el juego.

Atributos:
colors: Lista de posibles colores.
length: Número de colores en la secuencia secreta.
print_colors: Instancia de PrintColors para imprimir texto con colores.
secret_colors: Secuencia de colores secretos generada por SecretColors.
user_colors: Instancia de UserColors para capturar las adivinanzas del usuario.
Métodos:
play(): Ejecuta el bucle del juego donde el usuario adivina la secuencia. Proporciona retroalimentación después de cada intento y verifica si el usuario ha adivinado correctamente.