from peewee import *
from datetime import datetime

DBNAME = "data/sensordata-{0}.db".format(datetime.strftime(datetime.today(), "%Y-%m-%d"))
db = SqliteDatabase(DBNAME)


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
