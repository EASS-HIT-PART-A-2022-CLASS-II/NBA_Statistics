
from fastapi import FastAPI
import uvicorn
import http.client

app = FastAPI()


@app.get("/get_all_players")
def index():
    conn = http.client.HTTPSConnection("free-nba.p.rapidapi.com")

    headers = {
        'X-RapidAPI-Key': "d76df82fddmsh6ea913d0e9198c3p180300jsn731409f18d41",
        'X-RapidAPI-Host': "free-nba.p.rapidapi.com"
        }

    conn.request("GET", "/players?page=0&per_page=25", headers=headers)

    res = conn.getresponse()
    data = res.read()


    return {data.decode("utf-8")} 


@app.get("/get_one_player") 
def index1():
    conn = http.client.HTTPSConnection("free-nba.p.rapidapi.com")
    headers = {
    'X-RapidAPI-Key': "d76df82fddmsh6ea913d0e9198c3p180300jsn731409f18d41",
    'X-RapidAPI-Host': "free-nba.p.rapidapi.com"
    }
    conn.request("GET", "/players/1", headers=headers)

    res = conn.getresponse()
    data = res.read()

    return(data.decode("utf-8"))



if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
