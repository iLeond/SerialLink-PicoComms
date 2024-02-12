import machine
import utime
# En Pico 1, usa "PICO_ID_1"; en Pico 2, usa "PICO_ID_2"
PICO_ID = "PICO_ID_2"  # Cambia este valor para el segundo Pico

class PicoUART:
    def __init__(self, baudrate=9600):
        self.uart = machine.UART(0, baudrate=baudrate)
    
    def send_greeting(self):
        message = f"{PICO_ID}: Hola desde la Pico\n"
        self.uart.write(message)
        print(message.strip())

    def listen_for_data(self):
        if self.uart.any():
            received_data = self.uart.read().decode('utf-8').strip()
            print(f"Dato recibido: {received_data}")
            response_message = f"{PICO_ID}: Dato recibido: {received_data}\n"
            self.uart.write(response_message.encode('utf-8'))

    def run(self):
        while True:
            self.send_greeting()
            self.listen_for_data()
            utime.sleep(5)

if __name__ == "__main__":
    uart_comm = PicoUART()
    uart_comm.run()
