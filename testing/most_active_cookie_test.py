"""
Define test functions that will be used by Pytest
"""

from parsing.parser import LogParser
from cookie.cookie_collection import CookieCollection
import pytest


@pytest.fixture
def cookie_list():
    return ['3330laUfhglK3lC7,2018-12-09T14:19:00+00:00\n', 
    '555uXPGUrfbcn5UA,2021-12-09T10:13:00+00:00\n', 
    '5UAVanZf6UtGyKVS,2021-12-09T07:25:00+00:00\n', 
    '3330laUfhglK3lC7,2021-12-09T06:19:00+00:00\n', 
    '555uXPGUrfbcn5UA,2021-12-08T22:03:00+00:00\n', 
    '4sMM2LxV07bPJzwf,2021-12-08T21:30:00+00:00\n', 
    'fbcn5UAVanZf6UtG,2021-12-08T09:30:00+00:00\n', 
    '4sMM2LxV07bPJzwf,2020-12-07T23:30:00+00:00']


def test_binary_search(cookie_list):

    expected = ['3330laUfhglK3lC7,2018-12-09T14:19:00+00:00\n', 
    '555uXPGUrfbcn5UA,2021-12-09T10:13:00+00:00\n', 
    '5UAVanZf6UtGyKVS,2021-12-09T07:25:00+00:00\n', 
    '3330laUfhglK3lC7,2021-12-09T06:19:00+00:00\n']

    date = "2021-12-09"

    lp = LogParser(LogParser.TYPE_CSV)
    result = lp.binary_search_cookie(cookie_list, date)
    assert expected == result


@pytest.mark.parametrize("input, expected", [
    (155, ['1010laUfhglK3lC7', 'SAZuXPGUrfbcn5UA', '2021XPGUrfbcn5UA']), 
    (100, ['SAZuXPGUrfbcn5UA', '2021XPGUrfbcn5UA'])]
)
def test_get_most_active_cookie(input, expected):
    data = {'1010laUfhglK3lC7': input, 'SAZuXPGUrfbcn5UA': 155, '5UAVanZf6UtGyKVS': 123, '2021XPGUrfbcn5UA': 155}

    cc = CookieCollection()
    cc.data = data
    result = cc.most_active()

    assert expected == result
