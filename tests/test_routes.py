from app import app


def test_home():
    response = app.test_client().get('/')
    assert response.text == 'Flask Website Running Successfully'
    assert response.status == '200 OK'
