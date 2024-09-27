import http.client
import pandas as pd 
import requests
import json

r = requests.get('https://rapidapi.com/Creativesdev/api/free-football-api-data/playground/apiendpoint_f2e4d9ed-136e-4218-bbe4-02a7439fc78f')
r.status_code
print((r.ok))


conn = http.client.HTTPSConnection("free-football-api-data.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "4266d5a238msh7d32f8bd011d4a3p1ac1ecjsn3ddd38379797",
    'x-rapidapi-host': "free-football-api-data.p.rapidapi.com"
}

conn.request("GET", "/football-league-team?teamid=2673", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

json_data = json.loads(data.decode("utf-8"))

df = pd.json_normalize(json_data)

#print(df)

df.to_csv('team_data.csv', index=False)
df.to_parquet('team_data.parquet', index=False)
team_data = pd.read_csv("team_data.csv")
#print("Data saved to team_data.csv and team_data.parquet")
