import unittest
from StockDataVisualizer import user_prompt
import datetime

class TestStockDataVisualizerInputs(unittest.TestCase):
    
    def test_ticer_symbol(self):
    #test for valid and invalid ticker symbols
        valid_symbols = ["AAPL", "GOOG", "TSLA"]
        invalid_symbols = ["APPLE!", "123", "GOOGLE", "A" * 8]

        for symbol in valid_symbols:
            self.assertTrue(symbol.isupper() and symbol.isalpha() and 1 <= len(symbol) <= 7)

        for symbol in invalid_symbols:
            self.assertFalse(symbol.isupper() and symbol.isalpha() and 1 <= len(symbol) <= 7)

    def test_chart_type(self):
        #test for valid and invalid chart types
        valid_chart_types = ["1", "2"]
        invalid_chart_types = ["0", "3", "a", "12"]

        for chart_type in valid_chart_types:
            self.assertIn(chart_type, ["1", "2"])

        for chart_type in invalid_chart_types:
            self.assertNotIn(chart_type, ["1", "2"])

    def test_time_series(self):
        #test for valid and invalid time series
        valid_time_series = ["1", "2", "3", "4"]
        invalid_time_series = ["0", "5", "a", "12"]

        for time_series in valid_time_series:
            self.assertIn(time_series, ["1", "2", "3", "4"])

        for time_series in invalid_time_series:
            self.assertNotIn(time_series, ["1", "2", "3", "4"])

    def test_start_date(self):
        #test for valid and invalid start dates
        valid_start_dates = ["2020-01-01", "2021-12-31"]
        invalid_start_dates = ["01-01-2020", "2020/01/01", "2020-13-01", "abc"]

        for date in valid_start_dates:
            try:
                datetime.datetime.strptime(date, '%Y-%m-%d')
                valid = True
            except ValueError:
                valid = False
            self.assertTrue(valid)

        for date in invalid_start_dates:
            try:
                datetime.datetime.strptime(date, '%Y-%m-%d')
                valid = True
            except ValueError:
                valid = False
            self.assertFalse(valid)

    def test_end_date(self):
        #test for valid and invalid end dates
        start_date = "2021-01-01"
        valid_end_dates = ["2021-01-02", "2021-12-31"]
        invalid_end_dates = ["2020-12-31", "2021-13-01", "01-01-2021"]

        for date in valid_end_dates:
            try:
                end_date = datetime.datetime.strptime(date, '%Y-%m-%d')
                start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
                valid = end_date >= start
            except ValueError:
                valid = False
            self.assertTrue(valid)

        for date in invalid_end_dates:
            try:
                end_date = datetime.datetime.strptime(date, '%Y-%m-%d')
                start = datetime.datetime.strptime(start_date, '%Y-%m-%d')
                valid = end_date >= start
            except ValueError:
                valid = False
            self.assertFalse(valid)

if __name__ == '__main__':
    unittest.main()