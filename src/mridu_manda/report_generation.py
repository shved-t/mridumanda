from mridu_manda import config, print_weather
from datetime import datetime

def format_date():
    weather_report = config.load_weather()

    formatted_report = {}

    for key, value in weather_report.items():
        date = key
        date_object = datetime.strptime(date, "%Y-%m-%d")
        date = date_object.strftime("%d %b")
        formatted_report[date] = value
    
    return formatted_report


def report_generation():
    report = format_date()

    printable_report = []

    for key, value in report.items():
        printable_report.append([key, value["location"], value["temperature"]])

    print_weather.print_report(printable_report)
