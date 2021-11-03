from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import random
import string
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()

class urls2(db.Model):
    id_ = db.Column("id_", db.Integer, primary_key=True)
    long = db.Column("long", db.String())
    short = db.Column("short", db.String(10))

    def __init__(self, long, short):
        self.long = long
        self.short = short

def shorten_url():
    letters = string.ascii_lowercase + string.ascii_uppercase
    while True:
        rand_letters =  ''.join(random.SystemRandom().choice(
        string.ascii_letters + \
        string.digits) for _ in range(10))
        short_url = urls2.query.filter_by(short=rand_letters).first()
        if not short_url:
            return rand_letters


@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == "POST":
        url_received = request.form.get('url')
        found_url = urls2.query.filter_by(long=url_received).first()

        if found_url:
            finalUrl = "127.0.0.1:5000/"+found_url.short
            return render_template('index.html', shortUrl = finalUrl)
        else:
            short_url = shorten_url()
            print(short_url)
            new_url = urls2(url_received, short_url)
            db.session.add(new_url)
            db.session.commit()
            finalUrl = "127.0.0.1:5000/"+short_url
            return render_template('index.html', shortUrl = finalUrl)
    else:
        return render_template('index.html')

@app.route('/<short_url>')
def redirection(short_url):
    long_url = urls2.query.filter_by(short=short_url).first()
    if long_url:
        return redirect(long_url.long)
    else:
        return f'<h1>Url doesnt exist</h1>'



@app.route('/history')
def display_all():
    return render_template('history.html', vals=urls2.query.all())

if __name__ == '__main__':
    app.run(debug=True)