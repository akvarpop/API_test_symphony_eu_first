import requests

def test_news():
    response = requests.get(url='https://www.symphony-solutions.eu/category/news/')
    assert response.status_code == 200

def test_news_page_2():
    response = requests.get(url='https://www.symphony-solutions.eu/category/news/page/2/')
    assert response.status_code == 200

def test_news_page_3():
    response = requests.get(url='https://www.symphony-solutions.eu/category/news/page/3/')
    assert response.status_code == 200

def test_news_page_4():
    response = requests.get(url='https://www.symphony-solutions.eu/category/news/page/4/')
    assert response.status_code == 200


def test_news_page_5():
    response = requests.get(url='https://www.symphony-solutions.eu/category/news/page/5/')
    assert response.status_code == 200