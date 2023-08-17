import sys
from classes import *

def get_month(month):
    """
    Gets month index (1-12)
    Returns abbreviated month name (Jan-Dec)
    """
    month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    return f"{month_names[month-1]}"

def get_month_full_name(month):
    """
    Gets month index (1-12)
    Returns full month name (January-December)
    """
    month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return f"{month_names[month-1]}"

def get_name_of_file(year, month, directory):
    """
    Gets year, month, and directory
    Returns formatted file name
    """
    month_name = get_month(month)
    return f"{directory}/Murree_weather_{year}_{month_name}.txt"

def reading_file(file_name):
    """
    Reads weather data of a month from a file
    Returns a list of Weather objects
    """
    list_of_weather = []
    with open(file_name) as f:
        f.readline()
        data = f.readline().removesuffix("\n")
        while data:
            data_list = data.split(",")
            weather = Weather(*data_list)
            list_of_weather.append(weather)
            data = f.readline().removesuffix("\n")
    return list_of_weather

def report_of_year(directory, year):
    """
    Generates and displays a yearly weather report
    """
    weather_list = []
    for i in range(0, 12):
        file_name = get_name_of_file(year, i, directory)
        weather_list += reading_file(file_name)

    year_report = YearReport(weather_list)
    
    # Display highest temperature and day
    highest_temperature_and_day = year_report.get_highest_temperature_and_day()
    highest_temperature_day = highest_temperature_and_day.get("highest_temperature_day").split("-")
    month = int(highest_temperature_day[1])
    print(f"Highest: {highest_temperature_and_day.get('highest_temperature')}C on {get_month_full_name(month)} {highest_temperature_day[2]}")
    
    # Display lowest temperature and day
    lowest_temperature_and_day = year_report.get_lowest_temperature_and_day()
    lowest_temperature_day = lowest_temperature_and_day.get("lowest_temperature_day").split("-")
    month = int(lowest_temperature_day[1])
    print(f"Lowest: {lowest_temperature_and_day.get('lowest_temperature')}C on {get_month_full_name(month)} {lowest_temperature_day[2]}")
    
    # Display highest humid and day
    get_highest_humidity_and_day = year_report.get_highest_humidity_and_day()
    most_humid_day = get_highest_humidity_and_day.get("most_humid_day").split("-")
    month = int(most_humid_day[1])
    print(f"Humidity: {get_highest_humidity_and_day.get('highest_humidity')}% on {get_month_full_name(month)} {most_humid_day[2]}")

def report_of_a_month(year, month, directory):
    """
    Generates and displays a monthly weather report
    """
    file_name = get_name_of_file(year, month, directory)
    weather_list = reading_file(file_name)
    month_report = MonthReport(weather_list)

    print(f"Highest Average: {month_report.get_average_highest_temperature()}C")
    print(f"Lowest Average: {month_report.get_average_lowest_temperature()}C")
    print(f"Average Mean Humidity: {month_report.get_average_mean_humidity()}")

def draw_charts(year, month, directory):
    """
    Draws temperature charts for each day of a specific month
    """
    month_name = get_month_full_name(month)
    print(f"{month_name} {year}")
    file_name = get_name_of_file(year, month, directory)
    weather_list = reading_file(file_name)
    chart = charts(weather_list)
    chart.draw_two_charts()
    print(f"{month_name} {year}")
    chart.draw_one_graph()

if __name__ == "__main__":
    try:
        arguments = sys.argv
        directory = arguments[1]

        if len(arguments) > 2:
            for i in range(2, len(arguments), 2):
                print("```````````````````````")
                if arguments[i] == "-e":
                    report_of_year(directory, arguments[i + 1])
                elif arguments[i] == "-a":
                    split_month_and_year = arguments[i + 1].split("/")
                    report_of_a_month(int(split_month_and_year[0]), int(split_month_and_year[1]), directory)
                elif arguments[i] == "-c":
                    split_month_and_year = arguments[i + 1].split("/")
                    draw_charts(int(split_month_and_year[0]), int(split_month_and_year[1]), directory)
    except Exception as e:
        print(e)
        raise e