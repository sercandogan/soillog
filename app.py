from src.models import create_tables
from os.path import join, dirname
from dotenv import load_dotenv
from src.sensors.temp_humidity import TempHumidity
from src.errors import Temp_Humidity_IOError
from src.writer import Writer

import time
import os

# Create .env file path.
dotenv_path = join(dirname(__file__), '.env')

# Load file from the path.
load_dotenv(dotenv_path)

# Create Tables
create_tables()
# @TODO: Find solution for daily db creation

while True:
    data = TempHumidity.get_temp_humidity()
    try:
        writer = Writer(**data)
        writer.save()
    except Temp_Humidity_IOError:
        # @TODO: Add logger
        pass
    time.sleep(os.getenv("RETRY_FREQUENCY"))
