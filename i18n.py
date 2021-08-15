from configparser import ConfigParser
from lang import lang


class I18n:
    def __init__(self):
        self.config = self.create_config()['I18n']
        self.lang = lang
        self.available = lang.keys()
        self.selected = lang[self.config['language']]

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
            value = default

        return value
