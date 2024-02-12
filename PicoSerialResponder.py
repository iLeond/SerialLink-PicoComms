import machine
import utime

# Configuración del UART
uart = machine.UART(0, baudrate=9600)  # Usa UART0, cambia el baudrate según necesites

while True:
    if uart.any():
        received_data = uart.read()  # Lee los datos disponibles en el buffer
        if received_data:  # Verifica que se hayan recibido datos
            print("Datos recibidos:", received_data)
            try:
                # Intenta decodificar los datos recibidos
                decoded_data = received_data.decode('utf-8')
                print("Decoded data:", decoded_data)
                # Envía una confirmación de vuelta a la computadora
                uart.write("Confirmación de llegada: " + decoded_data)
            except UnicodeDecodeError:
                # Maneja el caso donde los datos no puedan ser decodificados correctamente
                print("Error al decodificar los datos recibidos.")
    # Ejemplo de enviar un dato a la computadora cada 5 segundos
    utime.sleep(5)
    uart.write("Hola desde Pico\n")
