from configparser import ConfigParser
from lang import lang


class I18n:
    def __init__(self, init_lang: str = None):
        self.init_lang = init_lang
        self.init_bool = type(self.init_lang) is str
        self.config = self.create_config()['I18n']
        self.lang = lang
        self.available = lang.keys()
        self.selected = self.handle_selected()

    def create_config(self):
        config = ConfigParser()

        def hc(key: str, default: str):
            return self.handle_config(config, key, default)

        config.read('config.ini')

        config.set('I18n', 'language', hc('language', 'en'))

        return config

    def handle_config(self, config: ConfigParser, key: str, default: str):
        try:
            value = config.get('I18n', key)
        except:
            value = self.init_bool if self.init_lang else default

        return value

    def handle_selected(self):
        if(self.init_bool):
            try:
                obj = lang[self.init_lang]
            except:
                obj = {}

            return obj

        return lang[self.config['language']]
