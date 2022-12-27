import requests
from .models import * 
from fastapi import FastAPI
import uvicorn


app = FastAPI()
@app.get("/get_player/{first_name}",response_model=all_data,response_model_exclude_unset=True)
def get_player(first_name):
   url = "https://free-nba.p.rapidapi.com/players"

   querystring = {"page":"0","per_page":"25"}

   headers = {
        "X-RapidAPI-Key": "d76df82fddmsh6ea913d0e9198c3p180300jsn731409f18d41",
        "X-RapidAPI-Host": "free-nba.p.rapidapi.com"
    }

   response = requests.request("GET", url, headers=headers, params=querystring)
   response_dict=response.json()
   for i in response_dict['data']:
    if i['first_name']==first_name:
        teams =all_data(
            id=i['id'],
            
            first_name=i['first_name'],
            last_name=i['last_name'],
            position=i['position'],
            error="no error",
            team=[
                team(
                    id=i['team']['id'],
                    abbreviation=i['team']['abbreviation'],
                    city=i['team']['city'],
                    conference=i['team']['conference'],
                    division=i['team']['division'],
                    full_name=i['team']['full_name'],
                    name=i['team']['name'],
                    error="no error"
                )
            ]
        )
   return teams






@app.get("/get_all_teams") 
def get_all_teams():
    url = "https://free-nba.p.rapidapi.com/teams"

    querystring = {"page":"0"}

    headers = {
        "X-RapidAPI-Key": "d76df82fddmsh6ea913d0e9198c3p180300jsn731409f18d41",
        "X-RapidAPI-Host": "free-nba.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    response_dict=response.json()


    return (response_dict)






@app.get("/get_team/{name}",response_model=team,response_model_exclude_unset=True) 
def get_team(name):
   url = "https://free-nba.p.rapidapi.com/teams"
   headers = {
        "X-RapidAPI-Key": "d76df82fddmsh6ea913d0e9198c3p180300jsn731409f18d41",
        "X-RapidAPI-Host": "free-nba.p.rapidapi.com"
    }
   response = requests.request("GET", url, headers=headers)
   response_dict=response.json()
   for i in response_dict['data']:
            if i['name']==name:
                team.name=i['name']
                team.id=i['id']
                team.city=i['city']
                team.conference=i['conference']
                team.full_name=i['full_name']
                team.error="no error"
                return team
   team.id=0000
   team.error="no data" 
   return team


          
@app.get("/get_team_by_city/{city}",response_model=team,response_model_exclude_unset=True) 
def get_team_city(city):
      url = "https://free-nba.p.rapidapi.com/teams"

      headers = {
            "X-RapidAPI-Key": "d76df82fddmsh6ea913d0e9198c3p180300jsn731409f18d41",
            "X-RapidAPI-Host": "free-nba.p.rapidapi.com"
        }

      response = requests.request("GET", url, headers=headers)

      response_dict=response.json()

      for i in response_dict['data']:
                if i['city']==city:
                    team.city=i['city']
                    team.id=i['id']
                    team.name=i['name']
                    team.conference=i['conference']
                    team.full_name=i['full_name']
                    team.error="no error"
                    return team 
      return (response_dict)








if __name__ == "__main__":
    uvicorn.run("main:app", port=2375, reload=True)
