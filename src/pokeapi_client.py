"""
pokeapi-client.py
"""

BASE_URL: str = "https://pokeapi.co/api/v2/"


import requests




class PokeAPIClient():

    def __init__(self) -> None:
        self.base_url = BASE_URL


    def get_data(self, name: str = "pokemon") -> list:
        page_url =  self.base_url + name

        # useful name values:
        #   pokemon, ability, move, type, stat

        pokedata = []

        while page_url:
        
            response: requests.Response = requests.get(page_url)
            
            # will raise a  requests.HTTPError for unsuccessful HTTP statuc code
            response.raise_for_status()

            data = response.json()

            pokedata.extend(data["results"])

            page_url = data["next"]


        #print(pokedata)
        #print("Status Code: " + str(response.status_code))
        #print("Headers " + str(response.headers))
        #print("URL " + str(response.url))

        return pokedata


    def get_pokemon(self, id: int = None, name: str = None) -> list:

        if id is not None:
            page_url = self.base_url + f"pokemon/{id}"
        elif name is not None:
            page_url = self.base_url + f"pokemon/{name}"
        else:
            raise ValueError("Either id or name must be provided")

        response: requests.Response = requests.get(page_url)

        response.raise_for_status()

        data = response.json()

        name = self.get_name(data)

        return data


    def get_name(self, data: list) -> str:
        name: str = data["name"]

        return name

