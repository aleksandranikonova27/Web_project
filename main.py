from os import path, remove
from flask import Flask, render_template, redirect, request, abort
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from datetime import datetime
from PIL import Image
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = '7bafb7a4fc07dnn5848ii753118eco64eda'

@app.route('/')
@app.route('/index')
def index():
    year = datetime.now().year
    return render_template('index.html', title='Ярослав Никонов', year=year)

def main():
    db_session.global_init("db/visitka.db")
    app.run()
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
