''' Generates and displays a yearly weather report '''


class YearReport:
    '''Class to generate a yearly weather report'''

    def __init__(self, data_of_year) -> None:
        self.data_of_year = data_of_year

    def get_highest_temperature_and_day(self):
        '''
        Get highest temperature and day

        Returns:
            Tuple of highest temperature and day of Highest temperature
        '''
        return max((day.max_temperature_celcius, day.pkt) for day in self.data_of_year)

    def get_lowest_temperature_and_day(self):
        '''
        Get lowest temperature and day

        Returns:
            Tuple of lowest temperature and day of lowest temperature
        '''
        return min((day.min_temperature_celcius, day.pkt) for day in self.data_of_year)

    def get_highest_humidity_and_day(self):
        '''
        Get lowest temperature and day

        Returns:
            Tuple of highest humidity and day of highest humidity
        '''
        return max((day.max_humidity, day.pkt) for day in self.data_of_year)

    def format_date(self, date):
        '''
        Get formatted date

        Args:
            date: date to format

        Returns:
            Date with format (Mon day)
        '''
        return date.strftime("%b %d")

    def display_year_report(self):
        '''
        Displays year report
        '''
        # Display highest temperature and day
        highest_temperature_and_day = self.get_highest_temperature_and_day()
        print(f'''Highest: {highest_temperature_and_day[0]}C''', end=" ")
        print(f'''on {self.format_date(highest_temperature_and_day[1])}''')

        lowest_temperature_and_day = self.get_lowest_temperature_and_day()
        print(f'''Lowest: {lowest_temperature_and_day[0]}C''', end=" ")
        print(f'''on {self.format_date(lowest_temperature_and_day[1])}''')

        highest_humidity_and_day = self.get_highest_humidity_and_day()
        print(f'''Humidity: {highest_humidity_and_day[0]}%''', end=" ")
        print(f'''on {self.format_date(highest_humidity_and_day[1])}''')
