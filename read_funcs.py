from config import configuration as config
import os, json, pandas

def read_log():
    """
    Reads the coffe log .json file and outputs feeds which is a python json of the log file
    """
    if config['Switches']['location'] == 'local':
            path = f"{config['Local']['location']}Coffe_Log.json"
            if os.path.exists(path) == False:
                print("no file")
            else:
                with open(path,'r') as feedsjson:
                    feeds = json.load(feedsjson)
    return feeds

def log_ToDict():
    """
    inputs: coffe log JSON
    outputs: Pandas dataframe from Json file
    """
    df = pandas.DataFrame.from_records(read_log())
    return df

