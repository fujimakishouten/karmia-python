# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:



# Import modules
import calendar
import datetime
import math
from typing import Union


# Variables
days = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday'
]
month = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]


class KarmiaUtilityDate:
    def __init__(self, options: Union[dict, None]=None):
        options = options or {}
        self.offset = options.get("offset", datetime.timedelta(0))
        self.days = options.get("days", days)
        self.month = options.get("month", month)
        self.date = options.get("date", None)
        if not isinstance(self.date, datetime.datetime):
            self.date = None


    def set_date(self, date: datetime.datetime) -> "KarmiaUtilityDate":
        """
        Set date

        :param datetime.datetime date:
        :rtype: KarmiaUtilityDate
        """
        self.date = date

        return self

    def set_offset(self, offset: datetime.timedelta) -> "KarmiaUtilityDate":
        """
        Set offset

        :param datetime.timedelta offset:
        :rtype: KarmiaUtilityDate
        """
        self.offset = offset

        return self

    def get_offset(self):
        """
        Get current offset datetime.timedelta object

        :rtype: datetime.timedelta
        """
        return self.offset

    def get_date(self):
        """
        Get current datetime.datetime object

        :rtype: datetime.datetime
        """
        return self.date if self.date else datetime.datetime.now()

    def get_time(self):
        """
        Get current unix timestamp

        :rtype: float
        """
        return self.get_date().timestamp()

    def get_ymd(self):
        """
        Get current Year/Month/Date dict

        :rtype: dict
        """
        date = self.get_date()
        current = date - self.offset

        return {
            "year": current.year,
            "month": current.month,
            "date": current.day
        }

    def format(self, format: str, date: Union[datetime.datetime, None]=None) -> str:
        """
        Get formatted date/time string

        :param str format:
        :param datetime.datetime date: Optional
        :rtype: str
        """
        def convert(value: str) -> str:
            if value == "d":
                return date.strftime("%d")
            elif value == "D":
                return days[date.weekday()][:3]
            elif value == "j":
                return str(date.day)
            elif value == "l":
                return days[date.weekday()]
            elif value == "N":
                return str(date.isoweekday())
            elif value == "S":
                index = date.day - 1
                return ["st", "nd", "rd"][index] if index < 3 else "th"
            elif value == "w":
                return date.strftime("%w")
            elif value == "z":
                return str(int(date.strftime("%j"), 10) - 1)
            elif value == "W":
                return str(int(date.strftime("%V"), 10))
            elif value == "F":
                return self.month[date.month - 1]
            elif value == "m":
                return date.strftime("%m")
            elif value == "M":
                return month[date.month - 1][:3]
            elif value == "n":
                return str(date.month)
            elif value == "t":
                return str(calendar.monthrange(date.year, date.month)[1])
            elif value == "L":
                return "1" if calendar.isleap(date.year) else "0"
            elif value == "o":
                return date.isoformat()[:4]
            elif value == "Y":
                return date.strftime("%Y")
            elif value == "y":
                return date.strftime("%y")
            elif value == "a":
                return date.strftime("%p").lower()
            elif value == "A":
                return date.strftime("%p").upper()
            elif value == "B":
                utc = datetime.datetime.utcfromtimestamp(date.timestamp())
                offset = utc.timestamp() - date.timestamp() + 3600
                seconds = (date.hour * 60 * 60) + (date.minute * 60) + date.second + offset
                beat = (seconds / (24 * 60 * 60)) * 1000

                return str(math.floor(beat + 1000 if beat < 0 else beat))
            elif value == "g":
                return str(int(date.strftime("%I"), 10))
            elif value == "G":
                return str(date.hour)
            elif value == "h":
                return date.strftime("%I")
            elif value == "H":
                return date.strftime("%H")
            elif value == "i":
                return date.strftime("%M")
            elif value == "s":
                return date.strftime("%S")
            elif value == "u":
                return date.strftime("%f")
            elif value == "O":
                return self.format("P", date).replace(":", "")
            elif value == "P":
                utc = datetime.datetime.utcfromtimestamp(date.timestamp())
                offset = date.timestamp() - utc.timestamp()
                hours = int(offset / 60 / 60)
                minutes = int((offset - (hours * 60 * 60)) / 60)
                if hours or minutes:
                    sign = "-" if hours < 0 else "+"
                    return "{0}{1}:{2}".format(sign, str(abs(hours)).zfill(2), str(minutes).zfill(2))
                return "+00:00"
            elif value == "T":
                return date.strftime("%Z")
            elif value == "Z":
                utc = datetime.datetime.utcfromtimestamp(date.timestamp())
                offset = (utc - date).total_seconds()

                return str(int(offset / 60))
            elif value == "c":
                offset = int(date.strftime("%z") or 0)
                if offset:
                    return date.isoformat(timespec="milliseconds")
                return "{0}Z".format( date.isoformat(timespec="milliseconds").replace("+00:00", ""))
            elif value == "r":
                return self.format("D, d M Y H:i:s O", date)
            elif value == "U":
                return str(int(date.timestamp()))
            else:
                return value
        date = date or self.get_date()

        return "".join([convert(v) for v in format])



# Local variables:
# tab-width: 4
# c-basic-offset: 4
# c-hanging-comment-ender-p: nil
# End:
