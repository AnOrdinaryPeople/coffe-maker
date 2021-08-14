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
errors = lang['errors']


def throw(message: str):
    """
    Simplify raise exception.

    :type message: str
    :param message: Message for error output.

    :raises Exception: exception error message.
    """
    raise Exception(message)


def choose_coffee():
    """
    Choose available coffee at MENU.

    :raises Exception: error message for validation.

    :rtype: str
    :return: input from user.
    """
    try:
        user_input = input(lang['choose_coffee'](menu_keys)).lower()

        if user_input.isnumeric():
            throw(errors['must_char'])
        elif user_input == '':
            throw(errors['empty_input'])
        elif re.search('[@_!#$%^&*()<>?/\|}{~:]', user_input):
            throw(errors['symbols'])
        elif not (user_input in menu_keys):
            throw(errors['not_found'](user_input))
    except Exception as error:
        raise error

    return user_input


def input_money():
    """
    Input user coin with menu_coin.

    :raises Exception: error message for validation.

    :rtype: int
    :return: total coins.
    """
    print(lang['input_coins'])
    money = []

    for m in menu_coin:
        try:
            money.append(int(input(lang['input_coin_list'](m[0]))) * m[1])
        except:
            throw(errors['must_numeric'])

    return round(sum(money), 2)


def validate_money(total_money: int, cost: int):
    """
    Validation if the coins is enough.

    :type total_money: int
    :param total_money: Total coins user.

    :type cost: int
    :param cost: Coffee cost.

    :raises Exception: error message for validation.
    """
    if total_money >= cost:
        total_money -= cost
        print(lang['return'], total_money)
    else:
        throw(errors['not_enough'])


def coffee_maker(inputuser: str, ingredients: dict):
    """
    Create the coffee.

    :type inputuser: str
    :param inputuser: Selected coffee.

    :type ingredients: dict
    :param ingredients: Ingredients from selected coffee.

    :rtype: str
    :return: Result of the coffee.
    """
    counter = 0

    for i in ingredients.keys():
        ing = ingredients[i]

        if resources[i] >= ing:
            counter += 1
            resources[i] -= ing

    if(len(ingredients) == counter):
        return lang['enjoy'](inputuser)
    else:
        return errors['not_enough_ingredients']


print(lang['welcome'])

while boolean:
    try:
        user_input = choose_coffee()
        selected = MENU[user_input]

        validate_money(input_money(), selected['cost'])

        print(
            lang['result'],
            coffee_maker(user_input, selected['ingredients'])
        )

    except Exception as err:
        print(err)
    finally:
        want_exit = input(lang['should_loop']).lower()

        if want_exit == 't':
            boolean = False
