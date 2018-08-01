# vim: set expandtab tabstop=4 shiftwidth=4 softtabstop=4:



import datetime
import unittest
from karmia.utility import KarmiaUtilityDate

class TestKarmiaUtilityDateSetOffset(unittest.TestCase):
    def test_set_offset(self):
        utility = KarmiaUtilityDate()
        offset = datetime.timedelta(hours=9)
        self.assertNotEqual(utility.get_offset(), offset)

        utility.set_offset(offset)
        self.assertEqual(utility.get_offset(), offset)

class TestKarmiaUtilityDateSetDate(unittest.TestCase):
    def test_set_date(self):
        utility = KarmiaUtilityDate()
        date = datetime.datetime(2016, 1, 1, 0, 0, 0)
        self.assertNotEqual(utility.get_date(), date)

        utility.set_date(date)
        self.assertEqual(utility.get_date(), date)

class TestKarmiaUtilityDateGetDate(unittest.TestCase):
    def test_get_date(self):
        utility = KarmiaUtilityDate()
        date = datetime.datetime(2016, 1, 1, 0, 0, 0)
        utility.set_date(date)
        utility.set_offset(datetime.timedelta(0))

        self.assertEqual(utility.get_date(), date)

class TestKarmiaUtilityDateGetTime(unittest.TestCase):
    def test_get_time(self):
        utility = KarmiaUtilityDate()
        date = datetime.datetime(2016, 1, 1, 0, 0, 0)
        utility.set_date(date)
        utility.set_offset(datetime.timedelta(0))

        self.assertEqual(utility.get_time(), date.timestamp())

class TestKarmiaUtilityDateGetYMD(unittest.TestCase):
    def test_get_ymd_yesterday(self):
        utility = KarmiaUtilityDate()
        now = datetime.datetime(2016, 1, 1, 2, 59, 59, 999999)
        offset = datetime.timedelta(hours=3)
        utility.set_date(now)
        utility.set_offset(offset)
        result = utility.get_ymd()

        self.assertDictEqual(result, {
            "year": 2015,
            "month": 12,
            "date": 31
        })

    def test_get_ymd_today(self):
        utility = KarmiaUtilityDate()
        now = datetime.datetime(2016, 1, 1, 3, 0, 0, 0)
        offset = datetime.timedelta(hours=3)
        utility.set_date(now)
        utility.set_offset(offset)
        result = utility.get_ymd()

        self.assertDictEqual(result, {
            "year": 2016,
            "month": 1,
            "date": 1
        })

class TestKarmiaUtilityDateFormat(unittest.TestCase):
    def test_format_date(self):
        utility = KarmiaUtilityDate()
        format = "dDjlNSwz"
        result = "03Sun3Sunday7rd0214"
        utility.set_date(datetime.datetime(2014, 8, 3, 9, 0, 0))
        utility.set_offset(datetime.timedelta(0))

        self.assertEqual(utility.format(format), result)

    def test_format_week(self):
        utility = KarmiaUtilityDate()
        result = "31"
        utility.set_date(datetime.datetime(2014, 8, 3, 9, 0, 0))
        utility.set_offset(datetime.timedelta(0))

        self.assertEqual(utility.format("W"), result)

    def test_format_month(self):
        utility = KarmiaUtilityDate()
        format = "FmMnt"
        result = "August08Aug831"
        utility.set_date(datetime.datetime(2014, 8, 3, 9, 0, 0))
        utility.set_offset(datetime.timedelta(0))

        self.assertEqual(utility.format(format), result)

    def test_format_year(self):
        utility = KarmiaUtilityDate()
        format = "LoYy"
        result = "02014201414"
        utility.set_date(datetime.datetime(2014, 8, 3, 9, 0, 0))
        utility.set_offset(datetime.timedelta(0))

        self.assertEqual(utility.format(format), result)

    def test_format_time(self):
        utility = KarmiaUtilityDate()
        format = "aABgGhHisu"
        result = "pmPM54192109210000000000"
        utility.set_date(datetime.datetime(2014, 8, 3, 21, 0, 0))
        utility.set_offset(datetime.timedelta(0))

        self.assertEqual(utility.format(format), result)

    def test_format_timezone(self):
        utility = KarmiaUtilityDate()
        format = "OPZ"
        result = "+0900+09:00-540"
        utility.set_date(datetime.datetime(2014, 8, 3, 9, 0, 0))
        utility.set_offset(datetime.timedelta(0))

        self.assertEqual(utility.format(format), result)

    def test_format_full_date(self):
        utility = KarmiaUtilityDate()
        format = "crU"
        result = "2014-08-03T09:00:00.000ZSun, 03 Aug 2014 09:00:00 +09001407024000"
        utility.set_date(datetime.datetime(2014, 8, 3, 9, 0, 0))
        utility.set_offset(datetime.timedelta(0))

        self.assertEqual(utility.format(format), result)

    def test_test(self):
        utility = KarmiaUtilityDate()
        utility.set_date(datetime.datetime(2014, 8, 3, 9, 0, 0))
        utility.set_offset(datetime.timedelta(0))

        print(utility.format("T"))



# Local variables:
# tab-width: 4
# c-basic-offset: 4
# c-hanging-comment-ender-p: nil
# End:
