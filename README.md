# Puzzle2
Código Puzzle 2 interfaz gráfica para leer una tarjeta NFC con la RPi

# Aplicación NFC Card Reader

Esta aplicación en Python crea una interfaz gráfica simple para leer tarjetas NFC y mostrar su UID en la pantalla. El usuario puede iniciar la lectura y actualizar la interfaz con un botón.

## Características

- Mensaje de bienvenida inicial.
- Botón "Leer otro UID" para iniciar la lectura.
- Actualización de la interfaz con el UID leído.
- Cambio de color de fondo de la interfaz al leer una tarjeta.

## Uso

1. Ejecuta el programa.
2. La aplicación muestra un mensaje de bienvenida.
3. Haz clic en el botón "Leer otro UID" para iniciar la lectura.
4. La aplicación lee una tarjeta NFC y muestra su UID en la interfaz.
5. La interfaz se actualiza con un color de fondo verde al mostrar el UID.
6. Puedes hacer clic en el botón nuevamente para leer otra tarjeta.

## Requisitos

- Python
- Bibliotecas Gtk y GLib
- Biblioteca `puzzle1` (para la lectura de tarjetas NFC)

## Notas

- El programa utiliza hilos para la lectura de tarjetas NFC, lo que permite la lectura en segundo plano sin bloquear la interfaz de usuario.

Espero que este resumen sea útil para tu archivo README.md. Si necesitas más información o detalles, no dudes en preguntar.
