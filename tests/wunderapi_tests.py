from nose.tools import *
from wunderapi.wunderapi import Wunderapi
import json


def setup():
    api_key = '12345678901234567'
    location = '94101'
    return Wunderapi(api_key, location, units='imperial')

def mock_result():
    with open('tests/resources/result.txt') as data_file:
            result = json.load(data_file)
    return result

def mock_forecast_result():
    with open('tests/resources/forecast.txt') as data_file:
            result = json.load(data_file)
    return result


def setup_metric():
    api_key = '12345678901234567'
    location = '94101'
    return Wunderapi(api_key, location, units='metric')

def test_get_temp_f():
    api = setup()
    ("66.3 %sF" %  u"\u00b0")  == api.get_temp(mock_result())

def test_get_temp_c():
    api = setup_metric()
    ("19.1 %sc" %  u"\u00b0")  == api.get_temp(mock_result())

def test_get_url_current():
    api = setup()
    api_key = '12345678901234567'
    location = '12345'
    api.get_url('conditions')  == \
        "http://api.wunderground.com/api/%s/conditions/q/%s.json" % \
        (api_key, location)

def test_get_conditions():
    api = setup()
    conditions ="\nCurrent weather for San Francisco, CA \n"
    conditions += "66.3 and Partly Cloudy \n"
    conditions += "Winds: From the NNW at 22.0 MPH Gusting to 28.0 MPH \n"
    conditions += "Relative Humidty: 65%\n"
    conditions == api.get_conditions(mock_result())


def test_get_is_dict():
    api = setup()
    dict is type(api.get('conditions'))

def test_format_date():
    api = setup()
    "June 26" == api.format_date(mock_forecast_result())
