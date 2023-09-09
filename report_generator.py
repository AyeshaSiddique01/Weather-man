"""Generates yearly and monthly reports and bar_charts of given month"""
from constants import BLUE, RED, WHITE
from utils import stringnify_date

# from reports import YearReport, MonthReport


class ReportGenerator:
    """Generates reports"""

    def display_year_report(self, year_report):
        """
        Displays year report
        """
        # Display highest temperature and day

        print(f"Highest: {year_report.highest_temperature}C", end=" ")
        print(f"on {stringnify_date(year_report.highest_temperature_day)}")

        print(f"Lowest: {year_report.lowest_temperature}C", end=" ")
        print(f"on {stringnify_date(year_report.lowest_temperature_day)}")

        print(f"Humidity: {year_report.highest_humidity}%", end=" ")
        print(f"on {stringnify_date(year_report.highest_humidity_day)}")

    def disply_month_report(self, month_report):
        """
        Displays a monthly weather report
        """

        print(f"Highest Average: {month_report.average_highest_temperature}C")
        print(f"Lowest Average: {month_report.average_lowest_temperature}C")
        print(f"Average Mean Humidity: {month_report.average_mean_humidity}%")

    def display_temperature_bar_charts(self, records):
        """Draw bar_charts of highest and lowest temperature of each day"""

        single_graph = ""
        seperate_graph = ""
        for day in records:
            date = day.pkt.strftime("%d")
            max_temp = day.max_temperature_celcius
            min_temp = day.min_temperature_celcius
            seperate_graph += f"{date} {RED}{max_temp * '+'} {WHITE}{max_temp}C\n\
{date} {BLUE}{min_temp * '+'} {WHITE}{min_temp}C\n"
            single_graph += f"{date} {BLUE}{min_temp * '+'}{RED}{max_temp * '+'} \
{WHITE}{min_temp}C-{max_temp}C\n"

        month = records[0].pkt
        formated_date = month.strftime("%B %Y")
        print(formated_date)
        print(single_graph)
        print(formated_date)
        print(seperate_graph)
