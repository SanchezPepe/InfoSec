# Cifrado
## 3DES y AES
- Aprender a usar las bibliotecas de cifrado para 3DES y AES en el lenguaje de programación de su elección.
- Investigar la correcta generación de llaves para el cifrado
- Cifrar lo siguiente con los dos algoritmos:
    - Un mensaje corto - como algo que enviarían por WhatsApp, guardarlo en un archivo .txt
    - La presentación de Criptografía Simétrica que está en comunidad
    - El libro de Network Security Essentials que está en comunidad (des-zippearlo primero)
- Comparar los tiempos de ejecución de cada algoritmo para una llave de 128 bits.


## AES
Cifrado de bloques de 128 bits
La llave puede ser 128, 192 o 256 bits
El mensaje a cifrar se coloca en una matriz de 4x4, en cada celda se almacenan 8 bits = 1 byte

PlainText -> XOR -> Sustitur bytes -> Recorrer filas -> Mesclar columnas -> Añadir key

Para una llave de 128 = 10
192 = 12
256 = 14

