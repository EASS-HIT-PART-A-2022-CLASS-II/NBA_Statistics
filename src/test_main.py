from .main import *

def test_data():
    response = index("Ron")
    assert response.error=="ok"
    assert response.first_name=="Ron"
