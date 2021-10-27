#!/usr/bin/python3

import argparse

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="find most active cookie")
    parser.add_argument("logfile", help="log file name", metavar="LOGFILE")
    parser.add_argument("-d", "--date", help="date in UTC time zone", required=True)
    args = parser.parse_args()

    cookies = {}

    with open(args.logfile) as f:
        
        for line in f:
            # remove '\n' character at end of line
            line = line.strip()

            # each line will have two columns in csv format [cookie, UTC timestamp]
            cookie = line.split(",")[0]
            timestamp = line.split(",")[1]
            date = timestamp.split("T")[0]

            if date == args.date:
                if cookie in cookies:
                    cookies[cookie] += 1
                else:
                    cookies[cookie] = 1
    
    # keep track of most active cookies by occurence
    most_active_cookies = [""]
    max_occurence = 0
    for key in cookies:
        if cookies[key] > max_occurence:
            most_active_cookies[0] = key
            max_occurence = cookies[key]
        elif cookies[key] == max_occurence:
            most_active_cookies.append(key)

    for c in most_active_cookies:
        print(c)
