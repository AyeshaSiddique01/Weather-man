""" Driver File """
import argparse

from data_storage import DataStorage
from report_generator import ChartGenerator, MonthReportGenerator, YearReportGenerator
from utils import format_date

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
            help="Specify month(YYYY/MM) for charts",
            type=format_date,
        )
        parser.add_argument(
            "-a",
            "--average_month",
            help="Specify month(YYYY/M) to get month's report",
            type=format_date,
        )
        parser.add_argument(
            "-e", "--report_year", help="Specify year to get year'd report", type=int
        )
        args = parser.parse_args()
    except IndexError:
        pass

    data_storage = DataStorage(args.file_directory)
    if args.report_year:
        data_of_year = data_storage.get_year_data(args.report_year)
        year_report_generator = YearReportGenerator(data_of_year)
        year_report_generator.display_year_report()

    if args.average_month:
        data_of_month = data_storage.get_month_data(args.average_month)
        month_report_generator = MonthReportGenerator(data_of_month)
        month_report_generator.disply_month_report()

    if args.chart_month:
        data_of_month = data_storage.get_month_data(args.chart_month)
        charts_generator = ChartGenerator(data_of_month)
        charts_generator.display_charts()
