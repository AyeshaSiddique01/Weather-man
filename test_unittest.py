import datetime
import io
import sys
import unittest  # The test framework

from charts import Charts
from month_report import MonthReport
from utils import get_weather_data
from weather import Weather
from year_report import YearReport


class Test_TestFileReading(unittest.TestCase):
    '''
    Test get_weather_data function
    '''
    def test_get_weather_data(self):
        '''
        Test is the data feteched from the file is same as the expected data
        '''
        file_name = "/Users/ayshasiddique/Documents/Ayesha training/ayesha-2023-training/weatherfiles/Murree_weather_2010_Mar.txt"
        actual_result = get_weather_data(file_name)

        # Define your expected result
        expected_result = [
            Weather(
                pkt=datetime.datetime(2010, 3, 1, 0, 0),
                max_temperature_celcius=8,
                min_temperature_celcius=5,
                max_humidity=91,
                mean_humidity=76,
                min_humidity=43,
            ),
            Weather(
                pkt=datetime.datetime(2010, 3, 2, 0, 0),
                max_temperature_celcius=15,
                min_temperature_celcius=8,
                max_humidity=41,
                mean_humidity=29,
                min_humidity=20,
            ),
            Weather(
                pkt=datetime.datetime(2010, 3, 3, 0, 0),
                max_temperature_celcius=10,
                min_temperature_celcius=2,
                max_humidity=91,
                mean_humidity=56,
                min_humidity=24,
            ),
            Weather(
                pkt=datetime.datetime(2010, 3, 4, 0, 0),
                max_temperature_celcius=6,
                min_temperature_celcius=2,
                max_humidity=89,
                mean_humidity=79,
                min_humidity=61,
            ),
            Weather(
                pkt=datetime.datetime(2010, 3, 5, 0, 0),
                max_temperature_celcius=13,
                min_temperature_celcius=3,
                max_humidity=62,
                mean_humidity=50,
                min_humidity=27,
            ),
            Weather(
                pkt=datetime.datetime(2010, 3, 6, 0, 0),
                max_temperature_celcius=10,
                min_temperature_celcius=4,
                max_humidity=90,
                mean_humidity=64,
                min_humidity=38,
            ),
            Weather(
                pkt=datetime.datetime(2010, 3, 7, 0, 0),
                max_temperature_celcius=13,
                min_temperature_celcius=5,
                max_humidity=80,
                mean_humidity=54,
                min_humidity=27,
            ),
            Weather(
                pkt=datetime.datetime(2010, 3, 8, 0, 0),
                max_temperature_celcius=17,
                min_temperature_celcius=9,
                max_humidity=50,
                mean_humidity=29,
                min_humidity=14,
            ),
            Weather(
                pkt=datetime.datetime(2010, 3, 9, 0, 0),
                max_temperature_celcius=17,
                min_temperature_celcius=10,
                max_humidity=40,
                mean_humidity=26,
                min_humidity=18,
            ),
            Weather(
                pkt=datetime.datetime(2010, 3, 10, 0, 0),
                max_temperature_celcius=18,
                min_temperature_celcius=12,
                max_humidity=37,
                mean_humidity=24,
                min_humidity=14,
            ),
            Weather(
                pkt=datetime.datetime(2010, 3, 11, 0, 0),
                max_temperature_celcius=18,
                min_temperature_celcius=12,
                max_humidity=32,
                mean_humidity=26,
                min_humidity=21,
            ),
            Weather(
                pkt=datetime.datetime(2010, 3, 12, 0, 0),
                max_temperature_celcius=18,
                min_temperature_celcius=10,
                max_humidity=37,
                mean_humidity=33,
                min_humidity=27,
            ),
            Weather(
                pkt=datetime.datetime(2010, 3, 13, 0, 0),
                max_temperature_celcius=18,
                min_temperature_celcius=11,
                max_humidity=47,
                mean_humidity=36,
                min_humidity=27,
            ),
            Weather(
                pkt=datetime.datetime(2010, 3, 14, 0, 0),
                max_temperature_celcius=20,
                min_temperature_celcius=12,
                max_humidity=36,
                mean_humidity=25,
                min_humidity=18,
            ),
            Weather(
                pkt=datetime.datetime(2010, 3, 15, 0, 0),
                max_temperature_celcius=20,
                min_temperature_celcius=14,
                max_humidity=33,
                mean_humidity=23,
                min_humidity=12,
            ),
            Weather(
                pkt=datetime.datetime(2010, 3, 16, 0, 0),
                max_temperature_celcius=21,
                min_temperature_celcius=14,
                max_humidity=44,
                mean_humidity=30,
                min_humidity=20,
            ),
            Weather(
                pkt=datetime.datetime(2010, 3, 17, 0, 0),
                max_temperature_celcius=21,
                min_temperature_celcius=14,
                max_humidity=44,
                mean_humidity=35,
                min_humidity=29,
            ),
            Weather(
                pkt=datetime.datetime(2010, 3, 18, 0, 0),
                max_temperature_celcius=22,
                min_temperature_celcius=14,
                max_humidity=36,
                mean_humidity=32,
                min_humidity=28,
            ),
            Weather(
                pkt=datetime.datetime(2010, 3, 19, 0, 0),
                max_temperature_celcius=23,
                min_temperature_celcius=15,
                max_humidity=38,
                mean_humidity=32,
                min_humidity=26,
            ),
            Weather(
                pkt=datetime.datetime(2010, 3, 20, 0, 0),
                max_temperature_celcius=24,
                min_temperature_celcius=14,
                max_humidity=50,
                mean_humidity=37,
                min_humidity=24,
            ),
            Weather(
                pkt=datetime.datetime(2010, 3, 21, 0, 0),
                max_temperature_celcius=21,
                min_temperature_celcius=15,
                max_humidity=57,
                mean_humidity=44,
                min_humidity=33,
            ),
            Weather(
                pkt=datetime.datetime(2010, 3, 22, 0, 0),
                max_temperature_celcius=21,
                min_temperature_celcius=15,
                max_humidity=57,
                mean_humidity=50,
                min_humidity=42,
            ),
            Weather(
                pkt=datetime.datetime(2010, 3, 23, 0, 0),
                max_temperature_celcius=20,
                min_temperature_celcius=14,
                max_humidity=57,
                mean_humidity=46,
                min_humidity=40,
            ),
            Weather(
                pkt=datetime.datetime(2010, 3, 24, 0, 0),
                max_temperature_celcius=21,
                min_temperature_celcius=14,
                max_humidity=51,
                mean_humidity=44,
                min_humidity=35,
            ),
            Weather(
                pkt=datetime.datetime(2010, 3, 25, 0, 0),
                max_temperature_celcius=23,
                min_temperature_celcius=16,
                max_humidity=37,
                mean_humidity=32,
                min_humidity=26,
            ),
            Weather(
                pkt=datetime.datetime(2010, 3, 26, 0, 0),
                max_temperature_celcius=21,
                min_temperature_celcius=8,
                max_humidity=69,
                mean_humidity=50,
                min_humidity=34,
            ),
            Weather(
                pkt=datetime.datetime(2010, 3, 27, 0, 0),
                max_temperature_celcius=19,
                min_temperature_celcius=12,
                max_humidity=56,
                mean_humidity=48,
                min_humidity=40,
            ),
            Weather(
                pkt=datetime.datetime(2010, 3, 28, 0, 0),
                max_temperature_celcius=21,
                min_temperature_celcius=13,
                max_humidity=62,
                mean_humidity=41,
                min_humidity=27,
            ),
            Weather(
                pkt=datetime.datetime(2010, 3, 29, 0, 0),
                max_temperature_celcius=21,
                min_temperature_celcius=8,
                max_humidity=69,
                mean_humidity=44,
                min_humidity=30,
            ),
            Weather(
                pkt=datetime.datetime(2010, 3, 30, 0, 0),
                max_temperature_celcius=18,
                min_temperature_celcius=8,
                max_humidity=69,
                mean_humidity=52,
                min_humidity=44,
            ),
            Weather(
                pkt=datetime.datetime(2010, 3, 31, 0, 0),
                max_temperature_celcius=18,
                min_temperature_celcius=10,
                max_humidity=44,
                mean_humidity=37,
                min_humidity=33,
            ),
        ]
        self.assertEqual(actual_result, expected_result)

