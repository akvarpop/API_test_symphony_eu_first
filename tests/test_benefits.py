import requests


def test_benefits_in_ukraine():
    response = requests.get(url='https://www.symphony-solutions.eu/benefits-in-ukraine/')
    assert response.status_code == 200

def test_benefits_anywhere():
    response = requests.get(url='https://www.symphony-solutions.eu/benefits-anywhere/')
    assert response.status_code == 200

def test_benefits_in_poland():
    response = requests.get(url='https://www.symphony-solutions.eu/benefits-in-poland/')
    assert response.status_code == 200

def test_benefits_in_north_macedonia():
    response = requests.get(url='https://www.symphony-solutions.eu/benefits-in-north-macedonia/')
    assert response.status_code == 200
