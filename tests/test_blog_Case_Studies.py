import requests

def test_blog_case_studies_AI_and_iGaming_Come_Together():
    response = requests.get(url='https://www.symphony-solutions.eu/ai-and-igaming-come-together-case-study/')
    assert response.status_code == 200

def test_blog_case_studies_New_Face():
    response = requests.get(url='https://www.symphony-solutions.eu/a-new-face-always-gets-noticed-case-study/')
    assert response.status_code == 200

def test_blog_case_studies_New_Sportsbook():
    response = requests.get(url='https://www.symphony-solutions.eu/new-sportsbook-platform-increases-user-preference-case-study/')
    assert response.status_code == 200

def test_blog_case_studies_North_Macedonia():
    response = requests.get(url='https://www.symphony-solutions.eu/north-macedonia-only-5-of-leadership-roles-held-by-women/')
    assert response.status_code == 200

def test_blog_case_studies_Agile_Transformation():
    response = requests.get(url='https://www.symphony-solutions.eu/blexr-agile-transformation-case-study/')
    assert response.status_code == 200

def test_blog_case_studies_Gambling_and_Sports():
    response = requests.get(url='https://www.symphony-solutions.eu/coral-case-study/')
    assert response.status_code == 200

def test_blog_case_studies_Hologram_Pyramid():
    response = requests.get(url='https://www.symphony-solutions.eu/hologram-pyramid-project-case-study/')
    assert response.status_code == 200