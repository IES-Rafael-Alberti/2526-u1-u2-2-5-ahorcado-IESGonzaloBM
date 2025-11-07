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
    EPITEXTO
    Solicita una palabra al jugador 1
    La palabra debe tener mínimo 5 caracteres y solo contener letras
    
    @returns: palabra del jugador 1
    """
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


def solicitar_letra(letras_usadas: list[str]) -> str:
    """
    NumPy/SciPy
    Solicita una letra al jugador 2
    La letra debe ser válida (solo una letra) y no estar ya usada
    
    Parameters
    ----------
        letras_usadas : list
            Lista de letras ya introducidas
        
    Returns
    -------
        str
            La letra introducida en mayúsculas
    """
    letter: str = input("Letra: ")
    while not len(letter) == 1 or not letter.isalpha() or any(letter.upper() == letra for letra in letras_usadas):
        letter: str = input("Letra: ")

        if not isinstance(letter, str):
            raise Exception("La letra solo debe de contener letras en formato UTF-8")
        elif not letter.isalpha():
            raise Exception("La letra debe ser un string UTF-8")
        elif any(letter.upper() == letra for letra in letras_usadas):
            print("La letra esta repetida")

    return letter.upper()

def mostrar_estado(palabra_oculta: str, intentos: int, letras_usadas: list[str]):
    """
    NumPy/SciPy
    Muestra el estado actual del juego
    
    Parameters
    ----------
        palabra_oculta : str
            La palabra con _ y letras adivinadas
        intentos : int
            Número de intentos restantes
        letras_usadas : list
            Lista de letras ya usadas
    """
    print(f"Intentos restantes: {intentos}")
    print("Palabra: ", palabra_oculta)

    letras: str = ""
    for letra in letras_usadas:
        letras += f"{letra}, "

    print(f"Letras usadas: {letras}")


def actualizar_palabra_oculta(palabra: str, palabra_oculta: str, letra: str) -> str:
    """
    NumPy/SciPy
    Actualiza la palabra oculta revelando las apariciones de la letra
    
    Parameters
    ----------
        palabra : str
            La palabra completa a adivinar
        palabra_oculta : str
            La palabra actual con _ y letras adivinadas
        letra : str
            La letra que se ha adivinado
    Returns
    -------
        str
            La palabra oculta actualizada
    """

    # Usamos enumerate para enumerarar cada valor en [0, len(palabra)] y lo listamos en un array
    # Usamos compresion de listas con bucles para acceder al 2º valor de cada tupla, es decir, el caracter.
    # Despues contamos cuantos valores coinciden con letra para saber si es valor esta repetido e iterar mas veces sobre
    # el en el futuro
    palabra_enum: list[tuple] = list(enumerate(palabra))
    repetida: int = [tuplas[1] for tuplas in palabra_enum].count(letra)
    palabra_coulta_array: list[str] = palabra_oculta.split(" ")

    for i in range(len(palabra)):
        if palabra_enum[i][1] == letra:
            if repetida > 0:
                palabra_coulta_array[i] = letra
                repetida -= 1

                if repetida == 0:
                    return " ".join(palabra_coulta_array)
            else:
                palabra_coulta_array[i] = letra
                return " ".join(palabra_coulta_array)

    return palabra_oculta

def jugar():
    """
    Función principal que ejecuta el juego del ahorcado
    """
    print("=== JUEGO DEL AHORCADO ===\n")

    palabra: str = solicitar_palabra()

    limpiar_pantalla()

    palabra_oculta: str = "_ "*len(palabra)
    INTENTOS_MAXIMOS: int = 5
    letras_usadas: list = []
    juego_terminado: bool = False

    print("Jugador 2: ¡Adivina la palabra!\n")

    while INTENTOS_MAXIMOS != -1 and juego_terminado == False:
        letra: str = solicitar_letra(letras_usadas)
        letras_usadas.append(letra)

        palabra_oculta: str = actualizar_palabra_oculta(palabra, palabra_oculta, letra)
        mostrar_estado(palabra_oculta, INTENTOS_MAXIMOS, letras_usadas)

        if letra in palabra:
            print("Letra correcta\n")
            juego_terminado: bool = True if palabra_oculta.find("_") == -1 else False
        else:
            print("Letra incorrecta\n")
            INTENTOS_MAXIMOS -= 1

    print("\nJuego terminado, felicidades") if juego_terminado else print("\nJuego terminado, lo siento, te has quedado sin intentos")
    print("Palabra:", palabra)


def main():
    """
    Punto de entrada del programa
    """
    try:
        jugar()
        jugar_otra_vez: str = input("\n¿Quieres jugar otra vez? (s/n): ")
        if jugar_otra_vez.lower() == 's':
            main()
    except Exception as error:
        print(error)
        jugar_otra_vez: str = input("\n¿Quieres jugar otra vez? (s/n): ")
        if jugar_otra_vez.lower() == 's':
            main()
    except KeyboardInterrupt:
        print("Salida por usuario")


if __name__ == "__main__":
    main()
