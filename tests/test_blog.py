import requests

from configuration import BLOG_URL
from src.enums.global_enums import GlobalErrorMessages


def test_getting_posts():
    response = requests.get(url=BLOG_URL)

    assert response.status_code == 200, GlobalErrorMessages.WRONG_STATUS_CODE.value

    print(response.status_code)

def test_blog():
    response = requests.get(url='https://www.symphony-solutions.eu/blog/')
    assert response.status_code == 200

def test_blog_page_2():
    response = requests.get(url='https://www.symphony-solutions.eu/blog/page/2/')
    assert response.status_code == 200

def test_blog_page_3():
    response = requests.get(url='https://www.symphony-solutions.eu/blog/page/3/')
    assert response.status_code == 200

def test_blog_page_4():
    response = requests.get(url='https://www.symphony-solutions.eu/blog/page/4/')
    assert response.status_code == 200


def test_blog_page_5():
    response = requests.get(url='https://www.symphony-solutions.eu/blog/page/5/')
    assert response.status_code == 200


def test_blog_page_6():
    response = requests.get(url='https://www.symphony-solutions.eu/blog/page/6/')
    assert response.status_code == 200


def test_blog_page_7():
    response = requests.get(url='https://www.symphony-solutions.eu/blog/page/7/')
    assert response.status_code == 200


def test_blog_page_8():
    response = requests.get(url='https://www.symphony-solutions.eu/blog/page/8/')
    assert response.status_code == 200


def test_blog_page_9():
    response = requests.get(url='https://www.symphony-solutions.eu/blog/page/9/')
    assert response.status_code == 200


def test_blog_page_10():
    response = requests.get(url='https://www.symphony-solutions.eu/blog/page/10/')
    assert response.status_code == 200


def test_blog_page_11():
    response = requests.get(url='https://www.symphony-solutions.eu/blog/page/11/')
    assert response.status_code == 200


def test_blog_page_12():
    response = requests.get(url='https://www.symphony-solutions.eu/blog/page/12/')
    assert response.status_code == 200


