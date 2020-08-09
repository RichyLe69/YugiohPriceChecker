import yaml
import prettytable
from utils import rarity_converter, get_foreign_data

decklist_price_directory = 'decklist_price/'


class Analytics:

    def __init__(self, decklist):
        self.decklist = decklist + '_price.yaml'
        with open(decklist_price_directory + self.decklist, 'r') as stream:
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

    def get_card_list(self):
        return self.cards

    def get_decklist_name(self):
        return self.decklist

    def get_total_amount_cards(self):
        total_cards = 0
        for cards in self.deck_data:
            total_cards += self.deck_data[cards]['Quantity']
        return total_cards

    def get_total_price(self):
        total_high = 0
        total_low = 0
        total_average = 0
        for cards in self.deck_data:
            total_high += self.deck_data[cards]['Price']['High']
            total_low += self.deck_data[cards]['Price']['Low']
            total_average += self.deck_data[cards]['Price']['Average']

        price_table = prettytable.PrettyTable(['Average', 'High', 'Low'])
        price_table.add_row([round(total_average), round(total_high), round(total_low)])
        return price_table

    def get_rarity_count(self):
        rarity_counter = {'Common': 0, 'Rare': 0, 'Super Rare': 0, 'Ultra Rare': 0, 'Secret Rare': 0,
                          'Prismatic Secret Rare': 0, 'Ultimate Rare': 0, 'Ghost Rare': 0,
                          'Duel Terminal Ultra Parallel Rare': 0}
        for cards in self.deck_data:
            # print(self.deck_data[cards]['Rarity'])
            if self.deck_data[cards]['Rarity'] in rarity_counter:
                rarity_counter[self.deck_data[cards]['Rarity']] += self.deck_data[cards]['Quantity']

        rarity_counter = {k: v for k, v in rarity_counter.items() if v}
        rarity_table = prettytable.PrettyTable(rarity_counter)
        rarity_table.add_row(rarity_counter.values())
        return rarity_table

    def get_language_count(self):
        language_counter = {'ENG': 0, 'DEU': 0, 'JPN': 0, 'ITA': 0, 'SPA': 0, 'FRE': 0, 'PTG': 0}
        for cards in self.deck_data:
            # print(self.deck_data[cards]['Language'])
            if self.deck_data[cards]['Language'] in language_counter:
                language_counter[self.deck_data[cards]['Language']] += self.deck_data[cards]['Quantity']
                # print('found ' + self.deck_data[cards]['Language'])
        language_counter = {k: v for k, v in language_counter.items() if v}
        language_table = prettytable.PrettyTable(language_counter)
        language_table.add_row(language_counter.values())
        return language_table

    def create_table(self):
        deck_table = prettytable.PrettyTable(['Qty', 'Name', 'Rarity', 'Ed.', 'Set', 'Lang.',
                                              'Price (Avg)', 'Price (High)', 'Price (Low)',
                                              'Shift 3M', 'Shift 6M', 'Shift 1Y'])
        for cards in self.deck_data:
            deck_table.add_row([
                self.deck_data[cards]['Quantity'],
                cards,
                rarity_converter(self.deck_data[cards]['Rarity']),
                self.deck_data[cards]['Edition'][0:3],
                self.deck_data[cards]['Set'].split(',')[0],
                self.deck_data[cards]['Language'],
                self.deck_data[cards]['Price']['Average'],
                self.deck_data[cards]['Price']['High'],
                self.deck_data[cards]['Price']['Low'],
                self.deck_data[cards]['Price']['Shift 3 Months'],
                self.deck_data[cards]['Price']['Shift 6 Months'],
                self.deck_data[cards]['Price']['Shift 1 Year']])
        return deck_table

    def create_foreign_table(self):
        foreign_table = prettytable.PrettyTable(['Set', 'Name', 'Foreign Name', 'Foreign Set'])
        for cards in self.deck_data:
            if self.deck_data[cards]['Language'] != 'ENG':
                print(cards + ' - Foreign')
                foreign_data = get_foreign_data(cards, self.deck_data[cards]['Language'], self.deck_data[cards]['Set'].split(',')[0])
                foreign_table.add_row([self.deck_data[cards]['Set'].split(',')[0], cards, foreign_data[0], foreign_data[1]])
        return foreign_table

    # top 10 expensive cards
    def top_10_cards(self):
        return 0
