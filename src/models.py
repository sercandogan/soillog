from peewee import *
from datetime import datetime
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())
db = SqliteDatabase(os.getenv("DB_NAME"))


class BaseModel(Model):
    class Meta:
        database = db


class Sensor(BaseModel):
    created_date = DateTimeField(default=datetime.now)
    temperature = FloatField()
    humidity = FloatField()
    moisture_1 = IntegerField()
    moisture_1_voltage = FloatField()
    moisture_2 = IntegerField()
    moisture_2_voltage = FloatField()


def create_tables():
    with db:
        db.create_tables([Sensor, ])
