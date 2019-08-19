from playhouse.dataset import DataSet
from datetime import datetime

db = DataSet("sqlite:///sensordata.db")
table = db["sensor"]

db.freeze(table.all(),
          format="csv",
          filename="sensordata-{0}.csv".format(datetime.strftime(datetime.today(), "%Y-%m-%d")))