class Test_TestGraph(unittest.TestCase):
    '''
    Test graph class
    '''
    def test_printed_graph(self):
        '''
        Test weather draw graph function prints right or not
        '''
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        chart = Charts(
            [Weather(
                pkt=datetime.datetime(2010, 3, 1, 0, 0),
                max_temperature_celcius=8,
                min_temperature_celcius=5,
                max_humidity=91,
                mean_humidity=76,
                min_humidity=43,
            )]
            )
        chart.draw_graph()
        sys.stdout = sys.__stdout__
        # actual_result = capturedOutput.getvalue()
        # expected_result = f'''March 2010\n01 {BLUE}{5 * '+'}{RED}{8 * '+'} {
        #         WHITE}{5}C-{8}C\nMarch 2010\n01 {RED}{5 * '+'} {
        #         WHITE}{8}C\n01 {BLUE}{5 * '+'} {WHITE}{8}C\n'''
        # print (expected_result, actual_result)

class Test_TestMonthReport(unittest.TestCase):
    '''
    Test month report
    '''
    def test_get_average_highest_temperature(self):
        '''
        Test does the get_average_highest_temperature return the expected value
        '''
        month_report = MonthReport([Weather(
                pkt=datetime.datetime(2010, 3, 1, 0, 0),
                max_temperature_celcius=8,
                min_temperature_celcius=5,
                max_humidity=91,
                mean_humidity=76,
                min_humidity=43,
            ),
            Weather(
                pkt=datetime.datetime(2010, 3, 2, 0, 0),
                max_temperature_celcius=15,
                min_temperature_celcius=8,
                max_humidity=41,
                mean_humidity=29,
                min_humidity=20,
            )])
        actual_result = month_report.get_average_highest_temperature()
        # Define your expected result
        expected_result = 12
        self.assertEqual(actual_result, expected_result)

class Test_TestYearReport(unittest.TestCase):
    '''
    Test year report
    '''
    def test_get_highest_humidity_and_day(self):
        '''
        Test does the get_highest_humidity_and_day return the expected value
        '''
        year_report = YearReport([Weather(
                pkt=datetime.datetime(2010, 3, 1, 0, 0),
                max_temperature_celcius=8,
                min_temperature_celcius=5,
                max_humidity=91,
                mean_humidity=76,
                min_humidity=43,
            ),
            Weather(
                pkt=datetime.datetime(2010, 3, 2, 0, 0),
                max_temperature_celcius=15,
                min_temperature_celcius=8,
                max_humidity=41,
                mean_humidity=29,
                min_humidity=20,
            )])
        actual_result = year_report.get_highest_humidity_and_day()
        # Define your expected result
        expected_result = (91, datetime.datetime(2010, 3, 1, 0, 0))
        self.assertEqual(actual_result, expected_result)

if __name__ == "__main__":
    unittest.main()
