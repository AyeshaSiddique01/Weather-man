"""  Weather class """
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Weather:
    """Class to represent weather data for a specific day"""

    pkt: datetime
    max_temperature_celcius: int
    min_temperature_celcius: int
    max_humidity: int
    mean_humidity: int
    min_humidity: int

    def __init__(
        self,
        pkt,
        max_temperature_celcius,
        min_temperature_celcius,
        max_humidity,
        mean_humidity,
        min_humidity,
    ):
        self.pkt = pkt
        self.max_temperature_celcius = max_temperature_celcius
        self.min_temperature_celcius = min_temperature_celcius
        self.max_humidity = max_humidity
        self.mean_humidity = mean_humidity
        self.min_humidity = min_humidity
