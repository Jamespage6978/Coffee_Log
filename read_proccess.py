from config import configuration as config
#
import os, json, pandas



def read_log():
    if config['Switches']['location'] == 'local':
            path = f"{config['Local']['location']}Coffe_Log.json"
            if os.path.exists(path) == False:
                print("no file")
            else:
                with open(path,'r') as feedsjson:
                    feeds = json.load(feedsjson)
    return feeds

def log_ToDict(log):
    df = pandas.DataFrame.from_records(log)
    return df

def write_html():
    Log_Feed = read_log()
    Log_df = log_ToDict(Log_Feed)
    if config['Switches']['location'] == 'local':
        path = f"{config['Local']['location']}Coffe_Log.html"
        with open(path,'w') as outfile:
            outfile.write(Log_df.to_html())

if __name__ == "__main__":
    write_html()