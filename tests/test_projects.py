import requests


def test_projects():
    response = requests.get(url='https://www.symphony-solutions.eu/projects/')
    assert response.status_code == 200

def test_projects_pay_per_head_project():
    response = requests.get(url='https://www.symphony-solutions.eu/pay-per-head-project/')
    assert response.status_code == 200

def test_projects_hansecom_project():
    response = requests.get(url='https://www.symphony-solutions.eu/hansecom-project/')
    assert response.status_code == 200

def test_projects_indegene_project():
    response = requests.get(url='https://www.symphony-solutions.eu/indegene-project/')
    assert response.status_code == 200

def test_projects_casumo_project():
    response = requests.get(url='https://www.symphony-solutions.eu/casumo-project/')
    assert response.status_code == 200

def test_projects_hpe_project():
    response = requests.get(url='https://www.symphony-solutions.eu/hpe-project/')
    assert response.status_code == 200

def test_projects_avantage_project():
    response = requests.get(url='https://www.symphony-solutions.eu/avantage-project/')
    assert response.status_code == 200

def test_projects_vivino_project():
    response = requests.get(url='https://www.symphony-solutions.eu/vivino-project/')
    assert response.status_code == 200

def test_projects_omp_project():
    response = requests.get(url='https://www.symphony-solutions.eu/omp-project/')
    assert response.status_code == 200

def test_projects_react_career():
    response = requests.get(url='https://www.symphony-solutions.eu/react-career/')
    assert response.status_code == 200