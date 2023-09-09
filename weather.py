"""  Weather class """
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Weather:
    """Class to represent weather record for a specific day"""

    pkt: datetime
    max_temperature_celcius: int
    min_temperature_celcius: int
    max_humidity: int
    mean_humidity: int
    min_humidity: int
