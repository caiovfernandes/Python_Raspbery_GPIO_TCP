import RPi.GPIO as GPIO
import time
import Adafruit_DHT

class GPIOClass():
    def __init__(self, pino):
        self.pino = pino
        self.status = False


    def get_state(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pino, GPIO.IN)

        try:
            state = GPIO.input(self.pino)
            if (state):
                # print("ON")
                self.status = True
            else:
                # print("OFF")
                self.status = False
        except KeyboardInterrupt:
            pass
        finally:
            GPIO.cleanup()

    def set_state(self, status, pino):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(pino, GPIO.OUT)
        if status:
            GPIO.output(pino, GPIO.HIGH)
            time.sleep(1)
        elif not status:
            GPIO.output(pino, GPIO.LOW)

    def get_temperatura_humidade(self, pino):
        humidade, temperatura = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, pino)
        return round(temperatura,4), round(humidade,4)