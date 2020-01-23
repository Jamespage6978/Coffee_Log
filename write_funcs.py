from config import configuration
from read_funcs import log_ToDict
#
import os, json, pandas



def write_html():
    Log_df = log_ToDict()
    if config['Switches']['location'] == 'local':
        path = f"{config['Local']['location']}Coffe_Log.html"
        with open(path,'w') as outfile:
            outfile.write(Log_df.to_html())

if __name__ == "__main__":
   print(configuration.read("config.ini"))
   # write_html()