from src.sensors.temp_humidity import TempHumidity
from src.errors import Temp_Humidity_IOError
from src.writer import Writer

import time
import os

temp_humidity = TempHumidity()

while True:
    data = temp_humidity.get_temp_humidity()
    try:
        writer = Writer(**data)
        writer.save()
    except Temp_Humidity_IOError:
        # @TODO: Add logger
        pass
    time.sleep(os.getenv("RETRY_FREQUENCY"))
