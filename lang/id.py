id = {
    'welcome': 'Selamat Datang Di Coffee Machine 101\nsilahkan memilih menu yang telah disediakan',
    'choose_coffee': lambda list_coffee: f"Pilihan menu ({'/'.join(list_coffee)}) : ",
    'input_coins': '\nMasukkan Coin',
    'input_coin_list': lambda menu_coin: f"Masukkan {menu_coin}: ",
    'return': '\nKembalian: ',
    'result': 'hasilnya: ',
    'should_loop': 'Pilih menu lagi? (y/t) ',
    'enjoy': lambda input_user: f"Ini dia kopi {input_user}, Selamat dinikmati",
    'errors': {
        'must_char': 'Inputan harus huruf',
        'must_numeric': 'Inputan harus angka',
        'empty_input': 'Inputannya kosong :(',
        'symbols': 'Tidak boleh ada simbol',
        'not_found': lambda user_input: f"Pilihan {user_input} gk ad",
        'not_enough': 'Maaf uang anda tidak cukup, Uang anda dikembalikan kembali',
        'not_enough_ingredients': 'Maaf Bahan tidak cukup',
    },
}
