''' Driver File '''
import argparse
import glob
from datetime import datetime

from charts import Charts
from month_report import MonthReport
from utils import get_weather_data
from year_report import YearReport


def is_valid_date(date):
    '''
    Get date and format it

    Args:
        date: date to format

    Returns:
        Formatted date
    '''
    try:
        return datetime.strptime(date, "%Y/%m")
    except ValueError:
        raise argparse.ArgumentTypeError(f"Not a valid date: {date}")


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(
            description="Weatherman script for processing files"
        )
        parser.add_argument(
            "files_dir", help="Path of the directory containing files", type=str
        )
        parser.add_argument(
            "-c",
            "--for_chart",
            help="Specify month(YYYY/MM) for charts",
            type=is_valid_date,
        )
        parser.add_argument(
            "-a",
            "--for_average",
            help="Specify month(YYYY/M) to get month's report",
            type=is_valid_date,
        )
        parser.add_argument(
            "-e", "--for_year", help="Specify year to get year'd report", type=int
        )

        args = parser.parse_args()
        directory = args.files_dir
        for_charts = args.for_chart
        for_average = args.for_average
        for_year = args.for_year

        files = glob.glob(f"{directory}/*.txt", recursive=True)
        data_of_all_months = []
        for file in files:
            data_of_all_months += get_weather_data(file)

    except IndexError:
        pass

    if for_year:
        data_of_year = [
            day for day in data_of_all_months if day.pkt.year == int(for_year)
        ]
        report_of_year = YearReport(data_of_year)
        report_of_year.display_year_report()

    if for_average:
        data_of_month = [
            day
            for day in data_of_all_months
            if day.pkt.year == for_average.year and day.pkt.month == for_average.month
        ]
        report_of_month = MonthReport(data_of_month)
        report_of_month.disply_report_of_month()

    if for_charts:
        data_of_month = [
            day
            for day in data_of_all_months
            if day.pkt.year == for_charts.year and day.pkt.month == for_charts.month
        ]
        charts = Charts(data_of_month)
        charts.draw_graph()
