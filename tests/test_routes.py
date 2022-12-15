from app import app


def test_homepage():
    response = app.test_client().get('/')
    assert response.text == 'Flask Website Running Successfully'
    assert response.status == '200 OK'


def test_printname():
    response = app.test_client().get('/adithya')
    assert response.text == "Hey adithya"
    assert response.status_code == 200
