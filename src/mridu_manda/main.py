import sys
import threading
import time
from mridu_manda import fetch_city, http_call, parse_weather, print_weather
from rich.console import Console



def main():

    console = Console()
    
    if len(sys.argv) > 1 and sys.argv[1] == "-m":

        print("Welcome to MriduManda")
        time.sleep(1)
        print("A simple CLImate application!\n")
        time.sleep(1)

        console.print("Manual city entry mode enabled!", style="bold green")
        city = fetch_city.manual_city()

        with console.status("Fetching weather...", spinner="dqpb") as status:
            weather_report = http_call.make_call('w', city)
            time.sleep(1)
            status.update("Generating report...", spinner="dqpb")
            formatted_weather = parse_weather.weather_access(weather_report)
            time.sleep(1)
    else:

        print("Welcome to MriduManda")
        time.sleep(1)
        print("A simple CLImate application!\n")
        time.sleep(1)

        console.print("Auto city detection mode enabled!", style="bold green")

        with console.status("Detecting city...", spinner="dqpb") as status:
            city = fetch_city.auto_city()
            time.sleep(1)
            status.update("Fetching weather...", spinner="dqpb")
            weather_report = http_call.make_call('w', city)
            time.sleep(1)
            status.update("Generating report...", spinner="dqpb")
            formatted_weather = parse_weather.weather_access(weather_report)
            time.sleep(1)
    
    status.stop()
    print_weather.display(formatted_weather)