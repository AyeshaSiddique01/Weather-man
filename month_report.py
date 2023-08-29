''' Generates and displays a monthly weather report '''


class MonthReport:
    '''Class to generate a monthly weather report'''

    def __init__(self, data_of_month) -> None:
        self.data_of_month = data_of_month

    def get_average_highest_temperature(self):
        '''
        Calculate average highest temperature of month

        Returns:
            Average highest temperature
        '''
        sum_of_highest_temp = sum(
            day.max_temperature_celcius for day in self.data_of_month
        )
        average = round(sum_of_highest_temp / len(self.data_of_month))
        return average

    def get_average_lowest_temperature(self):
        '''
        Calculate average lowest temperature of month

        Returns:
            Average lowest temperature
        '''
        sum_of_lowest_temperature = sum(
            day.min_temperature_celcius for day in self.data_of_month
        )
        average = round(sum_of_lowest_temperature / len(self.data_of_month))
        return average

    def get_average_mean_humidity(self):
        '''
        Calculate average mean humidity of month

        Returns:
            Average mean humidity
        '''
        sum_of_mean_humidity = sum(day.mean_humidity for day in self.data_of_month)
        average = round(sum_of_mean_humidity / len(self.data_of_month))
        return average

    def disply_report_of_month(self):
        '''
        Displays a monthly weather report
        '''
        print(f"Highest Average: {self.get_average_highest_temperature()}C")
        print(f"Lowest Average: {self.get_average_lowest_temperature()}C")
        print(f"Average Mean Humidity: {self.get_average_mean_humidity()}%")
