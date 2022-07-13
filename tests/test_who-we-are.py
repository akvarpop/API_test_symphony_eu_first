import requests


def test_who_we_are():
    response = requests.get(url='https://www.symphony-solutions.eu/who-we-are/')
    assert response.status_code == 200

def test_who_we_are_culture():
    response = requests.get(url='https://www.symphony-solutions.eu/who-we-are/culture/')
    assert response.status_code == 200

def test_who_we_are_agile():
    response = requests.get(url='https://www.symphony-solutions.eu/who-we-are/agile/')
    assert response.status_code == 200

def test_who_we_are_symphony_care():
    response = requests.get(url='https://www.symphony-solutions.eu/who-we-are/symphony-care/')
    assert response.status_code == 200

def test_who_we_are_symphony_ur_awards_and_recognitions():
    response = requests.get(url='https://www.symphony-solutions.eu/who-we-are/our-awards-and-recognitions/')
    assert response.status_code == 200

def test_who_we_are_our_symphony_academy():
    response = requests.get(url='https://www.symphony-solutions.eu/who-we-are/symphony-academy/')
    assert response.status_code == 200

def test_who_we_are_symphony_anywhere():
    response = requests.get(url='https://www.symphony-solutions.eu/symphony-anywhere/')
    assert response.status_code == 200
