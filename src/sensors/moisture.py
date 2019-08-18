import spidev
from gpiozero import MCP3008
from src.errors import Moisture_IOError


class Moisture(object):

    def __init__(self, channel):
        self.channel = channel
        self.spi = spidev.SpiDev()
        self.spi.open(0, 0)
        self.spi.max_speed_hz = 1000000  # 1MHz
        self.adc = MCP3008(self.channel)

    def get_moisture(self):
        adc = self.spi.xfer2([1, (8 + self.channel) << 4, 0])
        data = ((adc[1] & 3) << 8) + adc[2]
        if data:
            return data
        raise Moisture_IOError

    def get_voltage(self):
        voltage = self.adc.value
        if voltage:
            return self.adc.value * 3.3
        raise Moisture_IOError
