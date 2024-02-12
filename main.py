import machine
import utime

class PicoUART:
    def __init__(self, baudrate=9600):
        self.uart = machine.UART(0, baudrate=baudrate)
    
    def send_greeting(self):
        message = "Hola desde la Pico\n"
        self.uart.write(message)
        print(message.strip())  # Para depuración

    def listen_for_data(self):
        if self.uart.any():
            received_data = self.uart.read().decode('utf-8').strip()
            print(f"Dato recibido: {received_data}")  # Confirmación de la recepción para depuración
            response_message = f"Dato recibido: {received_data}\n"
            self.uart.write(response_message.encode('utf-8'))  # Asegúrate de codificar la respuesta

    def run(self):
        while True:
            self.send_greeting()
            self.listen_for_data()
            utime.sleep(5)

if __name__ == "__main__":
    uart_comm = PicoUART()
    uart_comm.run()
