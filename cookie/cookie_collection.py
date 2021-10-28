"""
Module that defines a group of cookies and finds the most active cookie
"""

import cookie.cookie as c


class CookieCollection:
    def __init__(self):
        self.data = {}
    def add(self, cookie: c.Cookie) -> None:
        if cookie.code in self.data:
            self.data[cookie.code] += 1
        else:
            self.data[cookie.code] = 1
    def most_active(self) -> list:
        most_active_cookies = [""]
        max_occurence = 0
        
        for key in self.data:
            if self.data[key] > max_occurence:
                most_active_cookies[0] = key
                max_occurence = self.data[key]
            elif self.data[key] == max_occurence:
                most_active_cookies.append(key)
        return most_active_cookies
