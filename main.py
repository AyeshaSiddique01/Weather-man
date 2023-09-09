""" Driver File """
import argparse
from datetime import datetime

from data_storage import DataStorage
from report_calculations import ReportCalculation
from report_generator import ReportGenerator

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(
            description="Weatherman script for processing files"
        )
        parser.add_argument(
            "file_directory",
            help="Path of the directory containing files",
            type=str,
        )
        parser.add_argument(
            "-c",
            "--chart_month",
            help="Specify month(YYYY/MM) for bar_charts",
            type=lambda date: datetime.strptime(date, "%Y/%m"),
        )
        parser.add_argument(
            "-a",
            "--average_month",
            help="Specify month(YYYY/M) to get month's report",
            type=lambda date: datetime.strptime(date, "%Y/%m"),
        )
        parser.add_argument(
            "-e", "--report_year", help="Specify year to get year'd report", type=int
        )
        args = parser.parse_args()
    except IndexError:
        pass

    data_storage = DataStorage(args.file_directory)
    report_calculation = ReportCalculation()
    report_generator = ReportGenerator()
    if args.report_year:
        record = data_storage.filter_records(args.report_year)
        year_report = report_calculation.get_year_extreme_report(record)
        report_generator.display_year_report(year_report)

    if args.average_month:
        record = data_storage.filter_records(
            args.average_month.year, args.average_month.month
        )
        month_report = report_calculation.get_month_average_report(record)
        report_generator.disply_month_report(month_report)

    if args.chart_month:
        record = data_storage.filter_records(
            args.average_month.year, args.average_month.month
        )
        report_generator.display_temperature_bar_charts(record)
