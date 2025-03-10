
from flask import Flask, render_template, request, redirect, url_for, jsonify, send_from_directory
import os
from translations import TRANSLATIONS

app = Flask(__name__)

def get_user_language():
    # Default language if not specified
    return request.args.get('lang', 'en')

@app.route('/')
def index():
    language = get_user_language()
    return render_template('index.html', 
                           content=TRANSLATIONS[language],
                           current_lang=language)

@app.route('/about')
def about():
    language = get_user_language()
    return render_template('about.html',
                         content=TRANSLATIONS[language],
                         current_lang=language)

@app.route('/products')
def products():
    language = get_user_language()
    return render_template('products.html',
                         content=TRANSLATIONS[language],
                         current_lang=language)

@app.route('/online-testing-chamber')
def online_testing_chamber():
    language = get_user_language()
    return render_template('online_testing_chamber.html',
                         content=TRANSLATIONS[language],
                         current_lang=language)

@app.route('/acoustic-instruments')
def acoustic_instruments():
    language = get_user_language()
    return render_template('acoustic_instruments.html',
                         content=TRANSLATIONS[language],
                         current_lang=language)

@app.route('/contact-location')
def contact_location():
    language = get_user_language()
    return render_template('contact_location.html',
                         content=TRANSLATIONS[language],
                         current_lang=language)

@app.route('/honored-customers')
def honored_customers():
    language = get_user_language()
    return render_template('honored_customers.html',
                         content=TRANSLATIONS[language],
                         current_lang=language)

@app.route('/faq')
def faq():
    language = get_user_language()
    return render_template('faq.html',
                         content=TRANSLATIONS[language],
                         current_lang=language)

@app.route('/client/<int:client_id>')
def client_page(client_id):
    language = get_user_language()
    return render_template('client_page.html',
                         client_id=client_id,
                         content=TRANSLATIONS[language],
                         current_lang=language)

@app.route('/clients/page/<int:page_num>')
def clients_grid(page_num):
    # Mock pagination logic
    items_per_page = 9
    # Would normally fetch from database
    total_clients = 20
    
    return jsonify({
        'current_page': page_num,
        'html': render_template('_clients_grid.html', 
                               page=page_num,
                               items_per_page=items_per_page)
    })
