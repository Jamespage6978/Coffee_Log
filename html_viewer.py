from flask import *
from read_funcs import log_ToDict
import pandas

app = Flask(__name__)
@app.route("/")
def show_tables():
    Log_df = log_ToDict()
    rendered = render_template('view.html',tables=[Log_df.to_html(classes ='mystyle')])
    return rendered

app.run(debug=True)
