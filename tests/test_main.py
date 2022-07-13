import requests


from configuration import MAIN_URL
from src.enums.global_enums import GlobalErrorMessages


def test_main():
    response = requests.get(url=MAIN_URL)

    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value

    print(response.status_code)

def test_standby_ukraine():
    response = requests.get(url='https://standby-ukraine.com/')
    assert response.status_code == 200

