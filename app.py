import os
from flask import Flask, render_template, request, session, redirect, url_for
from translations import TRANSLATIONS

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev_key")

# Client data mapping
CLIENTS = {
    1: "AMETEK",
    2: "Cooler Master",
    3: "Pulse Secure",
    4: "Smiths Medical",
    5: "TRW",
    6: "Zealer",
    7: "Arvin Meritor",
    8: "北京航空航天大学",  # Beihang University
    9: "一汽奔腾",         # Bestune
    10: "BOSCH",
    11: "大金空调",        # DAIKIN
    12: "SONION",
    13: "DELPHI",
    14: "BOS"
}

def get_user_language():
    return session.get('language', 'en')

@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    items_per_page = 8
    total_clients = 70
    total_pages = (total_clients + items_per_page - 1) // items_per_page
    start_idx = (page - 1) * items_per_page + 1
    end_idx = min(start_idx + items_per_page - 1, total_clients)

    language = get_user_language()
    return render_template('index.html', 
                         content=TRANSLATIONS[language],
                         current_lang=language,
                         page=page,
                         total_pages=total_pages,
                         start_idx=start_idx,
                         end_idx=end_idx)

@app.route('/products')
def products():
    language = get_user_language()
    return render_template('products.html',
                         content=TRANSLATIONS[language],
                         current_lang=language)

@app.route('/panel-chamber')
def panel_chamber():
    language = get_user_language()
    return render_template('panel_chamber.html',
                         content=TRANSLATIONS[language],
                         current_lang=language)

@app.route('/wedge-chamber')
def wedge_chamber():
    language = get_user_language()
    return render_template('wedge_chamber.html',
                         content=TRANSLATIONS[language],
                         current_lang=language)

@app.route('/soundproof-boxes')
def soundproof_boxes():
    language = get_user_language()
    return render_template('soundproof_boxes.html',
                         content=TRANSLATIONS[language],
                         current_lang=language)

@app.route('/listening-room')
def listening_room():
    language = get_user_language()
    return render_template('listening_room.html',
                         content=TRANSLATIONS[language],
                         current_lang=language)

@app.route('/silent-rooms')
def silent_rooms():
    language = get_user_language()
    return render_template('silent_rooms.html',
                         content=TRANSLATIONS[language],
                         current_lang=language)

@app.route('/sound-isolation-cover')
def sound_isolation_cover():
    language = get_user_language()
    return render_template('sound-isolation-cover.html',
                         content=TRANSLATIONS[language],
                         current_lang=language)

@app.route('/reverb-room')
def reverb_room():
    language = get_user_language()
    return render_template('reverb_room.html',
                         content=TRANSLATIONS[language],
                         current_lang=language)

@app.route('/online-testing-chamber')
def online_testing_chamber():
    language = get_user_language()
    return render_template('online-testing-chamber.html',
                         content=TRANSLATIONS[language],
                         current_lang=language)

@app.route('/acoustic-instruments')
def acoustic_instruments():
    language = get_user_language()
    return render_template('acoustic_instruments.html',
                         content=TRANSLATIONS[language],
                         current_lang=language)

@app.route('/cases')
def cases():
    language = get_user_language()
    return render_template('cases.html',
                         content=TRANSLATIONS[language],
                         current_lang=language)

@app.route('/about')
def about():
    language = get_user_language()
    return render_template('about.html',
                         content=TRANSLATIONS[language],
                         current_lang=language)

@app.route('/set-language/<lang>')
def set_language(lang):
    if lang in TRANSLATIONS:
        session['language'] = lang
    return redirect(url_for('index'))

@app.route('/honored-customers')
def honored_customers():
    language = get_user_language()
    return render_template('honored_customers.html',
                         content=TRANSLATIONS[language],
                         current_lang=language)

@app.route('/honorary-qualification')
def honorary_qualification():
    language = get_user_language()
    return render_template('honorary_qualification.html',
                         content=TRANSLATIONS[language],
                         current_lang=language)

@app.route('/contact-location')
def contact_location():
    language = get_user_language()
    return render_template('contact_location.html',
                         content=TRANSLATIONS[language],
                         current_lang=language)

@app.route('/view-patent/<int:number>')
def view_patent(number):
    if 1 <= number <= 4:  # Validate patent number range
        language = get_user_language()
        return render_template('view_patent.html',
                            content=TRANSLATIONS[language],
                            current_lang=language,
                            number=number)
    return redirect(url_for('honorary_qualification'))

@app.route('/faq')
def faq():
    language = get_user_language()
    return render_template('faq.html',
                         content=TRANSLATIONS[language],
                         current_lang=language)

@app.route('/industry-dynamics')
def industry_dynamics():
    language = get_user_language()
    return render_template('industry_dynamics.html',
                         content=TRANSLATIONS[language],
                         current_lang=language)

@app.route('/client/<int:client_id>')
def client_page(client_id):
    client_name = CLIENTS.get(client_id, f"Client {client_id}")
    language = get_user_language()
    # For English version, use English names for specific clients
    if language == 'en':
        if client_id == 8:
            client_name = "Beihang University"
        elif client_id == 9:
            client_name = "Bestune"
        elif client_id == 11:
            client_name = "DAIKIN"
    return render_template('client_page.html',
                         content=TRANSLATIONS[language],
                         current_lang=language,
                         client_name=client_name,
                         client_id=client_id)