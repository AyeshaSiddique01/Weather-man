"""Generates yearly and monthly reports and charts of given month"""
from report_calculations import (
    ChartsCalculation,
    MonthReportCalculation,
    YearReportCalculation,
)
from utils import stringnify_date


class YearReportGenerator:
    """Generates year report"""

    def __init__(self, year_data):
        self.year_report = YearReportCalculation(year_data)

    def display_year_report(self):
        """
        Displays year report
        """
        # Display highest temperature and day
        highest_temperature_day = self.year_report.get_highest_temperature_day()
        print(f"Highest: {highest_temperature_day[0]}C", end=" ")
        print(f"on {stringnify_date(highest_temperature_day[1])}")

        lowest_temperature_day = self.year_report.get_lowest_temperature_day()
        print(f"Lowest: {lowest_temperature_day[0]}C", end=" ")
        print(f"on {stringnify_date(lowest_temperature_day[1])}")

        highest_humidity_day = self.year_report.get_highest_humidity_day()
        print(f"Humidity: {highest_humidity_day[0]}%", end=" ")
        print(f"on {stringnify_date(highest_humidity_day[1])}")


class MonthReportGenerator:
    """Generates month report"""

    def __init__(self, month_data):
        self.month_report = MonthReportCalculation(month_data)

    def disply_month_report(self):
        """
        Displays a monthly weather report
        """
        print(
            f"Highest Average: {self.month_report.get_average_highest_temperature()}C"
        )
        print(f"Lowest Average: {self.month_report.get_average_lowest_temperature()}C")
        print(
            f"Average Mean Humidity: {self.month_report.get_average_mean_humidity()}%"
        )


class ChartGenerator:
    """Generates month's charts"""

    def __init__(self, month_data) -> None:
        self.chart = ChartsCalculation(month_data)
        self.month_data = month_data

    def display_charts(self):
        """Draw charts of highest and lowest temperature of each day"""
        month = self.month_data[0].pkt
        formated_date = month.strftime("%B %Y")
        charts = self.chart.get_graph()
        print(formated_date)
        print(charts.get("single_graph_string"))
        print(formated_date)
        print(charts.get("seperate_graph_string"))
