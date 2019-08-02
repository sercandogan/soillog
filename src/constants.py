from enum import Enum

class Pins(Enum):
    TEMP_HUMIDITY = 3
    MOISTURE_1 = 5


    def __get__(self, instance, owner):
        return self.value