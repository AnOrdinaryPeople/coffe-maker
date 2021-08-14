from data import MENU, resources
from operator import itemgetter
from lang.id import lang
import re

boolean = True
menu_keys = MENU.keys()
menu_coin = [
    ['Penny', .01],
    ['Nickels', .05],
    ['Dimes', .1],
    ['Quarters', .25],
]


def choose_coffee():
    try:
        user_input = input(lang['choose_coffee'](menu_keys)).lower()

        if user_input.isnumeric():
            raise Exception(lang['errors']['must_char'])
        elif user_input == '':
            raise Exception(lang['errors']['empty_input'])
        elif re.search('[@_!#$%^&*()<>?/\|}{~:]', user_input):
            raise Exception(lang['errors']['symbols'])
        elif not (user_input in menu_keys):
            raise Exception(lang['errors']['not_found'](user_input))
    except Exception as error:
        raise error

    return user_input


def input_money():
    # TODO 2: input insert coin (quarters-dimes-nickles-pennies)
    print(lang['input_coins'])
    money = []

    for m in menu_coin:
        try:
            money.append(int(input(lang['input_coin_list'](m[0]))) * m[1])
        except:
            raise Exception(lang['errors']['must_numeric'])

    return round(sum(money), 2)


def validate_money(total_money):
    # TODO 5: Cek duit cukup atau nggk
    if total_money >= selected['cost']:
        # TODO 3: Jika duit cukup kopi dibikin dan uang kembalian diberikan
        total_money -= selected['cost']
        print(lang['return'], total_money)
    else:
        raise Exception(lang['errors']['not_enough'])


def coffee_maker(inputuser, object):
    # TODO 4: Cek Bahan
    ingredients = object['ingredients'].keys()
    counter = 0

    for i in ingredients:
        ing = object['ingredients'][i]

        if resources[i] >= ing:
            counter += 1
            resources[i] -= ing

    if(len(ingredients) == counter):
        return lang['enjoy']
    else:
        return lang['errors']['not_enough_ingredients']


# TODO 1: input buat pilihan menu (espresso/latte/cappuccino)
print(lang['welcome'])

while boolean:
    try:
        user_input = choose_coffee()
        selected = MENU[user_input]
        total_money = input_money()

        validate_money(total_money)

        print(lang['result'], coffee_maker(user_input, selected))

    except Exception as err:
        print(err)
    finally:
        # TODO 6: While loop

        want_exit = input(lang['should_loop']).lower()

        if want_exit == 't':
            boolean = False
