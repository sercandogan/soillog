from peewee import *
from datetime import datetime
import os

# db = SqliteDatabase(os.getenv("DB_NAME"))
db = SqliteDatabase("sensordata.db")


class BaseModel(Model):
    class Meta:
        database = db


class Sensor(BaseModel):
    created_date = DateTimeField(default=datetime.now)
    temperature = FloatField()
    humidity = FloatField()
    # moisture = FloatField()


def create_tables():
    with db:
        db.create_tables([Sensor, ])
