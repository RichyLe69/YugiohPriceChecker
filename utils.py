import json
import requests
import os
import errno
from datetime import datetime


def get_card_prices(card_name, card_set, card_rarity):
    # Uses card name, need to check set and rarity
    # print(card_name, card_set, card_rarity)
    full_card_data = (requests.get("http://yugiohprices.com/api/get_card_prices/" + card_name))
    if full_card_data.status_code == 200:
        # print('Card Info Found')
        card_data = json.loads(full_card_data.text)
        count = 0
        card_match = False
        for version in card_data['data']:
            if card_set == (version['print_tag']):
                # print('Card Set Match')
                if card_rarity == (version['rarity']):
                    # print('Card Match')
                    card_match = True
                    break
            count += 1
        if card_match is False:
            count = 0
            print('~~~~~~~~~Error Card not matched for ' + card_name)
        return card_data['data'][count]
    elif full_card_data.status_code == 404:
        print('Card not Found')
        return 0


def get_card_prices_id(card_id):
    # Uses card id, not ideal for multi-rarity cards
    card_data = (requests.get("http://yugiohprices.com/api/price_for_print_tag/" + card_id))
    if card_data.status_code == 200:
        # print('Card Info Found')
        return card_data
    elif card_data.status_code == 404:
        print('Card not Found')
        return 0


def language_converter(lang):
    language_dict = {
        # 'ENG': ['en_name', 'en_sets'],
        'DEU': ['de_name', 'de_sets'],
        'FRE': ['fr_name', 'fr_sets'],
        'SPA': ['es_name', 'sp_sets'],
        'KOR': ['ko_name', 'kr_sets'],
        'JPN': ['ja_name', 'jp_sets'],
        'CHI': ['zh_name', 'zh_sets'],
        'PTG': ['pt_name', 'pt_sets'],
        'ITA': ['it_name', 'it_sets']

    }
    return language_dict.get(lang)


def rarity_converter(rarity):
    rarity_dict = {
        'Rare': 'Rare',
        'Super Rare': 'Super',
        'Starfoil Rare': 'Star',
        'Ultra Rare': 'Ultra',
        'Ultra Parallel Rare': 'HL',
        'Secret Rare': 'Secret',
        'Prismatic Secret Rare': 'Pris Secret',
        'Ultimate Rare': 'Ultimate',
        'Duel Terminal Ultra Parallel Rare': 'Duel Terminal',
        'Ghost Rare': 'Ghost'
    }
    return rarity_dict.get(rarity)


def output_table(deck, analytics):
    current_date = str(datetime.date(datetime.now()))
    decklist_table_directory = 'decklist_table/' + current_date + '/'
    file_name = '_table_' + current_date + '.txt'
    final_file_name = decklist_table_directory + deck + file_name

    if not os.path.exists(os.path.dirname(final_file_name)):  # create directory if not exist
        try:
            os.makedirs(os.path.dirname(final_file_name))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    text_file = open(final_file_name, 'w', errors="ignore")
    text_file.write(str(analytics.create_table()) + '\n')
    text_file.write('Date Updated: ' + current_date + '\n')
    text_file.write(str(analytics.get_total_price()) + '\n')
    text_file.write(str(analytics.get_rarity_count()) + '\n')
    text_file.write(str(analytics.get_language_count()) + '\n')
    text_file.write(str(analytics.create_foreign_table()) + '\n')  # only needed if foreign names are wanted,
    # significantly reduce processing time
    text_file.close()
    print(deck + ' output table created')


def get_card_metadata(card):
    url = 'https://yugipedia.com/api.php?action=query&prop=revisions&rvprop=content&format=json&titles='
    full_card_data = (requests.get(url + card))
    if full_card_data.status_code == 200:
        # print('Card Found')
        card_data = json.loads(full_card_data.text)
        # print(card_data['query']['pages'])
        for x in card_data['query']['pages']:
            card_metadata = (card_data['query']['pages'][x]['revisions'][0]['*'])
    elif full_card_data.status_code == 404:
        print('Card not Found')
    return card_metadata


def get_foreign_data(card, lang, set_tag):
    metadata = get_card_metadata(card)
    # this gets the name of the foreign card
    var = language_converter(lang)
    fr_name = (list(var)[0])
    fr_set = (list(var)[1])
    foreign_name = ((metadata.split(fr_name, 1)[1]).split('\n', 1)[0].replace('=', ' ').lstrip())
    # get name of set tag with corresponding language
    print_tag_no_lang = (set_tag.split('-', 1)[0])
    number = (((metadata.split(fr_set, 1)[1]).split('|', 1)[0].replace('=', ' ').lstrip()).split(print_tag_no_lang, 1)[1].split(';', 1)[0])
    foreign_set = (print_tag_no_lang + number)
    return foreign_name, foreign_set
