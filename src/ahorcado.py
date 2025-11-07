"""
Juego del Ahorcado
==================

Práctica de programación que evalúa:
- Variables y tipos de datos primitivos
- Sentencias condicionales
- Sentencias iterativas
- Manipulación de strings

Autor: Gonzalo Blanco Mosteiro
Fecha: 07/11/2025
"""

def limpiar_pantalla():
    """
    Imprime varias líneas en blanco para 'limpiar' la consola
    y que el jugador 2 no vea la palabra introducida
    """
    print("\n" * 50)


def solicitar_palabra() -> str:
    """
    Solicita una palabra al jugador 1
    La palabra debe tener mínimo 5 caracteres y solo contener letras
    
    Returns:
        str: La palabra a adivinar en mayúsculas
    """
    # TODO: Implementar la función
    # - Usar un bucle while para repetir hasta que la palabra sea válida
    # - Verificar que tenga al menos 5 caracteres (len())
    # - Verificar que solo contenga letras (isalpha())
    # - Convertir a mayúsculas (upper())
    word: str = input("Jugador 1: Introduce la palabra a adivinar (mínimo 5 letras): ")
    while len(word) < 5 or not word.isalpha() or not isinstance(word, str):
        word: str = input("Jugador 1: Introduce la palabra a adivinar (mínimo 5 letras): ")

        if not isinstance(word, str):
            raise Exception("La palabra a adivinar solo debe de contener letras en formato UTF-8")
        elif not word.isalpha():
            raise Exception("La palabra a adivinar debe ser una string UTF-8")
        elif len(word) < 5:
            raise Exception("La palabra debe de tener minimo 5 letras")

    return word.upper()


def solicitar_letra(letras_usadas: list[str]):
    """
    Solicita una letra al jugador 2
    La letra debe ser válida (solo una letra) y no estar ya usada
    
    Args:
        letras_usadas (list): Lista de letras ya introducidas
        
    Returns:
        str: La letra introducida en mayúsculas
    """
    # TODO: Implementar la función
    # - Usar un bucle while para repetir hasta que la letra sea válida
    # - Verificar que sea solo un carácter (len() == 1)
    # - Verificar que sea una letra (isalpha())
    # - Verificar que no esté en letras_usadas (operador 'in')
    # - Convertir a mayúsculas (upper())
    letter: str = input("Letra: ")
    while not len(letter) == 1 or not letter.isalpha() or any(letter.upper() == letra for letra in letras_usadas):
        letter: str = input("Letra: ")

        if not isinstance(letter, str):
            raise Exception("La letra solo debe de contener letras en formato UTF-8")
        elif not letter.isalpha():
            raise Exception("La letra debe ser una string UTF-8")
        elif any(letter.upper() == letra for letra in letras_usadas):
            raise Exception("La letra esta repetida")

    return letter.upper()

def mostrar_estado(palabra_oculta: str, intentos: int, letras_usadas: list[str]):
    """
    Muestra el estado actual del juego
    
    Args:
        palabra_oculta (str): La palabra con _ y letras adivinadas
        intentos (int): Número de intentos restantes
        letras_usadas (list): Lista de letras ya usadas
    """
    # TODO: Implementar la función
    # - Imprimir intentos restantes
    # - Imprimir la palabra con espacios entre caracteres
    # - Imprimir las letras usadas
    print(f"Intentos restantes: {intentos}")
    print("Palabra: ", palabra_oculta)

    letras = ""
    for letra in letras_usadas:
        letras += f"{letra}, "

    print(f"Letras usadas: {letras}")


