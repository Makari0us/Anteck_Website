import os
from flask import Flask, render_template, request, session, redirect, url_for, jsonify

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
    8: "Beihang University",
    9: "Bestune",
    10: "BOSCH",
    11: "DAIKIN",
    12: "SONION",
    13: "DELPHI",
    14: "BOS",
    15: "INTEVA",
    16: "Valeo",
    17: "Philips",
    18: "Foxconn",
    19: "Fujitsu",
    20: "GHSP",
    21: "HIT",
    22: "Kumho Tire",
    23: "KAIT",
    24: "HuaBao",
    25: "SAIC",
    26: "Huaguan Group",
    27: "Huaqin",
    28: "JAC",
    29: "Jin Laike",
    30: "Joyoung",
    31: "Konka",
    32: "HEC",
    33: "Longcheer",
    34: "Logitech",
    35: "MA Steel",
    36: "BenQ",
    37: "Sharp",
    38: "NUAA",
    39: "Yinghuada",
    40: "Desano",
    41: "Omron",
    42: "Richmat",
    43: "Nidec",
    44: "Realsil",
    45: "Sanhua",
    46: "Mitsubishi Heavy Industries",
    47: "Sangfei Communication",
    48: "HYO SEONG ZHIDA",
    49: "Meiji",
    50: "Visteon",
    51: "Providence Enterprise",
    52: "SUMIDA",
    53: "Panasonic",
    54: "Mando",
    55: "TRICO",
    56: "TINNO",
    57: "TIANSHIDA",
    58: "SKYBEST",
    59: "VIA",
    60: "Webasto",
    61: "Crown",
    62: "Siemens",
    63: "Xiaomi",
    64: "ADDA",
    65: "SIASUN",
    66: "EC Research",
    67: "Yankuang Textile",
    68: "YISEN",
    69: "cebi international",
    70: "Infineon"
}

def get_user_language():
    return session.get('language', 'en')

@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    items_per_page = 10  # Changed from 8 to 10
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
    return render_template('acoustic-instruments.html',
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
    return render_template('client_page.html',
                         content=TRANSLATIONS[language],
                         current_lang=language,
                         client_name=client_name,
                         client_id=client_id)

@app.route('/get_clients/<int:page>')
def get_clients(page):
    items_per_page = 10  # Changed from 8 to 10
    total_clients = 70
    start_idx = (page - 1) * items_per_page + 1
    end_idx = min(start_idx + items_per_page - 1, total_clients)

    clients_html = render_template('_clients_grid.html',
                                start_idx=start_idx,
                                end_idx=end_idx,
                                content=TRANSLATIONS[get_user_language()],
                                current_lang=get_user_language())

    return jsonify({
        'html': clients_html,
        'total_pages': (total_clients + items_per_page - 1) // items_per_page,
        'current_page': page
    })