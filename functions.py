import csv
import pandas as pd

data = pd.read_csv("pokemon.csv")


items_per_page = 10


def show_pokemon_page(page_number):
    start_index = (page_number - 1) * items_per_page
    end_index = start_index + items_per_page
    page_data = data[start_index:end_index]

    if not page_data.empty:
        print(page_data)
    else:
        print("No Pokémon on this page.")


def show_all_pokemon():
    total_pages = len(data) // items_per_page + 1

    while True:
        try:
            page_number = int(
                input(f"Enter the page number (1 - {total_pages}) or '0' to exit: ")
            )
            if page_number == 0:
                break
            if 1 <= page_number <= total_pages:
                show_pokemon_page(page_number)
            else:
                print("Invalid page number. Please enter a valid page number.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def search_pokemon_by_name(name):
    # Search for the Pokémon by name
    pokemon = data[data["Name"].str.lower() == name.lower()]

    if not pokemon.empty:
        print("\n")
        print(pokemon)
        print("\n")
    else:
        print("Pokemon not found in the Pokédex.")


def show_pokemons_by_gen(gen):
    try:
        gen = int(gen)
        # Show all Pokemons by generation
        pokemon = data[data["Generation"] == gen]

        if not pokemon.empty:
            print("\n")
            for index, row in pokemon.iterrows():
                print("Name:", row["Name"])
                print("Generation:", row["Generation"])
                # maybe i can add more attributes to display
                print("\n")
        else:
            print("No Pokémon found in Generation " + str(gen))
    except ValueError:
        print("Invalid generation selection. Please enter a number between 1 and 6.")


def show_pokemons_by_type(type):
    try:
        pokemon = data[data["Type 1"].str.lower() == type.lower()]
        if not pokemon.empty:
            print("\n")
            for index, row in pokemon.iterrows():
                print("Name:", row["Name"])
                print("Type 1:", row["Type 1"])
                # may add more attributes to display here too like Type 2
                print("\n")
        else:
            print("No Pokémon Type found " + type)
    except ValueError:
        print(
            "Invalid type selection. Please enter a correct type('fire','bug','poison',etc.): ."
        )
