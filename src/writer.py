from src.models import Sensor


class Writer(object):

    def __init__(self, **sensor_data):
        self.sensor_data = sensor_data

    def validation(self):
        pass

    def save(self):
        return Sensor.create(temperature=self.sensor_data["temperature"],
                             humidity=self.sensor_data["humidity"],
                             moisture_1=self.sensor_data["moisture_1"],
                             moisture_2=self.sensor_data["moisture_2"],
                             moisture_1_voltage=self.sensor_data["moisture_1_voltage"],
                             moisture_2_voltage=self.sensor_data["moisture_2_voltage"]
                             )
