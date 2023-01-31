from Crypto.Cipher import DES 
import base64
import os

"""
Es necesario reemplazar la instalación de pycrypto por pycryptodome:
pip uninstall pycrypto
pip install pycryptodome
"""


def formatear_multiplo_de_8(text): 
    while(len(text)%8 != 0):
        text += b' ' #leañado espacios en blanco al final 
    return text


def encriptar(mensaje,key,iv):
    #instanciamos un nuevo objeto DES
    cipher = DES.new(key,DES.MODE_OFB,IV=iv) 
    #ciframos los datos
    bytesCifrados = cipher.encrypt(mensaje)
    print ("Bytes cifrados: ", bytesCifrados)
    return bytesCifrados


def desencriptar(mensaje,key,iv):
    #es necesario un nuevo objeto para descifrar 
    cipher = DES.new(key, DES.MODE_OFB,IV=iv) 
    mensajeDescifrado = cipher.decrypt(mensaje)
    return mensajeDescifrado


def main():
    Password = b'Mi pa$$ para P$P' #Los algoritmos DES se usaban para encriptar las contraseñas de los usuarios
    mensaje = formatear_multiplo_de_8(Password)
    print ("Mensaje original:", mensaje.decode())

    key = os.urandom(8) #establecemos una clave de 16 bytes
    iv = os.urandom(DES.block_size) #generamos aleatoriamente un iv del tamaño del bloque DES
    mensajeCifrado = encriptar(mensaje,key,iv) #para imprimir una mejor representación 
    mensajeCifrado_decod = base64.b64encode(mensajeCifrado).decode("utf-8") 
    print ("Mensaje Cifrado:", mensajeCifrado_decod)

    #desciframos usando la misma key e iv 
    mensajeDescifrado = desencriptar(mensajeCifrado,key,iv) 
    print ("Mensaje: ", mensajeDescifrado.decode("utf-8"))


if __name__=="__main__": 
    main()