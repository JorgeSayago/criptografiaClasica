from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

def generar_claves():
    clave = RSA.generate(2048)
    return clave, clave.publickey()

def cifrar_rsa(mensaje_bytes, clave_publica):
    cifrador = PKCS1_OAEP.new(clave_publica)
    return cifrador.encrypt(mensaje_bytes)

def descifrar_rsa(mensaje_cifrado, clave_privada):
    descifrador = PKCS1_OAEP.new(clave_privada)
    return descifrador.decrypt(mensaje_cifrado)

def demo_rsa():
    clave_privada, clave_publica = generar_claves()
    print('Claves RSA de 2048 bits generadas correctamente')
    print()

    mensaje = b'Mensaje secreto RSA'
    cifrado = cifrar_rsa(mensaje, clave_publica)
    descifrado = descifrar_rsa(cifrado, clave_privada)

    print(f'Mensaje original:   {mensaje.decode()}')
    print(f'Mensaje cifrado:    {binascii.hexlify(cifrado)[:40]}...')
    print(f'Mensaje descifrado: {descifrado.decode()}')
    print(f'¿Coinciden? {mensaje == descifrado}')

if __name__ == '__main__':
    demo_rsa()