from os import path, remove
from flask import Flask, render_template, redirect, request, abort
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from datetime import datetime
from PIL import Image
from data import db_session
from forms import order_form

app = Flask(__name__)
app.config['SECRET_KEY'] = '7bafb7a4fc07dnn5848ii753118eco64eda'


@app.route('/')
@app.route('/index')
def index():
    year = datetime.now().year
    return render_template('index.html', title='Ярослав Никонов', year=year)


@app.route('/order')
def order():
    #form = order_form.OrderForm()
    return render_template('order.html', title='Регистрация',)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
    db_session.global_init("db/visitka.db")
