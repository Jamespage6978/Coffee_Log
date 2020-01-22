from main import readConfig
import os
import configparser
import json
def read_log(config):
    if config['Switches']['location'] == 'local':
            path = f"{config['Local']['location']}Coffe_Log.json"
            if os.path.exists(path) == False:
                print("no file")
            else:
                with open(path,'r') as feedsjson:
                    feeds = json.load(feedsjson)
    return feeds

def brews_method_Comp(Log_Feed):
    return 1

config = readConfig()
Log_Feed = read_log(config)
compare_log = []
for i in range(len(Log_Feed)):
    CurrentLog = Log_Feed[i]
    if CurrentLog['B_method'] == "V60":
        compare_log.append(CurrentLog)
    else:
        print("not this one")
att_compare = ["R_taste","taste"]

for i in range(len(compare_log)):
    CurrentLog = compare_log[i]
    print(f"{CurrentLog[att_compare[0]]} + {CurrentLog[att_compare[1]]}")