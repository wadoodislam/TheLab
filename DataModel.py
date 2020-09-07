from datetime import datetime


class WeatherData:

    def __init__(self, row):
        self.pkt = datetime.strptime(row["PKT"], '%Y-%m-%d')
        self.max_temp = int(row["Max TemperatureC"]) if row["Max TemperatureC"] else None
        self.mean_temp = str(row["Mean TemperatureC"]) if row["Mean TemperatureC"] else None
        self.min_temp = str(row["Min TemperatureC"]) if row["Min TemperatureC"] else None
        self.max_humidity = str(row["Max Humidity"]) if row["Max Humidity"] else None
        self.mean_humidity = str(row[" Mean Humidity"]) if row[" Mean Humidity"] else None
