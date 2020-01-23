import configparser

def readConfig():
    config = configparser.ConfigParser()
    config.read("config1.ini")
    return config

configuration = readConfig()
print(configuration.sections())