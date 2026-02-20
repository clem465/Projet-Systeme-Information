import random
import time
from dataclasses import dataclass


@dataclass(frozen=True)
class WeatherMeasures:
    temperature: int
    humidity: int
    pressure: int


class DisplayPublisher:
    def __init__(self, *displays):
        self.__displays = displays

    def publish(self, measures):
        for display in self.__displays:
            display.display(
                measures.temperature,
                measures.humidity,
                measures.pressure,
            )

class StatsDisplay:
    def display(self, temperature, humidity, pressure):
        print(f"Stats - Temperature: {temperature}°C, Humidity: {humidity}%, Pressure: {pressure} hPa")
    
class RealtimeDisplay:
    def display(self, temperature, humidity, pressure):
        print(f"Realtime - Temperature: {temperature}°C, Humidity: {humidity}%, Pressure: {pressure} hPa")

class DailyMaxDisplay:
    def __init__(self):
        self.max_temperature = 0
        self.max_humidity = 0
        self.max_pressure = 0
    
    def calculate_max(self, temperature, humidity, pressure):
        if temperature > self.max_temperature:
            self.max_temperature = temperature
        if humidity > self.max_humidity:
            self.max_humidity = humidity
        if pressure > self.max_pressure:
            self.max_pressure = pressure

    def display(self, temperature, humidity, pressure):
        self.max_temperature = max(self.max_temperature, temperature)
        self.max_humidity = max(self.max_humidity, humidity)
        self.max_pressure = max(self.max_pressure, pressure)
        print(f"Daily Max - Max Temperature: {self.max_temperature}°C, Max Humidity: {self.max_humidity}%, Max Pressure: {self.max_pressure} hPa")

class WeatherStation:
    def __init__(self, display_publisher):
        self.__display_publisher = display_publisher

    def get_temperature(self):
        return random.randint(-30, 50)
    
    def get_humidity(self):
        return random.randint(0, 100)
    
    def get_pressure(self):
        return random.randint(800, 1300)

    def read_measures(self):
        return WeatherMeasures(
            temperature=self.get_temperature(),
            humidity=self.get_humidity(),
            pressure=self.get_pressure(),
        )
    
    def mesures_changed(self):
        self.__display_publisher.publish(self.read_measures())
        
        
if __name__ == "__main__":
    stats = StatsDisplay()
    real_time = RealtimeDisplay()
    daily_max = DailyMaxDisplay()
    publisher = DisplayPublisher(stats, real_time, daily_max)
    polar_station = WeatherStation(publisher)
    
    for _ in range(10):
        polar_station.mesures_changed()
        time.sleep(1)
        
