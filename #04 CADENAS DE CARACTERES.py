"""
- EJERCICIO:
- Muestra ejemplos de todas las operaciones que puedes realizar con cadenas de caracteres
- en tu lenguaje. Algunas de esas operaciones podrían ser (busca todas las que puedas):
- Acceso a caracteres específicos, subcadenas, longitud, concatenación, repetición, recorrido,
- conversión a mayúsculas y minúsculas, reemplazo, división, unión, interpolación, verificación...
"""

s1 = "Hola"
s2 = "Python"

# Concatenacion
print(s1 + ", " + s2 + "!")

# Repetición
print(s1 * 3)

# Indexación
print(s1[0] + s1[1] + s1[2] + s1[3])

# Longitud
print(len(s2))

# Slicing (porción)
print(s2[2:6])
print(s2[2:])
print(s2[0:2])
print(s2[:2])

# Busqueda
print("a" in s1)
print("i" in s1)

# Reemplazo
print(s1.replace("o", "a"))

# División
print(s2.split("t"))

# Mayúsculas, minúsculas y letras en mayúsculas
print(s1.upper())
print(s1.lower())
print("christian bustamante".title())
print("christian bustamante".capitalize())

# Eliminación de espacios al principio y al final
print(" christian bustamante ".strip())

# Búsqueda al principio y al final
print(s1.startswith("Ho"))
print(s1.startswith("Py"))
print(s1.endswith("la"))
print(s1.endswith("thon"))

s3 = "Christian Daniel @ChristianDaniel"

# Búsqueda de posición
print(s3.find("christian"))
print(s3.find("Christian"))
print(s3.find("C"))
print(s3.lower().find("c"))

# Búsqueda de ocurrencias
print(s3.lower().count("C"))

# Formateo
print("Saludo: {}, lenguaje: {}!".format(s1, s2))

# Interpolación
print(f"Saludo: {s1}, lenguje: {s2}!")

# Tranformación en lista de caracteres
print(list(s3))

# Transformación de lista en cadena
l1 = [s1, ", ", s2, "!"]
print("".join(l1))

# Transformaciones numéricas
s4 = "123456"
s4 = int(s4)
print(s4)

s5 = "123456.123"
s5 = float(s5)
print(s5)

# Comprobaciones varias
s4 = "123456"
print(s1.isalnum())
print(s1.isalpha())
print(s4.isalpha())
print(s4.isnumeric())


"""
- DIFICULTAD EXTRA (opcional):
- Crea un programa que analice dos palabras diferentes y realice comprobaciones
- para descubrir si son:
- * Palíndromos
- * Anagramas
- * Isogramas
"""

def programa(word1: str, word2: str):

    # Palindromo
    print(f"¿{word1} es un palindromo?: {word1 == word1[::-1]}")
    print(f"¿{word2} es un palindromo?: {word2 == word2[::-1]}")

    # Anagrama
    print(f"¿{word1} es un anagrama de {word2}?: {sorted(word1) == sorted(word2)}")

    # Isograma

    def isogram(word: str) -> bool:

        word_dict = dict()
        for character in word:
            word_dict[character] = word_dict.get(character, 0) + 1

        isogram = True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break

        return isogram
    
    print(f"¿{word1} es un isograma?: {isogram(word1)}")
    print(f"¿{word2} es un isograma?: {isogram(word2)}")


programa("amor", "roma")




