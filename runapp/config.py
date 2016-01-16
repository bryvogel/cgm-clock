import argparse

config_values = {
    'weather_station': 'KCMH',
    'audio_files': '../runapp/audio'
}

class Configuration(object):
    def __init__(self):
        parser = argparse.ArgumentParser()
        args, _ = parser.parse_known_args()

    def get(self, name):
        return config_values.get(name)

configuration = Configuration()
