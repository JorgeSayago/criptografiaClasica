def cifrado_cesar(texto, desplazamiento):
    resultado = ''
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            resultado += chr((ord(char) - base + desplazamiento) % 26 + base)
        else:
            resultado += char
    return resultado

def ataque_fuerza_bruta(mensaje_cifrado, mensaje_original):
    print("Ataque de fuerza bruta (probando los 26 desplazamientos):")
    for i in range(1, 27):
        intento = cifrado_cesar(mensaje_cifrado, -i)
        marca = ' <-- ¡CLAVE ENCONTRADA!' if intento == mensaje_original else ''
        print(f'  Clave {i:2d}: {intento}{marca}')

def demo_cesar():
    mensaje_original = 'Hola Mundo Seguro'
    desplazamiento = 3
    mensaje_cifrado = cifrado_cesar(mensaje_original, desplazamiento)
    print(f'Mensaje original: {mensaje_original}')
    print(f'Mensaje cifrado:  {mensaje_cifrado}')
    print()
    ataque_fuerza_bruta(mensaje_cifrado, mensaje_original)

if __name__ == '__main__':
    demo_cesar()