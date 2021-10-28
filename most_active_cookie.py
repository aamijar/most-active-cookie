#!/usr/bin/env python

"""
Entry point to program
"""

from parser.parser import ArgParser, FileParser, LogParser
from cookie.cookie import LABEL_COOKIE, LABEL_TIMESTAMP, LABEL_CODE, LABEL_DATE, Cookie
from cookie.cookie_collection import CookieCollection
from timeutil.timeutil import parse_date_utc

if __name__ == "__main__":

    args = ArgParser().parse()
    
    fp = FileParser(filename=args.logfile)
    fdata = fp.parse(omit_headers=True)

    lp = LogParser(delimeter=LogParser.TYPE_CSV)

    log_lines = lp.binary_search_cookie(fdata, args.date)
    cc = CookieCollection()

    for line in log_lines:
        parsed_log = lp.parse(line, labels=[LABEL_CODE, LABEL_TIMESTAMP])
        cookie = Cookie(parsed_log[LABEL_CODE], parse_date_utc(parsed_log[LABEL_TIMESTAMP]))
        cc.add(cookie)
    most_active = cc.most_active()
    for active in most_active:
        print(active)
