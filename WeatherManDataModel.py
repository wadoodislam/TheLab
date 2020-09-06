class DataModel:

    def __init__(self, pkt, max_temp, mean_temp, min_temp, dew_point, mean_dew_point, min_dew_point, max_humidity,
                 mean_humidity, min_humidity, max_pressure, mean_pressure, min_pressure, max_visibility,
                 mean_visibility, min_visibility, max_wind, mean_wind, min_wind, precipitation, cloud_cover, event,
                 wind_direction):
        self.pkt = pkt
        self.max_temp = max_temp
        self.mean_temp = mean_temp
        self.min_temp = min_temp
        self.dew_point = dew_point
        self.mean_dew_point = mean_dew_point
        self.min_dew_point = min_dew_point
        self.max_humidity = max_humidity
        self.mean_humidity = mean_humidity
        self.min_humidity = min_humidity
        self.max_pressure = max_pressure
        self.mean_pressure = mean_pressure
        self.min_pressure = min_pressure
        self.max_visibility = max_visibility
        self.mean_visibility = mean_visibility
        self.min_visibility = min_visibility
        self.max_wind = max_wind
        self.mean_wind = mean_wind
        self.min_wind = min_wind
        self.precipitation = precipitation
        self.cloud_cover = cloud_cover
        self.event = event
        self.wind_direction = wind_direction
