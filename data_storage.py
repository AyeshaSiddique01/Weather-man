""" Data Manipulator for weatherman application """
import glob
from csv import DictReader
from datetime import datetime

from constants import DATE_FORMAT
from utils import WeatherAttribute
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
        all_months_record = []

        for file in files:
            all_months_record += self.get_weather_record(file)

        self.all_months_record = all_months_record

    def get_weather_record(self, file_name):
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
                if self.is_valid_record(row):
                    weather_of_murree.append(self.create_weather_object(row))

        return weather_of_murree

    def filter_records(self, year, month=None):
        """
        Get date and filter data of that month or year

        Args:
            year: year of which data is required
            month: month of that year of which data is required(optional)

        Returns:
            list of weather of all days of that date
        """
        if month:
            return [
                day
                for day in self.all_months_record
                if day.pkt.year == year and day.pkt.month == month
            ]

        return [day for day in self.all_months_record if day.pkt.year == year]

    def is_valid_record(self, record):
        """
            Validate is record is valid or not
        Args:
            record: data to validate
        Returns:
            bolean if data is valid returns ture else false
        """
        if (
            (record.get(WeatherAttribute.DATE.value) or record["PKST"])
            and record.get(WeatherAttribute.MAX_TEMP.value)
            and record.get(WeatherAttribute.MIN_TEMP.value)
            and record.get(WeatherAttribute.MAX_HUMIDITY.value)
            and record.get(WeatherAttribute.MEAN_HUMIDITY.value)
            and record.get(WeatherAttribute.MIN_HUMIDITY.value)
        ):
            return True
        return False

    def create_weather_object(self, record):
        """
        Creates object of weather of corresponding record
        Args:
            record: dictionary object to create object
        Returns:
            weather object of that record
        """
        pkt = record.get(WeatherAttribute.DATE.value) or record["PKST"]
        return Weather(
            datetime.strptime(pkt, DATE_FORMAT),
            int(record[WeatherAttribute.MAX_TEMP.value]),
            int(record[WeatherAttribute.MIN_TEMP.value]),
            int(record[WeatherAttribute.MAX_HUMIDITY.value]),
            int(record[WeatherAttribute.MEAN_HUMIDITY.value]),
            int(record[WeatherAttribute.MIN_HUMIDITY.value]),
        )
