import pandas as pd 
import requests
import json

#r = requests.get('https://tennis-api-atp-wta-itf.p.rapidapi.com/tennis/v2/atp/h2h/matches/5992/677/')
#print((r.ok))

def request_url(url,headers):
    response = requests.get(url, headers=headers)
    print(response.status_code)
    data = response.json()
    return data

def save_to_excel(data,path_to_xlsx):
  try:
    data = pd.DataFrame(data)
    data.to_excel(path_to_xlsx,index=False,engine="openpyxl")
    print("Data saved!!")
  except Exception as e:
     print(f"Invalid URL {e}")

def save_to_parquet(data,path_to_parquet):
  try:
    data = pd.DataFrame(data)
    data.to_parquet(path_to_parquet,engine="pyarrow")
    print("Data saved!!")
  except Exception as e:
     print(f"Invalid URL {e}")


if __name__ == "__main__":
  url = "https://tennis-api-atp-wta-itf.p.rapidapi.com/tennis/v2/atp/ranking/doubles/"

  headers = {
    "x-rapidapi-key": "4266d5a238msh7d32f8bd011d4a3p1ac1ecjsn3ddd38379797",
    "x-rapidapi-host": "tennis-api-atp-wta-itf.p.rapidapi.com"
  }  
  data = request_url(url,headers)
  print(f'This is data {data}')
  if data:
     save_to_excel(data,"tennis.xlsx")
     save_to_parquet(data,"tennis.parquet")
  