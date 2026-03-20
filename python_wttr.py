import requests
import json

class Fetcher:
    def __init__(self, location: str):
        self._forecast_json: dict = requests.get(f'https://wttr.in/{location}?format=j1').json()
        self.raw_current_forecast: dict = self._forecast_json["current_condition"][0]
        self.raw_general_weather: dict = self._forecast_json["weather"][0]
        self.forecast: Forecast = Forecast(raw_current_forecast=self.raw_current_forecast, raw_general_weather=self.raw_general_weather)

class Forecast:
    def __init__(self, raw_current_forecast: dict, raw_general_weather: dict):
        # Current Weather Data
        self.observation_time: str = raw_current_forecast["observation_time"]
        self.local_observation_time: str = raw_current_forecast["localObsDateTime"]

        self.temp_c: int = int(raw_current_forecast["temp_C"])
        self.temp_f: int = int(raw_current_forecast["temp_F"])
        self.feels_like_c: int = int(raw_current_forecast["FeelsLikeC"])
        self.feels_like_f: int = int(raw_current_forecast["FeelsLikeF"])

        self.windspeed_kph: int = int(raw_current_forecast["windspeedKmph"])
        self.windspeed_mph: int = int(raw_current_forecast["windspeedMiles"])
        self.wind_direction_degree: int = int(raw_current_forecast["winddirDegree"])
        self.wind_direction_compass: str = raw_current_forecast["winddir16Point"]

        self.precipitation_mm: float = float(raw_current_forecast["precipMM"])
        self.precipitation_inches: float = float(raw_current_forecast["precipInches"])
        self.humidity: int = int(raw_current_forecast["humidity"])

        self.pressure_milibar: int = int(raw_current_forecast["pressure"])
        self.pressure_inhg: int = int(raw_current_forecast["pressureInches"])
        self.cloud_cover: int = int(raw_current_forecast["cloudcover"])

        self.visibility_km: int = int(raw_current_forecast["visibility"])
        self.visibility_miles: int = int(raw_current_forecast["visibilityMiles"])

        self.weather_description: list = raw_current_forecast["weatherDesc"]

        # Current Day Forecast/Info
        self.date: str = raw_general_weather["date"]
        
        self.sunrise: str = raw_general_weather["astronomy"][0]["sunrise"]
        self.sunset: str = raw_general_weather["astronomy"][0]["sunset"]
        
        self.moonrise: str = raw_general_weather["astronomy"][0]["moonrise"]
        self.moonset: str = raw_general_weather["astronomy"][0]["moonset"]

        self.moon_phase: str = raw_general_weather["astronomy"][0]["moon_phase"]
        self.moon_illumination: int = int(raw_general_weather["astronomy"][0]["moon_illumination"])

        self.max_temp_c: int = int(raw_general_weather["maxtempC"])
        self.high_temp_c: int = int(raw_general_weather["maxtempC"])

        self.max_temp_f: int = int(raw_general_weather["maxtempF"])
        self.high_temp_f: int = int(raw_general_weather["maxtempF"])

        self.min_temp_c: int = int(raw_general_weather["mintempC"])
        self.low_temp_c: int = int(raw_general_weather["mintempC"])
        
        self.min_temp_f: int = int(raw_general_weather["mintempF"])
        self.low_temp_f: int = int(raw_general_weather["mintempF"])