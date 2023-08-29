''' Helper functions for weatherman application '''
from csv import DictReader
from datetime import datetime

from constants import DATE_FORMAT
from weather import Weather


def get_weather_data(file_name):
    '''
    Get file data and read data of it

    Args:
        file_name: Name of file

    Returns:
        list of weather of all days of month
    '''
    weather_of_murree = []
    with open(file_name, "r", encoding="utf-8") as file:
        file_reader = DictReader(file, skipinitialspace=True)
        for row in file_reader:
            pkt = row.get("PKT")
            if not pkt:
                pkt = row.get("PKST")

            try:
                weather = Weather(
                    datetime.strptime(pkt, DATE_FORMAT),
                    int(row.get("Max TemperatureC", None)),
                    int(row.get("Min TemperatureC", None)),
                    int(row.get("Max Humidity", None)),
                    int(row.get("Mean Humidity", None)),
                    int(row.get("Min Humidity", None)),
                )
                weather_of_murree.append(weather)
            except (ValueError, TypeError):
                pass
    return weather_of_murree
