import requests

def test_blog_Events_invites_you_to_the_Java():
    response = requests.get(url='https://www.symphony-solutions.eu/java-meetup/')
    assert response.status_code == 200

def test_blog_Events_Join_our_event():
    response = requests.get(url='https://www.symphony-solutions.eu/open-day-at-symphony-solutions/')
    assert response.status_code == 200

def test_blog_Events_python_security():
    response = requests.get(url='https://www.symphony-solutions.eu/python-security-best-practices-webinar/')
    assert response.status_code == 200

def test_blog_Events_ISTQB():
    response = requests.get(url='https://www.symphony-solutions.eu/istqb-foundation-exam-preparation-course/')
    assert response.status_code == 200

def test_blog_Events_invites_you():
    response = requests.get(url='https://www.symphony-solutions.eu/react-in-the-front-end-world-practical-cases/')
    assert response.status_code == 200

def test_blog_Events_motivated_remote_team():
    response = requests.get(url='https://www.symphony-solutions.eu/motivated-remote-team-webinar/')
    assert response.status_code == 200

def test_blog_Events_project_change_management():
    response = requests.get(url='https://www.symphony-solutions.eu/project-change-management-webinar/')
    assert response.status_code == 200

def test_blog_Events_design_thinking_online():
    response = requests.get(url='https://www.symphony-solutions.eu/design-thinking-online-workshop/')
    assert response.status_code == 200

