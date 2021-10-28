"""
This Module handles CLI arguments and Log file content
"""

import argparse
from timeutil.timeutil import parse_date_utc

class Parser:

    def __init__(self):
        pass
    def parse(self):
        raise NotImplementedError

class FileParser:
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
    
    def parse(self, omit_headers = False) -> list:
        lines = []
        with open(self.filename) as f:
            lines = f.readlines()
        if omit_headers:
            return lines[1:]
        return lines

class LogParser(Parser):

    TYPE_CSV = ","

    def __init__(self, delimeter: str, delnewline: bool = True):
        super().__init__()
        self.delimeter = delimeter
        self.delnewline = delnewline
    
    def parse(self, line: str, labels: list = None) -> list:
        # remove '\n' character at end of line
        if self.delnewline:
            line = line.strip()
        columns = line.split(self.delimeter)
        if labels is not None:
            return dict(zip(labels, columns))
        return columns

    def binary_search_cookie(self, data: list, target: str) -> list:
        # since we want the contigous range of targets within a sorted list we need to perform two binary searches
        # lower bound = first date that is just under target
        # upper bound = first date that is just above target
        lower = self._binary_search(data, target, upper=False)
        upper = self._binary_search(data, target, upper=True)
        return data[lower:upper]

        
    def _binary_search(self, data: list, target: str, upper: bool):
        # data is sorted in decsending order
        low = 0
        high = len(data)
        while (low < high):
            mid = (low + high) // 2
            timestamp = self.parse(data[mid])[1]
            date = parse_date_utc(timestamp)
            if date > target or (upper and date == target):
                low = mid + 1
            else:
                high = mid
        return low
        


class ArgParser(Parser):
    def __init__(self):
        super().__init__()
        parser = argparse.ArgumentParser(description="find most active cookie")
        parser.add_argument("logfile", help="log file name", metavar="LOGFILE")
        parser.add_argument("-d", "--date", help="date in UTC time zone", required=True)
        self.parser = parser

    def parse(self) -> argparse.Namespace:
        return self.parser.parse_args()
