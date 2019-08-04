from src.models import Sensor


class Writer(object):

    def __init__(self, **sensors):
        self.sensors = sensors

    def validation(self):
        pass

    def save(self):
        return Sensor.create(temperature=self.sensors["temperature"],
                             humidity=self.sensors["humidity"],
                             )
