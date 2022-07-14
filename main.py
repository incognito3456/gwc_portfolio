from flask import *
import random

app = Flask(__name__)


app.debug = True
app.secret_key = 'jdkfsjdlf'


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('main3.html')



if __name__ == '__main__':
    app.run()
