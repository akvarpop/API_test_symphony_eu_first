import requests

def test_symphony_events():
    response = requests.get(url='https://www.symphony-solutions.eu/category/symphony-events/')
    assert response.status_code == 200