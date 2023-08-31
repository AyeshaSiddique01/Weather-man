""" Data Manipulator for weatherman application """
import glob
from csv import DictReader
from datetime import datetime

from constants import DATE_FORMAT
from weather import Weather


class DataStorage:
    """Fetch and manipulate data of the weather files"""

    def __init__(self, directory_path):
        """
        Get file directory and read data of all files

        Args:
            directory_path: directory of files

        Returns:
            list of data of all files
        """
        files = glob.glob(f"{directory_path}/*.txt", recursive=True)
        all_months_data = []
        for file in files:
            all_months_data += self.get_weather_data(file)

        self.all_months_data = all_months_data

    def get_weather_data(self, file_name):
        """
        Get file name and read data of it

        Args:
            file_name: Name of file

        Returns:
            list of weather of all days of month
        """
        weather_of_murree = []
        with open(file_name, "r", encoding="utf-8") as file:
            file_reader = DictReader(file, skipinitialspace=True)
            for row in file_reader:
                pkt = row.get("PKT") if row.get("PKT") else row.get("PKST")
                try:
                    weather = Weather(
                        datetime.strptime(pkt, DATE_FORMAT),
                        int(row.get("Max TemperatureC")),
                        int(row.get("Min TemperatureC")),
                        int(row.get("Max Humidity")),
                        int(row.get("Mean Humidity")),
                        int(row.get("Min Humidity")),
                    )
                    weather_of_murree.append(weather)
                except (ValueError, TypeError):
                    pass
        return weather_of_murree

    def get_year_data(self, year):
        """
        Get year and filter data of that year

        Args:
            year: year of which data is required

        Returns:
            list of weather of all days of that year
        """
        return [day for day in self.all_months_data if day.pkt.year == year]

    def get_month_data(self, date):
        """
        Get date and filter data of that month

        Args:
            date: date(year/month) of which data is required

        Returns:
            list of weather of all days of that date
        """
        return [
            day
            for day in self.all_months_data
            if day.pkt.year == date.year and day.pkt.month == date.month
        ]
