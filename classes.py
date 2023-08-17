from colorama import Fore

class Weather :
    """Class to represent weather data for a specific day."""
    def __init__(self, PKT, max_temperature_cel, mean_temperature_cel, min_temperature_cel, dew_point_cel,
                 mean_dew_point_cel, min_dew_point_cel, max_humidity, mean_humidity, min_humidity,
                 max_sea_level_pressure_hPa,mean_sea_level_pressure_hPa, min_sea_level_pressure_hPa, 
                 max_visibility_km, mean_visibility_km, min_visibility_km, max_wind_speed_km_per_hour, 
                 mean_wind_speed_km_per_hour, max_gust_speed_km_per_hour, precipitation_mm, cloud_cover, events, 
                 wind_dir_degrees) -> None:
        self.PKT = PKT
        self.max_temperature_cel = int(max_temperature_cel) if max_temperature_cel else None
        self.mean_temperature_cel = int(mean_temperature_cel) if mean_temperature_cel else None
        self.min_temperature_cel = int(min_temperature_cel) if min_temperature_cel else None
        self.dew_point_cel = int(dew_point_cel) if dew_point_cel else None
        self.mean_dew_point_cel = int(mean_dew_point_cel) if mean_dew_point_cel else None
        self.min_dew_point_cel = int(min_dew_point_cel) if min_dew_point_cel else None
        self.max_humidity = int(max_humidity) if max_humidity else None
        self.mean_humidity = int(mean_humidity) if mean_humidity else None
        self.min_humidity = int(min_humidity) if min_humidity else None
        self.max_sea_level_pressure_hPa = float(max_sea_level_pressure_hPa) if max_sea_level_pressure_hPa else None
        self.mean_sea_level_pressure_hPa = float(mean_sea_level_pressure_hPa) if mean_sea_level_pressure_hPa else None
        self.min_sea_level_pressure_hPa = float(min_sea_level_pressure_hPa) if min_sea_level_pressure_hPa else None
        self.max_visibility_km = float(max_visibility_km) if max_visibility_km else None
        self.mean_visibility_km = float(mean_visibility_km) if mean_visibility_km else None
        self.min_visibility_km = float(min_visibility_km) if min_visibility_km else None
        self.max_wind_speed_km_per_hour = float(max_wind_speed_km_per_hour) if max_wind_speed_km_per_hour else None
        self.mean_wind_speed_km_per_hour = float(mean_wind_speed_km_per_hour) if mean_wind_speed_km_per_hour else None
        self.max_gust_speed_km_per_hour = float(max_gust_speed_km_per_hour) if max_gust_speed_km_per_hour else None
        self.precipitation_mm = float(precipitation_mm) if precipitation_mm else None
        self.cloud_cover = int(cloud_cover) if cloud_cover else None
        self.events = events
        self.wind_dir_degrees = int(wind_dir_degrees) if wind_dir_degrees else None
        
class YearReport:
    """Class to generate a yearly weather report."""
    def __init__(self, weather_list) -> None:
        self.weather_list = weather_list

    def get_highest_temperature_and_day(self):
        """Calculate and return the highest temperature and day of year."""
        highest_temperature = self.weather_list[0].max_temperature_cel
        highest_temperature_day = self.weather_list[0].PKT
        for i in self.weather_list:
            if i.max_temperature_cel and i.max_temperature_cel > highest_temperature:
                highest_temperature = i.max_temperature_cel
                highest_temperature_day = i.PKT
        
        return {"highest_temperature" : highest_temperature, "highest_temperature_day" : highest_temperature_day}

    def get_lowest_temperature_and_day(self):
        """Calculate and return the lowest temperature and day of year."""
        lowest_temperature = self.weather_list[0].min_temperature_cel
        lowest_temperature_day = self.weather_list[0].PKT
        for i in self.weather_list:
            if i.min_temperature_cel and i.min_temperature_cel < lowest_temperature:
                lowest_temperature = i.min_temperature_cel
                lowest_temperature_day = i.PKT
        
        return {"lowest_temperature" : lowest_temperature, "lowest_temperature_day" : lowest_temperature_day}

    def get_highest_humidity_and_day(self):
        """Calculate and return the most humid and day of year."""
        highest_humidity = self.weather_list[0].max_humidity     
        most_humid_day = self.weather_list[0].PKT
        for i in self.weather_list:
            if i.max_humidity and i.max_humidity > highest_humidity:
                highest_humidity = i.max_humidity
                most_humid_day = i.PKT
        
        return {"most_humid_day" : most_humid_day, "highest_humidity" : highest_humidity}

class MonthReport:
    """Class to generate a monthly weather report."""
    def __init__(self, weather_list) -> None:
        self.weather_list = weather_list
    
    def average(self, list_of_numbers):
        """Calculate the average of a list of numbers."""
        sum = 0
        for i in list_of_numbers:
            if i:
                sum += i
        return round(sum / len(list_of_numbers))

    def get_average_highest_temperature(self):
        """Calculate and return the average of the highest temperatures."""
        list_of_highest_temperature = []
        for i in self.weather_list:
            list_of_highest_temperature.append(i.max_temperature_cel)
        average = self.average(list_of_highest_temperature)
        return average
    
    def get_average_lowest_temperature(self):
        """Calculate and return the average of the lowest temperatures."""
        list_of_lowest_temperature = []
        for i in self.weather_list:
            list_of_lowest_temperature.append(i.min_temperature_cel)
        average = self.average(list_of_lowest_temperature)
        return average
    
    def get_average_mean_humidity(self):
        """Calculate and return the average of the mean humidity."""
        list_of_mean_humidity = []
        for i in self.weather_list:
            list_of_mean_humidity.append(i.mean_humidity)
        average = self.average(list_of_mean_humidity)
        return average
    
class charts:
    """Class to draw temperature charts."""
    def __init__(self, weather_list) -> None:
        self.weather_list = weather_list
    
    def draw_two_charts(self):
        ''' Draw charts of highest and lowest temperature of each day''' 
        for day in self.weather_list:
            date_of_day = day.PKT
            date = date_of_day.split("-")[2]
            if day.max_temperature_cel:
                max_temp = int(day.max_temperature_cel)
                print(date, end=' ')
                print(Fore.RED + max_temp*'+' + Fore.WHITE, end=" ")
                print(f"{max_temp}C")
            if day.min_temperature_cel:
                min_temp = int(day.min_temperature_cel)
                print(date, end=' ')
                print(Fore.BLUE + min_temp*'+' + Fore.WHITE, end=" ")
                print(f"{min_temp}C")
    
    def draw_one_graph(self):
        ''' Draw highest and lowest temperature chart of each day''' 
        for day in self.weather_list:
            date_of_day = day.PKT
            date = date_of_day.split("-")[2]
            max_temp = min_temp = 0
            if day.max_temperature_cel:
                print(date, end=' ')
                max_temp = int(day.max_temperature_cel)
                if day.min_temperature_cel:
                    min_temp = int(day.min_temperature_cel)
                    print(Fore.BLUE + min_temp*'+', end="")
                print(Fore.RED + max_temp*'+' + Fore.WHITE, end=" ")
            if day.min_temperature_cel:
                print(f"{min_temp}C-", end="")
            if day.max_temperature_cel:
                print(f"{max_temp}C")