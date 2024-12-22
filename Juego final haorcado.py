import random  # Importa el módulo random para seleccionar una palabra al azar

# Función para dibujar el ahorcado según los intentos restantes
def dibujar_ahorcado(intentos):
    # Lista de dibujos que representan el estado del ahorcado en cada etapa
    figuras = [
        """
           +---+
               |
               |
               |
              ===
        """,
        """
           +---+
           O   |
               |
               |
              ===
        """,
        """
           +---+
           O   |
           |   |
               |
              ===
        """,
        """
           +---+
           O   |
          /|   |
               |
              ===
        """,
        """
           +---+
           O   |
          /|\  |
               |
              ===
        """,
        """
           +---+
           O   |
          /|\  |
          /    |
              ===
        """,
        """
           +---+
           O   |
          /|\  |
          / \  |
              ===
        """
    ]
    # Muestra la figura correspondiente al número de intentos restantes
    print(figuras[6 - intentos])

# Función principal para jugar al ahorcado
def jugar_ahorcado():
    # Lista de palabras posibles para adivinar
    palabras = ["programar", "jugar", "python", "barberia"]
    # Selecciona una palabra secreta al azar
    palabra_secreta = random.choice(palabras)
    # Inicializa la palabra con guiones bajos para cada letra no descubierta
    letras_adivinadas = ["_" for _ in palabra_secreta]
    # Número inicial de intentos permitidos
    intentos_restantes = 6
    # Lista para registrar las letras que el jugador ya intentó
    letras_intentadas = []

    # Mensaje de bienvenida
    print("\n\u26A1 Bienvenido al juego del Ahorcado \u26A1\n")

    # Bucle principal del juego
    while intentos_restantes > 0 and "_" in letras_adivinadas:
        # Dibuja el estado actual del ahorcado
        dibujar_ahorcado(intentos_restantes)
        # Muestra el progreso actual de la palabra
        print("Palabra:", " ".join(letras_adivinadas))
        # Muestra el número de intentos restantes
        print(f"Intentos restantes: {intentos_restantes}")
        # Muestra las letras que el jugador ya intentó
        print("Letras intentadas:", ", ".join(letras_intentadas))

        # Solicita al jugador que introduzca una letra
        letra = input("\nIntroduce una letra: ").lower()

        # Verifica si la entrada es válida (una sola letra alfabética)
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, introduce una letra válida.")
            continue

        # Verifica si la letra ya fue intentada previamente
        if letra in letras_intentadas:
            print("Ya intentaste esa letra. Intenta con otra.")
            continue

        # Agrega la letra a la lista de letras intentadas
        letras_intentadas.append(letra)

        # Verifica si la letra está en la palabra secreta
        if letra in palabra_secreta:
            print(f"¡Bien! La letra '{letra}' está en la palabra.")
            # Reemplaza los guiones bajos con la letra adivinada en las posiciones correctas
            for i, l in enumerate(palabra_secreta):
                if l == letra:
                    letras_adivinadas[i] = letra
        else:
            # Si la letra no está en la palabra, se pierde un intento
            print(f"Lo siento, la letra '{letra}' no está en la palabra.")
            intentos_restantes -= 1

    # Dibuja el estado final del ahorcado
    dibujar_ahorcado(intentos_restantes)

    # Verifica si el jugador ganó o perdió
    if "_" not in letras_adivinadas:
        # Si no quedan guiones bajos, el jugador gana
        print("\n¡Felicidades! Adivinaste la palabra:", palabra_secreta)
    else:
        # Si los intentos se acabaron, el jugador pierde
        print("\nGame Over. La palabra era:", palabra_secreta)

# Verifica si el archivo se está ejecutando directamente
if __name__ == "__main__":
    jugar_ahorcado()  # Llama a la función principal para iniciar el juego