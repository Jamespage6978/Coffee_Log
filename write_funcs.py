from config import configuration as config
from read_funcs import log_ToDict
#
import os, json, pandas



def write_html():
    Log_df = log_ToDict()
    pandas.set_option('colheader_justify', 'center')
    if config['Switches']['location'] == 'local':
        path = "Coffee_Log.html"#f"{config['Local']['location']}Coffe_Log.html"
        html_string = '''<html>
  <head><title>HTML Pandas Dataframe with CSS</title></head>
  <link rel="stylesheet" type="text/css" href="static\df_style.css"/>
  <body>
    {table}
  </body>
</html>.
'''
        with open(path,'w') as outfile:
            outfile.write(html_string.format(table=Log_df.to_html(classes='mystyle')))
            #outfile.write(Log_df.to_html())

if __name__ == "__main__":
    write_html()