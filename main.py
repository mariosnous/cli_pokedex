from functions import *


if __name__ == "__main__":
    while True:
        print("\n")
        user_selection = input(
            "Please choose an option: Press '1' to show Pokémon by generation, '2' by name, '3' by type or '4' to show all Pokémon (or 'q' to exit): "
        )
        if user_selection.lower() == "q":
            break
        if user_selection == "1":
            gen_selection = input(
                "Select a number from 1-6 to show all Pokémon by generation :  "
            )

            show_pokemons_by_gen(gen_selection)

        if user_selection == "2":
            user_input_by_name = input(
                "Enter the name of the Pokémon (or 'q' to exit): "
            )
            print("\n")

            search_pokemon_by_name(user_input_by_name)

        if user_selection == "3":
            type_selection = input(
                "Enter a type to view all pokemon by their type, eg.('fire','flying',''poison',etc.):  "
            )
            print("\n")

            show_pokemons_by_type(type_selection)

        if user_selection == "4":
            print("*" * 140)
            show_all_pokemon()
