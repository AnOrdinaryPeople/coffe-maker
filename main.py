from data import MENU, resources
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


def throw(message):
    raise Exception(message)


def choose_coffee():
    try:
        user_input = input(lang['choose_coffee'](menu_keys)).lower()

        if user_input.isnumeric():
            throw(lang['errors']['must_char'])
        elif user_input == '':
            throw(lang['errors']['empty_input'])
        elif re.search('[@_!#$%^&*()<>?/\|}{~:]', user_input):
            throw(lang['errors']['symbols'])
        elif not (user_input in menu_keys):
            throw(lang['errors']['not_found'](user_input))
    except Exception as error:
        raise error

    return user_input


def input_money():
    print(lang['input_coins'])
    money = []

    for m in menu_coin:
        try:
            money.append(int(input(lang['input_coin_list'](m[0]))) * m[1])
        except:
            throw(lang['errors']['must_numeric'])

    return round(sum(money), 2)


def validate_money(total_money, cost):
    if total_money >= cost:
        total_money -= cost
        print(lang['return'], total_money)
    else:
        throw(lang['errors']['not_enough'])


def coffee_maker(inputuser, object):
    ingredients = object['ingredients'].keys()
    counter = 0

    for i in ingredients:
        ing = object['ingredients'][i]

        if resources[i] >= ing:
            counter += 1
            resources[i] -= ing

    if(len(ingredients) == counter):
        return lang['enjoy'](inputuser)
    else:
        return lang['errors']['not_enough_ingredients']


print(lang['welcome'])

while boolean:
    try:
        user_input = choose_coffee()
        selected = MENU[user_input]

        validate_money(input_money(), selected['cost'])

        print(lang['result'], coffee_maker(user_input, selected))

    except Exception as err:
        print(err)
    finally:
        want_exit = input(lang['should_loop']).lower()

        if want_exit == 't':
            boolean = False
