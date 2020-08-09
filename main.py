from deck import Deck
from analytics import Analytics
from utils import output_table


if __name__ == "__main__":

    my_collection = ['goat_decklist', 'yugi_decklist', 'jaden_decklist', 'zane_decklist',
                     'teledad_decklist', 'plants_decklist', 'lightsworn_decklist']
    # binder_decklist

    for my_deck in my_collection:
        # Creates deck JSON object, updates the price yaml with full pricing info
        deck = Deck(my_deck)
        deck.get_deck_price()

        # Reads price yaml and outputs a clean table with calculated info
        analytics = Analytics(my_deck)
        output_table(my_deck, analytics)

# TODO
# add binder
# parallel processing lol
# https://yugipedia.com/api.php?action=query&prop=revisions&rvprop=content&format=json&titles=Stardust_Dragon
