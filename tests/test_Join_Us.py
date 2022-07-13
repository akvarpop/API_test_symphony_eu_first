import requests


def test_vacancies():
    response = requests.get(url='https://www.symphony-solutions.eu/vacancies/')
    assert response.status_code == 200

def test_vacancies_ukraine():
    response = requests.get(url='https://www.symphony-solutions.eu/vacancies-ukraine/')
    assert response.status_code == 200

def test_vacancies_poland():
    response = requests.get(url='https://www.symphony-solutions.eu/vacancies-poland/')
    assert response.status_code == 200

def test_vacancies_macedonia():
    response = requests.get(url='https://www.symphony-solutions.eu/vacancies-macedonia/')
    assert response.status_code == 200

def test_vacancies_anywhere():
    response = requests.get(url='https://www.symphony-solutions.eu/vacancies-anywhere/')
    assert response.status_code == 200

def test_nigeria_remote_vacancies():
    response = requests.get(url='https://www.symphony-solutions.eu/nigeria-remote-vacancies/')
    assert response.status_code == 200

def test_1():
    requests.get(url='https://www.symphony-solutions.eu/nigeria-remote-vacancies/tr').status_code
