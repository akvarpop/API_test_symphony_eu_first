import requests


def test_contact_us():
    response = requests.get(url='https://www.symphony-solutions.eu/contact-us/')
    assert response.status_code == 200
