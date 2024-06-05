from sds.db.repositories.sensor import SensorsDataRepository


class DB:
    sensor_data_repo = SensorsDataRepository("sensors", "sensors_data")
