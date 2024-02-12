import machine
import utime

# Configuración del UART
uart = machine.UART(0, baudrate=9600)  # Usa UART0, cambia el baudrate según necesites

print("Iniciando envío de mensajes...")  # Confirmación inicial

while True:
    # Enviar "Hola desde la Pico" cada 5 segundos
    mensaje = "Hola desde la Pico\n"
    uart.write(mensaje)
    print("Enviado:", mensaje)  # Imprimir el mensaje enviado
    utime.sleep(5)
