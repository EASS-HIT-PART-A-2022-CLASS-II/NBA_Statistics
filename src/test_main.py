from .main import *


def test_get_player():
    response = get_player("Ron")
    assert response.error=="no error"
    assert response.first_name=="Ron"



def test_get_player_false():
    response = get_player("Ron")
    assert response.error=="no error"
    assert response.first_name=="Sahar"


def test_get_team():
    response = get_team("Lakers")
    assert response.error=="no error"
    assert response.name=="Lakers"

def test_get_city():
    response = get_team_city("LA")
    assert response.city=="LA"

def test_get_teams():
    response = get_all_teams
    assert response==response
