from src.sensors.temp_humidity import TempHumidity
from src.sensors.moisture import Moisture
from src.errors import Temp_Humidity_IOError, Moisture_IOError
from src.writer import Writer
from src.constants import Pins, Channels

# env
from dotenv import load_dotenv, find_dotenv

import time
import os
# Logging
import logging

logging.basicConfig(filename='soillog.log', level=logging.ERROR, format='%(asctime)s %(levelname)s %(message)s')

load_dotenv(find_dotenv())

temp_humidity = TempHumidity(Pins.TEMP_HUMIDITY)
moisture_1 = Moisture(Channels.MOISTURE_1)
moisture_2 = Moisture(Channels.MOISTURE_2)

while True:
    try:
        temp_humidity_data = temp_humidity.get_temp_humidity()
        moisture_data = dict(moisture_1=moisture_1.get_moisture(),
                             moisture_2=moisture_2.get_moisture(),
                             moisture_1_voltage=moisture_1.get_voltage(),
                             moisture_2_voltage=moisture_2.get_voltage()
                             )
        data = {**temp_humidity_data, **moisture_data}

        writer = Writer(**data)
        writer.save()
    except Temp_Humidity_IOError:
        logging.error("Temperature & Humidity IO Error")
    except Moisture_IOError:
        logging.error("Moisture IO Error")
    except RuntimeError:
        logging.critical("Run time error")
    except Exception as msg:
        logging.critical(msg)

    time.sleep(int(os.getenv("RETRY_FREQUENCY")))
