""" calculates reports """
from reports import MonthReport, YearReport


class ReportCalculation:
    """Class to calculate a weather report"""

    def get_year_extreme_report(self, records):
        """
        calculate year extreme report
        Args:
            records: to generate extreme reports
        Returns:
            object of year report dataclass
        """
        highest_temp_record = max(records, key=lambda day: day.max_temperature_celcius)
        highest_temperature = highest_temp_record.max_temperature_celcius
        highest_temperature_day = highest_temp_record.pkt

        lowest_temp_record = min(records, key=lambda day: day.min_temperature_celcius)
        lowest_temperature = lowest_temp_record.min_temperature_celcius
        lowest_temperature_day = lowest_temp_record.pkt

        highest_humidity_record = max(records, key=lambda day: day.max_humidity)
        highest_humidity = highest_humidity_record.max_humidity
        highest_humidity_day = highest_humidity_record.pkt

        return YearReport(
            highest_temperature,
            highest_temperature_day,
            lowest_temperature,
            lowest_temperature_day,
            highest_humidity,
            highest_humidity_day,
        )

    def get_month_average_report(self, records):
        """
        calculate monthly average report
        Args:
            records: to generate average reports
        Returns:
            object of year report dataclass
        """
        sum_of_highest_temp = sum(day.max_temperature_celcius for day in records)
        average_highest_temperature = sum_of_highest_temp // len(records)

        sum_of_lowest_temperature = sum(day.min_temperature_celcius for day in records)
        average_lowest_temperature = sum_of_lowest_temperature // len(records)

        sum_of_mean_humidity = sum(day.mean_humidity for day in records)
        average_mean_humidity = sum_of_mean_humidity // len(records)

        return MonthReport(
            average_highest_temperature,
            average_lowest_temperature,
            average_mean_humidity,
        )
