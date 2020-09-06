class WeatherData:

    def __init__(self, row):
        self.pkt = str(row["PKT"])
        self.max_temp = int(row["Max TemperatureC"]) if row["Max TemperatureC"] else None
        self.mean_temp = str(row["Mean TemperatureC"])
        self.min_temp = str(row["Min TemperatureC"])
        self.max_humidity = str(row["Max Humidity"])
        self.mean_humidity = str(row[" Mean Humidity"])
