"""  Reports data class """
from dataclasses import dataclass
from datetime import datetime


@dataclass
class YearReport:
    """Class to store year report"""

    highest_temperature: int
    highest_temperature_day: datetime
    lowest_temperature: int
    lowest_temperature_day: datetime
    highest_humidity: int
    highest_humidity_day: datetime


@dataclass
class MonthReport:
    """Class to store month report"""

    average_highest_temperature: int
    average_lowest_temperature: int
    average_mean_humidity: int
