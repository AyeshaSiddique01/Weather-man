""" calculates reports """
from constants import BLUE, RED, WHITE


class YearReportCalculation:
    """Class to generate a yearly weather report"""

    def __init__(self, data_of_year):
        self.data_of_year = data_of_year

    def get_highest_temperature_day(self):
        """
        Get highest temperature and day of year

        Returns:
            Tuple (highest_temperature, day)
        """
        return max((day.max_temperature_celcius, day.pkt) for day in self.data_of_year)

    def get_lowest_temperature_day(self):
        """
        Get lowest temperature and day of year

        Returns:
            Tuple (lowest_temperature, day)
        """
        return min((day.min_temperature_celcius, day.pkt) for day in self.data_of_year)

    def get_highest_humidity_day(self):
        """
        Get highest humidity and day of year

        Returns:
            Tuple (highest_humidity, day)
        """
        return max((day.max_humidity, day.pkt) for day in self.data_of_year)


class MonthReportCalculation:
    """Class to generate a monthly weather report"""

    def __init__(self, data_of_month):
        self.data_of_month = data_of_month

    def get_average_highest_temperature(self):
        """
        Calculate average highest temperature of month

        Returns:
            Average highest temperature
        """
        sum_of_highest_temp = sum(
            day.max_temperature_celcius for day in self.data_of_month
        )
        return sum_of_highest_temp // len(self.data_of_month)

    def get_average_lowest_temperature(self):
        """
        Calculate average lowest temperature of month

        Returns:
            Average lowest temperature
        """
        sum_of_lowest_temperature = sum(
            day.min_temperature_celcius for day in self.data_of_month
        )
        return sum_of_lowest_temperature // len(self.data_of_month)

    def get_average_mean_humidity(self):
        """
        Calculate average mean humidity of month

        Returns:
            Average mean humidity
        """
        sum_of_mean_humidity = sum(day.mean_humidity for day in self.data_of_month)
        return sum_of_mean_humidity // len(self.data_of_month)


class ChartsCalculation:
    """Class to draw temperature charts"""

    def __init__(self, data_of_month):
        self.data_of_month = data_of_month

    def get_graph(self):
        """
        Generate single and seperate graphs
        Returns:
            Dictionary of single and seperate charts of highest and lowest temperature of each day
        """
        single_graph_string = ""
        seperate_graph_string = ""
        for day in self.data_of_month:
            date = day.pkt.strftime("%d")
            max_temp = day.max_temperature_celcius
            min_temp = day.min_temperature_celcius
            seperate_graph_string += f"{date} {RED}{max_temp * '+'} {WHITE}{max_temp}C\n\
{date} {BLUE}{min_temp * '+'} {WHITE}{min_temp}C\n"
            single_graph_string += f"{date} {BLUE}{min_temp * '+'}{RED}{max_temp * '+'} \
{WHITE}{min_temp}C-{max_temp}C\n"
        return {
            "single_graph_string": single_graph_string,
            "seperate_graph_string": seperate_graph_string,
        }
