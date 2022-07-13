import requests

from configuration import MAIN_URL
from src.enums.global_enums import GlobalErrorMessages


def test_main_http():
    response = requests.get(url='http://www.symphony-solutions.eu/')
    assert response.status_code == 200
    assert response.url.__str__() == 'https://www.symphony-solutions.eu/'
    print(response.url.__str__())


def test_main_without_www():
    response = requests.get(url='http://symphony-solutions.eu/')
    assert response.status_code == 200
    assert response.url.__str__() == 'https://www.symphony-solutions.eu/'
    print(response.url.__str__())


def test_main_uncorrect_text_after_slash():
    response = requests.get(url='https://www.symphony-solutions.eu/uncorrect')
    assert response.status_code == 404
    assert response.url.__str__() == 'https://www.symphony-solutions.eu/uncorrect'
    print(response.url.__str__())
