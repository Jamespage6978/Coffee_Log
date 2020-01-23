from main import readConfig
import os
import configparser
import json
import pandas
def read_log(config):
    if config['Switches']['location'] == 'local':
            path = f"{config['Local']['location']}Coffe_Log.json"
            if os.path.exists(path) == False:
                print("no file")
            else:
                with open(path,'r') as feedsjson:
                    feeds = json.load(feedsjson)
    return feeds

def log_Dict(log):
    df = pandas.DataFrame.from_records(log)
    return df

def write_html(config,Log_df):
     if config['Switches']['location'] == 'local':
        path = f"{config['Local']['location']}Coffe_Log.html"
        with open(path,'w') as outfile:
            outfile.write(Log_df.to_html())


config = readConfig()
Log_Feed = read_log(config)
Log_df = log_Dict(Log_Feed)

write_html(config,Log_df)