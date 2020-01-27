import configparser
import os

def readConfig():
    config = configparser.ConfigParser()
    config.read("configs\config1.ini")
    return config

configuration = readConfig()
configuration['Local']['location'] = os.getcwd() + "\\data\\"
print(configuration['Local']['location'])
