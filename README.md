# soillog

Soillog is a data collection module based on Raspberry PI with Temperature, Humidity and Moisture Sensors (Extendible). It provides an easy structure that allow everyone to design experiments in their garden to analyise and optimize irrigation adequacy. 

## Requirements

- Raspberry PI
- ADC Converter (MCP3008)
- Moisture Sensor 
- Temperature and Humidity Sensor (DHT22)

## Installation

### Prerequisites

soillog is using SQLite as a database
```bash
sudo apt-get install sqlite3
```

Install dependencies:
```bash
pip install -r requirements.txt
```

### Configration

Edit `env.dist` and change as `.env`

```.env
#PINS AND CHANNELS (ADC - MCP3008)
PIN_TEMPERATURE_HUMIDITY=21
CHANNEL_MOISTURE_1=0
CHANNEL_MOISTURE_2=1

# General Config
RETRY_FREQUENCY=3 #second
DB_NAME="sensordata.db" # path
```

Recommended running process is with [Supervisor](http://supervisord.org/)

### Quick Start

Running the application:

```bash
python app.py
```

## Todo

- Circuit diagram
- Supervisor configration
- Backup
