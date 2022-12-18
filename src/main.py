import requests
from .models import * 
from fastapi import FastAPI
import uvicorn
import http.client
import json

app = FastAPI()
@app.get("/get_all_players/{first_name}",response_model=all_data,response_model_exclude_unset=True)
def index(first_name):
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
            error="ok",
            team=[
                team(
                    id=i['team']['id'],
                    abbreviation="",
                    city=i['team']['city'],
                    conference="",
                    division="",
                    full_name="",
                    name="",
                    error="ok"
                )
            ]
        )
   return teams


@app.get("/get_one_player") 
def index1():
    url = "https://free-nba.p.rapidapi.com/players/1"

    headers = {
        "X-RapidAPI-Key": "d76df82fddmsh6ea913d0e9198c3p180300jsn731409f18d41",
        "X-RapidAPI-Host": "free-nba.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    response_dict=response.json()
    


    return (response_dict)




@app.get("/get_all_teams") 
def index2():
    url = "https://free-nba.p.rapidapi.com/teams"

    querystring = {"page":"0"}

    headers = {
        "X-RapidAPI-Key": "d76df82fddmsh6ea913d0e9198c3p180300jsn731409f18d41",
        "X-RapidAPI-Host": "free-nba.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    response_dict=response.json()


    return (response_dict)






@app.get("/get_teams_data/{name}",response_model=team,response_model_exclude_unset=True) 
def index3(name):
   url = "https://free-nba.p.rapidapi.com/teams"
   headers = {
        "X-RapidAPI-Key": "d76df82fddmsh6ea913d0e9198c3p180300jsn731409f18d41",
        "X-RapidAPI-Host": "free-nba.p.rapidapi.com"
    }
   response = requests.request("GET", url, headers=headers)
   response_dict=response.json()
   for i in response_dict['data']:
            if i['name']==name:
                team.id=i['id']
                team.city=i['city']
                team.error="ok"
                return team
   team.id=0000
   team.error="no data" 
   return team

@app.get("/get_teams_data_test/{name}") 
def indextst(name):
   url = "https://free-nba.p.rapidapi.com/teams"
   headers = {
        "X-RapidAPI-Key": "d76df82fddmsh6ea913d0e9198c3p180300jsn731409f18d41",
        "X-RapidAPI-Host": "free-nba.p.rapidapi.com"
    }
   response = requests.request("GET", url, headers=headers)
   response_dict=response.json()
   for i in response_dict['data']:
    if i['name']==name:
        return i
   return (response_dict)
          
@app.get("/get_teams_datas/{city}") 
def index4(city):
      url = "https://free-nba.p.rapidapi.com/teams"

      headers = {
            "X-RapidAPI-Key": "d76df82fddmsh6ea913d0e9198c3p180300jsn731409f18d41",
            "X-RapidAPI-Host": "free-nba.p.rapidapi.com"
        }

      response = requests.request("GET", url, headers=headers)

      response_dict=response.json()

      for i in response_dict['data']:
                if i['city']==city:
                    return i 
      return (response_dict)




@app.get("/test/{id}")
def index6(id:int):

    url = "https://free-nba.p.rapidapi.com/players"

    querystring = {"page":"0","per_page":"25"}

    headers = {
        "X-RapidAPI-Key": "d76df82fddmsh6ea913d0e9198c3p180300jsn731409f18d41",
        "X-RapidAPI-Host": "free-nba.p.rapidapi.com"
    }
    

    response = requests.request("GET", url, headers=headers, params=querystring)

    response_dict=response.json()

    for i in response_dict['data']:
        if i['id']==id:
            return i 
    return (response_dict)



if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
