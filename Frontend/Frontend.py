import streamlit as st
import requests
import json
import pandas as pd 
import pymongo
client=pymongo.MongoClient("mongodb+srv://ron_pinto:Aa123456@icons.uvffn44.mongodb.net/icons")
db=client["icons_database"]
collection=db["icons_collection"]

def get_player(first_name):
  response = requests.get(f"http://backend:8000/get_player/{first_name}")
  return response.json()

def get_team(name):
  response = requests.get(f"http://backend:8000/get_team/{name}")
  return response.json()

def get_team_by_city(city):
  response = requests.get(f"http://backend:8000/get_team_by_city/{city}")
  return response.json()

def get_all_teams():
  response = requests.get("http://backend:8000/get_all_teams")
  return response.json()

  


def main():
  st.sidebar.title("NBA Lookup")
  st.sidebar.markdown("Enter a player's first name or a team's name to look up:")
  search_term = st.sidebar.text_input("")

  if st.sidebar.button("Get player"):
    player = get_player(search_term)
    if player['error'] == "no error":
      st.write(f"Player: {player['first_name']} {player['last_name']}")
      st.write(f"Team: {player['team'][0]['name']}")

  if st.sidebar.button("Get team"):
    team = get_team(search_term)
    if team['error'] == "no error":
      st.write(f"Team: {team['name']}")
      st.write(f"City: {team['city']}")
      st.write(f"Conference: {team['conference']}")
      st.write(f"Full name: {team['full_name']}")
      result=collection.find({"image_name":team['name']})
      png=""
      for res in result:
        png=res["image_url"]
      st.image(png,width=200)

  if st.sidebar.button("Get team by city"):
    team = get_team_by_city(search_term)
    if team['error'] == "no error":
      st.write(f"Team: {team['name']}")
      st.write(f"City: {team['city']}")
      st.write(f"Conference: {team['conference']}")
      st.write(f"Full name: {team['full_name']}")
    else:
      st.write("No results found.")

  

  if st.sidebar.button ("get all teams"):
   teams=get_all_teams()
   json_data=json.dumps(teams['data'])
   data=json.loads(json_data)
   df=pd.DataFrame(data)
   st.dataframe(df)





image_path = 'https://cdn.nba.com/manage/2022/12/NBA_holidayfinalB_16x9-2-e1671646455710.png'
st.image(image_path,width=600)






if __name__ == '__main__':
  main()
