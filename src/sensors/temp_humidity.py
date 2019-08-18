import Adafruit_DHT
from src.errors import Temp_Humidity_IOError


class TempHumidity(object):

    def __init__(self, pin):
        self.pin = pin
        self.sensor = Adafruit_DHT.DHT22

    def get_temp_humidity(self):
        humidity, temperature = Adafruit_DHT.read_retry(self.sensor, self.pin)
        if humidity and temperature:
            return {
                "temperature": temperature,
                "humidity": humidity
            }
        raise Temp_Humidity_IOError()
