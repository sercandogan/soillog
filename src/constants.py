from enum import Enum
from dotenv import load_dotenv, find_dotenv

import os

load_dotenv(find_dotenv())


class Pins(Enum):
    TEMP_HUMIDITY = int(os.getenv("PIN_TEMPERATURE_HUMIDITY"))

    def __get__(self, instance, owner):
        return self.value


class Channels(Enum):
    MOISTURE_1 = int(os.getenv("CHANNEL_MOISTURE_1"))
    MOISTURE_2 = int(os.getenv("CHANNEL_MOISTURE_2"))

    def __get__(self, instance, owner):
        return self.value
