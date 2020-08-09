import yaml
from utils import get_card_prices

decklist_directory = 'decklist/'
decklist_price_directory = 'decklist_price/'


class Deck:

    def __init__(self, deck_name):
        self.deck_name = deck_name
        with open(decklist_directory + self.deck_name + ".yaml", 'r') as stream:
            try:
                yaml_data = yaml.safe_load(stream)
                card_list = list()
                for cards in yaml_data:
                    card_list.append(cards)
            except yaml.YAMLError as exc:
                print(exc)

        self.deck_data = yaml_data
        self.cards = card_list

    def get_deck_data(self):
        return self.deck_data

    def get_deck_list(self):
        return self.cards

    def get_card_info(self, name):
        return self.deck_data[name]

    def get_deck_price(self):
        with open(decklist_price_directory + self.deck_name + '_price.yaml', 'w') as stream:
            for cards in self.cards:
                print(cards)
                card_json_data = get_card_prices(cards, self.deck_data[cards]['Set'], self.deck_data[cards]['Rarity'])
                if card_json_data['price_data']['status'] == 'success':
                    del card_json_data['price_data']['data']['listings']  # removes any long ass listing data
                    set_name_tag = (card_json_data['print_tag'] + ', ' + card_json_data['name']).replace(':', '')
                    rarity = (card_json_data['rarity'])
                    price_high = (card_json_data['price_data']['data']['prices']['high'])
                    price_low = (card_json_data['price_data']['data']['prices']['low'])
                    price_average = (card_json_data['price_data']['data']['prices']['average'])
                    shift_90 = round((card_json_data['price_data']['data']['prices']['shift_90']) * 100, 2)
                    shift_180 = round((card_json_data['price_data']['data']['prices']['shift_180']) * 100, 2)
                    shift_365 = round((card_json_data['price_data']['data']['prices']['shift_365']) * 100, 2)

                    card_dict_data = {cards: {'Set': set_name_tag,
                                              'Rarity': rarity,
                                              'Edition': self.deck_data[cards]['Edition'],
                                              'Price':
                                                  {'High': price_high,
                                                   'Low': price_low,
                                                   'Average': price_average,
                                                   'Shift 3 Months': shift_90,
                                                   'Shift 6 Months': shift_180,
                                                   'Shift 1 Year': shift_365},
                                              'Quantity': self.deck_data[cards]['Quantity'],
                                              'Language': self.deck_data[cards]['Language']}}

                    yaml.dump(card_dict_data, stream, sort_keys=False)
                else:
                    print('~~~~~~~~~~~~~cannot find this card data:' + cards)
