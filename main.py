"""
main.py
"""

from src.pokemon import Pokemon
from src.pokeapi_client import PokeAPIClient

import json


def print_pokemon_info(pokemon: list) -> None:
    print()
    print(str(pokemon["id"]) + " - ", end="")
    print(pokemon["name"] + " (", end="")
    for type in pokemon["types"]:
        print(type["type"]["name"], end="")
    print(")")
    print("Abilities:")
    for ability in pokemon["abilities"]:
        print(" - " + ability["ability"]["name"])
    print("Stats:")
    total_stats = 0
    for stat in pokemon["stats"]:
        if stat["stat"]["name"] not in ["special-defense", "special-attack"]:
            print(" - " + stat["stat"]["name"] + ": " + str(stat["base_stat"]))
            total_stats += stat["base_stat"]

    print(f"Total Stats: {total_stats}")


def main() -> None:
    client = PokeAPIClient()

    #pokemon: list = client.get_data("ability")
    #print(json.dumps(pokemon, indent=4))

    pokemon = client.get_pokemon(4)
    print_pokemon_info(pokemon)
    
    pokemon = client.get_pokemon(name="pikachu")
    print_pokemon_info(pokemon)
    #print(json.dumps(pokemon, indent=4))



if __name__ == "__main__":
    main()
  