import os
from flask import Flask, render_template, request, session, redirect, url_for, jsonify

from translations import TRANSLATIONS

app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev_key")

# Client data mapping with language-specific names
CLIENTS = {
    1: "AMETEK",
    2: "Cooler Master",
    3: "Pulse Secure",
    4: "Smiths Medical",
    5: "TRW",
    6: "Zealer",
    7: "Arvin Meritor",
    8: {"en": "Beihang University", "vi": "Beihang University", "zh": "北京航空航天大学"},
    9: {"en": "Bestune", "vi": "Bestune", "zh": "一汽奔腾"},
    10: "BOSCH",
    11: {"en": "DAIKIN", "vi": "DAIKIN", "zh": "大金空调"},
    12: "SONION",
    13: "DELPHI",
    14: "BOS",
    15: "INTEVA",
    16: "Valeo",
    17: "Philips",
    18: {"en": "Foxconn", "vi": "Foxconn", "zh": "富士康"},
    19: {"en": "Fujitsu", "vi": "Fujitsu", "zh": "富士通"},
    20: "GHSP",
    21: {"en": "HIT", "vi": "HIT", "zh": "哈工大"},
    22: {"en": "Kumho Tire", "vi": "Kumho Tire", "zh": "锦湖轮胎"},
    23: "KAIT",
    24: {"en": "HuaBao", "vi": "HuaBao", "zh": "华宝"},
    25: {"en": "SAIC", "vi": "SAIC", "zh": "上汽集团"},
    26: {"en": "Huaguan Group", "vi": "Huaguan Group", "zh": "华冠集团"},
    27: {"en": "Huaqin", "vi": "Huaqin", "zh": "华勤"},
    28: {"en": "JAC", "vi": "JAC", "zh": "江淮汽车"},
    29: {"en": "Jin Laike", "vi": "Jin Laike", "zh": "金莱克"},
    30: {"en": "Joyoung", "vi": "Joyoung", "zh": "九阳"},
    31: {"en": "Konka", "vi": "Konka", "zh": "康佳"},
    32: {"en": "HEC", "vi": "HEC", "zh": "鸿志"},
    33: {"en": "Longcheer", "vi": "Longcheer", "zh": "龙旗"},
    34: "Logitech",
    35: {"en": "MA Steel", "vi": "MA Steel", "zh": "马钢"},
    36: "BenQ",
    37: "Sharp",
    38: {"en": "NUAA", "vi": "NUAA", "zh": "南京航空航天大学"},
    39: {"en": "Yinghuada", "vi": "Yinghuada", "zh": "英华达"},
    40: {"en": "Desano", "vi": "Desano", "zh": "德赛"},
    41: "Omron",
    42: {"en": "Richmat", "vi": "Richmat", "zh": "豪江"},
    43: "Nidec",
    44: {"en": "Realsil", "vi": "Realsil", "zh": "瑞昱"},
    45: {"en": "Sanhua", "vi": "Sanhua", "zh": "三花"},
    46: "Mitsubishi Heavy Industries",
    47: {"en": "Sangfei Communication", "vi": "Sangfei Communication", "zh": "桑菲通讯"},
    48: "HYO SEONG ZHIDA",
    49: "Meiji",
    50: "Visteon",
    51: "Providence Enterprise",
    52: "SUMIDA",
    53: "Panasonic",
    54: "Mando",
    55: "TRICO",
    56: {"en": "TINNO", "vi": "TINNO", "zh": "天珑移动"},
    57: {"en": "TIANSHIDA", "vi": "TIANSHIDA", "zh": "天时达"},
    58: "SKYBEST",
    59: {"en": "VIA", "vi": "VIA", "zh": "威盛电子"},
    60: "Webasto",
    61: "Crown",
    62: "Siemens",
    63: {"en": "Xiaomi", "vi": "Xiaomi", "zh": "小米"},
    64: "ADDA",
    65: {"en": "SIASUN", "vi": "SIASUN", "zh": "新松"},
    66: {"en": "EC Research", "vi": "EC Research", "zh": "研科"},
    67: {"en": "Yankuang Textile", "vi": "Yankuang Textile", "zh": "扬子江纺业"},
    68: {"en": "YISEN", "vi": "YISEN", "zh": "易森"},
    69: "cebi international",
    70: "Infineon"
}

def get_client_name(client_id, language):
    """Get client name based on language"""
    client = CLIENTS.get(client_id)
    if isinstance(client, dict):
        return client.get(language, client['en'])
    return client

def get_user_language():
    return session.get('language', 'en')

@app.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    items_per_page = 10  
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
    if 1 <= number <= 4:  
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
    language = get_user_language()
    client_name = get_client_name(client_id, language)
    return render_template('client_page.html',
                         content=TRANSLATIONS[language],
                         current_lang=language,
                         client_name=client_name,
                         client_id=client_id)

@app.route('/get_clients/<int:page>')
def get_clients(page):
    items_per_page = 10
    total_clients = 70
    start_idx = (page - 1) * items_per_page + 1
    end_idx = min(start_idx + items_per_page - 1, total_clients)

    language = get_user_language()
    # Create a dictionary of translated client names for the current language
    translated_clients = {i: get_client_name(i, language) for i in range(1, 71)}

    clients_html = render_template('_clients_grid.html',
                                start_idx=start_idx,
                                end_idx=end_idx,
                                client_names=translated_clients,
                                content=TRANSLATIONS[language],
                                current_lang=language)

    return jsonify({
        'html': clients_html,
        'total_pages': (total_clients + items_per_page - 1) // items_per_page,
        'current_page': page
    })

@app.route('/faq/why-soundproof')
def why_soundproof():
    language = get_user_language()
    return render_template('why_soundproof.html',
                         content=TRANSLATIONS[language],
                         current_lang=language)

@app.route('/faq/why-electromagnetic-shielding')
def why_electromagnetic_shielding():
    language = get_user_language()
    return render_template('why_electromagnetic_shielding.html',
                         content=TRANSLATIONS[language],
                         current_lang=language)

@app.route('/faq/soundproof-room-standards')
def soundproof_room_standards():
    language = get_user_language()
    return render_template('soundproof_room_standards.html',
                         content=TRANSLATIONS[language],
                         current_lang=language)