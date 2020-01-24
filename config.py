import configparser

def readConfig():
    config = configparser.ConfigParser()
    config.read("configs\config1.ini")
    return config

configuration = readConfig()