def actualizar_palabra_oculta(palabra: str, palabra_oculta: str, letra: str) -> str:
    """
    Actualiza la palabra oculta revelando las apariciones de la letra
    
    Args:
        palabra (str): La palabra completa a adivinar
        palabra_oculta (str): La palabra actual con _ y letras adivinadas
        letra (str): La letra que se ha adivinado
    Returns:
        str: La palabra oculta actualizada
    """
    # TODO: Implementar la función
    # - Recorrer la palabra original con un bucle for
    # - Usar enumerate() para obtener índice y carácter
    # - Si el carácter coincide con la letra, reemplazar en palabra_oculta
    # - Puedes convertir palabra_oculta a lista, modificar y volver a string
    repetida = False
    palabra_enum = list(enumerate(palabra))
    repetida_contador = [tuplas[1] for tuplas in palabra_enum].count(letra)
    palabra_coulta_array = palabra_oculta.split(" ")
    for i in range(len(palabra)):
        if palabra_enum[i][1] == letra:
            if repetida_contador > 0:
                palabra_coulta_array[i] = letra
                repetida_contador -= 1

                if repetida_contador == 0:
                    palabra_oculta_actualizada = " ".join(palabra_coulta_array)
                    return palabra_oculta_actualizada
            else:
                palabra_coulta_array = palabra_oculta.split(" ")
                palabra_coulta_array[i] = letra

                palabra_oculta_actualizada = " ".join(palabra_coulta_array)
                return palabra_oculta_actualizada

    return palabra_oculta

def jugar():
    """
    Función principal que ejecuta el juego del ahorcado
    """
    print("=== JUEGO DEL AHORCADO ===\n")
    
    # Configuración inicial
    # TODO: Solicitar la palabra al jugador 1
    palabra = solicitar_palabra()
    
    # TODO: Limpiar la pantalla para que el jugador 2 no vea la palabra
    limpiar_pantalla()
    
    # TODO: Inicializar variables del juego
    # - palabra_oculta: string con guiones bajos (ej: "_ _ _ _ _")
    # - intentos: número de intentos restantes
    # - letras_usadas: lista vacía
    # - juego_terminado: False


    palabra_oculta = "_ "*len(palabra)
    INTENTOS_MAXIMOS = 5
    letras_usadas = []
    juego_terminado = False

    print("Jugador 2: ¡Adivina la palabra!\n")

    # TODO: Bucle principal del juego
    # - Mientras haya intentos y el juego no haya terminado:
    #   1. Mostrar el estado actual
    #   2. Solicitar una letra
    #   3. Añadir la letra a letras_usadas
    #   4. Si la letra está en la palabra:
    #      - Actualizar palabra_oculta
    #      - Mostrar mensaje de acierto
    #      - Si ya no hay '_' en palabra_oculta, el jugador ha ganado
    #   5. Si la letra NO está en la palabra:
    #      - Restar un intento
    #      - Mostrar mensaje de fallo


    while INTENTOS_MAXIMOS != -1 and juego_terminado == False:
        letra = solicitar_letra(letras_usadas)
        letras_usadas.append(letra)

        palabra_oculta = actualizar_palabra_oculta(palabra, palabra_oculta, letra)
        mostrar_estado(palabra_oculta, INTENTOS_MAXIMOS, letras_usadas)

        if letra in palabra:
            print("Letra correcta")
            juego_terminado = True if palabra_oculta.find("_") == -1 else False
        else:
            print("Letra incorrecta")
            INTENTOS_MAXIMOS -= 1

    # TODO: Mostrar mensaje final
    # - Si ganó: mostrar felicitación y la palabra
    # - Si perdió: mostrar mensaje de derrota y la palabra correcta
    if juego_terminado:
        print("\nJuego terminado, felicidades")
    else:
        print("\nJuego terminado, lo siento, te has quedado sin intentos")

    print("Palabra:", palabra)


def main():
    """
    Punto de entrada del programa
    """
    try:
        jugar()
    except Exception as error:
        print(error)
    except KeyboardInterrupt:
        print("Salida por usuario")
    
    # TODO (Opcional): Preguntar si quiere jugar otra vez
    # jugar_otra_vez = input("\n¿Quieres jugar otra vez? (s/n): ")
    # if jugar_otra_vez.lower() == 's':
    #     main()


if __name__ == "__main__":
    main()
