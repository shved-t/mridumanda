import sys
import time
from mridu_manda import fetch_city, http_call, parse_weather, print_weather, report_generation
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
            time.sleep(0.5)
            weather_report = http_call.make_call('w', city)
            status.update("Generating report...", spinner="dqpb")
            time.sleep(0.5)
            formatted_weather = parse_weather.weather_access(weather_report)

    else:

        print("Welcome to MriduManda")
        time.sleep(1)
        print("A simple CLImate application!\n")
        time.sleep(1)

        console.print("Auto city detection mode enabled!", style="bold green")

        with console.status("Detecting city...", spinner="dqpb") as status:
            time.sleep(0.5)
            city = fetch_city.auto_city()
            status.update("Fetching weather...", spinner="dqpb")
            time.sleep(0.5)
            weather_report = http_call.make_call('w', city)
            status.update("Generating report...", spinner="dqpb")
            time.sleep(0.5)
            formatted_weather = parse_weather.weather_access(weather_report)
            
    
    status.stop()
    print_weather.display(formatted_weather)

    print("\nDo you want to generate the weather report? (y/n)")
    choice = input().lower()

    if choice == "y":
        report_generation.report_generation()