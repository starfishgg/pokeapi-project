"""
pokeapi-client.py
"""

BASE_URL: str = "https://pokeapi.co/api/v2"


import requests




class PokeAPIClient():

    def __init__(self) -> None:
        self.base_url = BASE_URL


    def get_all_pokemon(self) -> list:
        page_url =  self.base_url + "/pokemon"

        pokedata = []

        while page_url:
        
            response: requests.Response = requests.get(page_url)
            
            # will raise a  requests.HTTPError for unsuccessful HTTP statuc code
            response.raise_for_status()

            data = response.json()

            pokedata.extend(data["results"])

            page_url = data["next"]


        print(pokedata)
        #print("Status Code: " + str(response.status_code))
        #print("Headers " + str(response.headers))
        #print("URL " + str(response.url))

        return pokedata

        

        
