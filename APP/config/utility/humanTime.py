from datetime import datetime, timezone, timedelta
from APP.config.dotenvfile import GetEnv
from APP.config.log import LogProses

globals_offset = GetEnv("timezone_offset", "7").int()


class _convertime_to:
    def __init__(self):
        self.current_time = datetime.now(timezone.utc)
        self.result = None  # Properti untuk menyimpan hasil
        self.time_offset = 0

    def addOffset(self, hours: int = 0, minutes: int = 0, second: int = 0):
        self.current_time += timedelta(hours=hours, minutes=minutes, seconds=second)
        return self

    def addTime(self, addtime: int, inwhat: str):
        # Tambahkan waktu berdasarkan unit (H = jam, M = menit, S = detik)
        if inwhat == "H":
            self.current_time += timedelta(hours=addtime)
        elif inwhat == "M":
            self.current_time += timedelta(minutes=addtime)
        elif inwhat == "S":
            self.current_time += timedelta(seconds=addtime)
        # Simpan hasil update ke result
        return self

    def Human(self, timeFormat: str = "%Y-%m-%d %H:%M:%S"):
        # Format waktu dalam bentuk human-readable dan simpan ke result
        self.result = self.current_time.strftime(timeFormat)
        return self

    def Timestamp(self, simple: bool = True):
        # Simpan timestamp ke result
        if simple:
            self.result = int(self.current_time.timestamp())
        else:
            self.result = str(self.current_time.timestamp())

        return self

    def getResult(self) -> str:
        # Fungsi untuk mengembalikan hasil akhir
        return str(self.result)


class _convertime_from:
    def __init__(self):
        pass

    def Human(self, date_str: str, time_format: str = "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.strptime(date_str, time_format)
        except ValueError:
            LogProses(f"Format waktu tidak valid : {date_str},{time_format}")
            return f"Format waktu tidak valid {date_str}"

    def Timestamp(self, timestamp: float):
        return datetime.fromtimestamp(timestamp)


def GetTimeNow() -> _convertime_to:
    return _convertime_to()


def WhatTime() -> _convertime_from:
    return _convertime_from()
