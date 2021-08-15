en = {
    'welcome': 'Welcome to Coffee Machine 101\nplease choose the menu that has been provided',
    'choose_coffee': lambda list_coffee: f"Menu options ({'/'.join(list_coffee)}) : ",
    'input_coins': '\nInsert Coins',
    'input_coin_list': lambda menu_coin: f"Insert {menu_coin}: ",
    'return': '\nYour return: ',
    'result': 'result: ',
    'should_loop': 'Choose menu again? (y/n) ',
    'enjoy': lambda input_user: f"This is {input_user} coffee, enjoy",
    'errors': {
        'must_char': 'Input must be letters',
        'must_numeric': 'Input must be numeric',
        'empty_input': 'The input is empty :(',
        'symbols': 'Symbols is not allowed',
        'not_found': lambda user_input: f"{user_input} not available",
        'not_enough': 'Sorry you don\'t have enough money, your money will be returned',
        'not_enough_ingredients': 'Sorry the material is not enough',
    },
}
