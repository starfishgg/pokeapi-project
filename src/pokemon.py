



class Pokedex():
    list_of_pokemon: list[Pokemon]

    def add_pokemon(self, new_pokemon: Pokemon) -> None:
        self.list_of_pokemon.append(new_pokemon)


class Pokemon():

    id: int
    name: str
    type: str
    hp: int
    abilities: list[str]


    def set_stats(self) -> None:
        pass