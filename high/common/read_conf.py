import configparser

class ReadConfig:
    def read_config(self, conf_file, section, location):
        config = configparser.ConfigParser()
        config.read(conf_file)
        value = config.get(section, location)
        return value