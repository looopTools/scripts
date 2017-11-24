import yaml
import io

class Config:

    site = None
    interval = None
    def __init__(self, site, interval):
        self.site = site
        self.interval = interval

    @staticmethod
    def _read_configuration_file(path):
        with open(path, 'r') as stream:
            try:
                return yaml.load(stream)
            except yaml.YAMLError as e:
                print(e)
                return None

    @staticmethod
    def build(path):
        config = Config._read_configuration_file(path)['config']
        return Config(config['site'] ,config['interval'])
        return None
