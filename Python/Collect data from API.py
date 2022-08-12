import requests

#or

from requests import get



## URL of The Metropolitan Museum of Art in New York City or The Met
urlmet = "https://collectionapi.metmuseum.org/public/collection/v1/objects/1"

response = get(urlmet)

response.status_code



json_resp = response.json()

json_resp["title"]

json_resp["objectName"]

json_resp["objectDate"]

json_resp["artistDisplayName"]



list(range(40))


from requests import get

base_url = "https://collectionapi.metmuseum.org/public/collection/v1/objects/"

for i in range(40):
    url = base_url + str(i+1)
    print(url)
    
    

from requests import get

base_url = "https://collectionapi.metmuseum.org/public/collection/v1/objects/"

for i in range(40):
    url = base_url + str(i+1)
    response = get(url)
    print(response.json()["title"])
    
    
    
## Create Dataframe

from requests import get


base_url = "https://collectionapi.metmuseum.org/public/collection/v1/objects/"

titles = []
objectnames = []
objectdates = []
artists = []
countries = []

for i in range(40):
    url = base_url + str(i+1)
    response = get(url)
    titles.append(response.json()['title'])
    objectnames.append(response.json()['objectName'])
    objectdates.append(response.json()['objectDate'])
    artists.append(response.json()['artistDisplayName'])
    countries.append(response.json()["country"])
   


import pandas as pd
dfmet = pd.DataFrame(
    {"Title": titles, "Object": objectnames, "Year": objectdates, "Artist": artists, "Country": countries}
)

dfmet
    
  
  
dfmet.info()
