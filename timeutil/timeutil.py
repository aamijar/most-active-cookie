"""
Module that provides functions to process timestamps
"""

def parse_date_utc(timestamp: str) -> str:
    return timestamp.split("T")[0]

def parse_time_utc(timestamp: str) -> str:
    return timestamp.split("T")[1]


