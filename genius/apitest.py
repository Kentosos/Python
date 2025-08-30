from http.client import responses

import requests

def test_1:
    response = requests.get('https://www.google.com')
    assert response.status_code == 200