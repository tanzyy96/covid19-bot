import requests


def get_covid_stats(country):
    URL = "https://corona.lmao.ninja/countries/{}".format(country)
    return requests.get(url=URL).json()
