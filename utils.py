"""Helper functions for application"""
from enum import Enum


def stringnify_date(date):
    """
    Get stringnify date

    Args:
        date: date to stringnify

    Returns:
        Stringnify date with format (Mon day)
    """
    return date.strftime("%b %d")


class WeatherAttribute(Enum):
    """Enum for Weather Attribute"""

    DATE = "PKT"
    MAX_TEMP = "Max TemperatureC"
    MIN_TEMP = "Min TemperatureC"
    MAX_HUMIDITY = "Max Humidity"
    MEAN_HUMIDITY = "Mean Humidity"
    MIN_HUMIDITY = "Min Humidity"
