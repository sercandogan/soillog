from enum import Enum
import os


class Pins(Enum):
    TEMP_HUMIDITY = os.getenv("PIN_TEMPERATURE_HUMIDITY")

    def __get__(self, instance, owner):
        return self.value
