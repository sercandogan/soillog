from enum import Enum
import os


class Pins(Enum):
    TEMP_HUMIDITY = os.getenv("PIN_TEMPERATURE_HUMIDITY")

    def __get__(self, instance, owner):
        return self.value


class Channels(Enum):
    MOISTURE_1 = os.getenv("CHANNEL_MOISTURE_1")
    MOISTURE_2 = os.getenv("CHANNEL_MOISTURE_2")

    def __get__(self, instance, owner):
        return self.value
