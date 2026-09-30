# PokeAPI Project

A small Python project for practising REST API development, Python, JSON handling, and API pagination using the [PokeAPI](https://pokeapi.co/).

The project is intentionally being built incrementally as a way to become more confident working with APIs and Python.

## Current functionality

The `PokeAPIClient` currently:

- Connects to the PokeAPI.
- Retrieves the Pokémon list from `/pokemon`.
- Follows the API's `next` links to retrieve all pages.
- Combines the results into a single list.
- Raises an exception when an HTTP request fails.
- Returns the Pokémon data as a list of dictionaries.

Example result:

```json
[
    {
        "name": "bulbasaur",
        "url": "https://pokeapi.co/api/v2/pokemon/1/"
    },
    {
        "name": "ivysaur",
        "url": "https://pokeapi.co/api/v2/pokemon/2/"
    }
]
```

## Project structure

```text
pokeapi-project/
├── main.py
├── src/
│   └── pokeapi_client.py
├── .gitignore
└── README.md
```

## Requirements

- Python 3.12+
- `requests`

Install the dependency with:

```bash
pip install requests
```

## Running the project

From the project directory:

```bash
python main.py
```

## Planned development

This project will be expanded to practise additional API and Python concepts, including:

- Retrieving individual Pokémon.
- Working with query parameters.
- More robust error handling.
- Handling different HTTP responses.
- Working with more complex nested JSON responses.
- Building useful functionality on top of the API.
- Improving the structure and testability of the client.