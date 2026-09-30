"""
main.py
"""

from src.pokeapi_client import PokeAPIClient

import json





def main() -> None:
    client = PokeAPIClient()

    pokemon: list = client.get_all_pokemon()

    print(json.dumps(pokemon, indent=4))



if __name__ == "__main__":
    main()
  