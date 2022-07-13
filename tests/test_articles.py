import requests

def test_articles():
    response = requests.get(url='https://www.symphony-solutions.eu/category/articles/')
    assert response.status_code == 200

def test_articles_page_2():
    response = requests.get(url='https://www.symphony-solutions.eu/category/articles/page/2/')
    assert response.status_code == 200

def test_articles_page_3():
    response = requests.get(url='https://www.symphony-solutions.eu/category/articles/page/3/')
    assert response.status_code == 200

def test_articles_page_4():
    response = requests.get(url='https://www.symphony-solutions.eu/category/articles/page/4/')
    assert response.status_code == 200


def test_articles_page_5():
    response = requests.get(url='https://www.symphony-solutions.eu/category/articles/page/5/')
    assert response.status_code == 200