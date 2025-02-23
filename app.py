import os
from flask import Flask, render_template, request, session, redirect, url_for
from translations import TRANSLATIONS

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev_key")

def get_user_language():
    return session.get('language', 'en')

@app.route('/')
def index():
    language = get_user_language()
    return render_template('index.html', 
                         content=TRANSLATIONS[language],
                         current_lang=language)

@app.route('/set-language/<lang>')
def set_language(lang):
    if lang in TRANSLATIONS:
        session['language'] = lang
    return redirect(url_for('index'))
