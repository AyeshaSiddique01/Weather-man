"""Testing Weatherman application"""
import argparse
import datetime
import io
import sys
import unittest

from data_storage import DataStorage
# from report_calculations import MonthReportCalculation

# from report_generator import ChartGenerator
from weather import Weather


class Test_TestFileReading(unittest.TestCase):
    """
    Test get_weather_data function
    """

    def __init__(self, testName, file_path):
        super(Test_TestFileReading, self).__init__(testName)
        self.file_path = file_path

    def test_get_weather_data(self):
        """
        Test is the data feteched from the file is same as the expected data
        """
        data_storage = DataStorage(self.file_path)
        actual_result = data_storage.filter_records(2010, 3)

        # Define your expected result
        first_day_data = Weather(
            pkt=datetime.datetime(2010, 3, 1, 0, 0),
            max_temperature_celcius=8,
            min_temperature_celcius=5,
            max_humidity=91,
            mean_humidity=76,
            min_humidity=43,
        )
        self.assertEqual(actual_result[0].pkt, first_day_data.pkt)


# class Test_TestGraph(unittest.TestCase):
#     """
#     Test graph class
#     """

#     def __init__(self, testName):
#         super(Test_TestGraph, self).__init__(testName)

#     def test_printed_graph(self):
#         """
#         Test weather draw graph function prints right or not
#         """
#         capturedOutput = io.StringIO()
#         sys.stdout = capturedOutput
#         chart_generator = ChartGenerator(
#             [
#                 Weather(
#                     pkt=datetime.datetime(2010, 3, 1, 0, 0),
#                     max_temperature_celcius=8,
#                     min_temperature_celcius=5,
#                     max_humidity=91,
#                     mean_humidity=76,
#                     min_humidity=43,
#                 )
#             ]
#         )
#         chart_generator.display_temperature_bar_charts()
#         sys.stdout = sys.__stdout__


# class Test_TestMonthReport(unittest.TestCase):
#     """
#     Test month report
#     """

#     def __init__(self, testName):
#         super(Test_TestMonthReport, self).__init__(testName)

#     def test_get_average_highest_temperature(self):
#         """
#         Test does the get_average_highest_temperature return the expected value
#         """
#         month_report_calculator = MonthReportCalculation(
#             [
#                 Weather(
#                     pkt=datetime.datetime(2010, 3, 1, 0, 0),
#                     max_temperature_celcius=8,
#                     min_temperature_celcius=5,
#                     max_humidity=91,
#                     mean_humidity=76,
#                     min_humidity=43,
#                 ),
#                 Weather(
#                     pkt=datetime.datetime(2010, 3, 2, 0, 0),
#                     max_temperature_celcius=15,
#                     min_temperature_celcius=8,
#                     max_humidity=41,
#                     mean_humidity=29,
#                     min_humidity=20,
#                 ),
#             ]
#         )
#         actual_result = month_report_calculator.get_average_highest_temperature()
#         # Define your expected result
#         expected_result = 11
#         self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Weatherman script for processing files"
    )
    parser.add_argument(
        "file_directory", help="Path of the directory containing files", type=str
    )
    args = parser.parse_args()

    suite = unittest.TestSuite()
    suite.addTest(Test_TestFileReading("test_get_weather_data", args.file_directory))
    # suite.addTest(Test_TestGraph("test_printed_graph"))
    # suite.addTest(Test_TestMonthReport("test_get_average_highest_temperature"))
    unittest.TextTestRunner(verbosity=2).run(suite)
