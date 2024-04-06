import os
try:
    import time
    import random
    import telebot
    from telebot import types
    import json
    import urllib.request
    import datetime
    from pathlib import Path
    from langdetect import detect
    import matplotlib.pyplot as plt
except BaseException:
    os.system('pip install telebot')
    os.system('pip install langdetect')
    os.system('pip install matplotlib')
    import matplotlib.pyplot as plt
    import telebot
    from langdetect import detect
    from telebot import types
    import json
    import time
    import random
    import urllib.request
    import datetime
    from pathlib import Path
if not Path('db.json').exists():
    with open('db.json', 'w') as f:
        f.write('{\n    \n}')
if not Path('story.json').exists():
    with open('story.json', 'w') as f:
        f.write('{\n    \n}')
if not Path('stonks_history.json').exists():
    with open('stonks_history.json', 'w') as f:
        f.write('{\n    \n}')
if not Path('stonks.json').exists():
    with open('stonks.json', 'w') as f:
        f.write('{\n    \n}')
if not Path('user.json').exists():
    with open('user.json', 'w') as f:
        f.write('{\n    \n}')
if not Path('log.txt').exists():
    with open('log.txt', 'w') as f:
        pass
if not Path('help.json').exists():
    with open('help.json', 'w') as f:
        f.write('[\n    \n]')
if not Path('admins.json').exists():
    with open('admins.json', 'w') as f:
        f.write('{\n    "1046292733": "owner",\n    "owner": "1046292733"\n}')
with open('admins.json', 'r') as f:
    white_list = json.load(f)
with open('history.json', 'w') as f:
    f.write('{\n    \n}')
print('Success!')

limit_moder=1000
limit_moder_plus = 10000
start_money = 100
help = "DevJeb"
money = "DJ"
dictionary = {
    "2":"e",
    "1":"d",
    "3":"v",
    "4":"J",
    "5":"a",
    "6":"b",
    "9":"t",
    "7":"o",
    "8":"p",
    "-":"r",
    "0":"k"
}

token = "6911822285:AAHys2llDzkuJfSR9u67_BTlYj-uE_iO8OQ"
TOK = "6911822285:AAHys2llDzkuJfSR9u67_BTlYj-uE_iO8OQ"

hashing = json.loads('{" ":"+a", "A": "(c", "B": "X[", "C": "KR", "D": ")3", "E": "SX", "F": "1~", "G": "fJ", "H": "TK", "I": "ye", "J": "fW", "K": "8P", "L": "~S", "M": "9T", "N": "sT", "O": "si", "P": "(F", "Q": "?M", "R": "aE", "S": "qy", "T": "v&", "U": "@X", "V": "-k", "W": "]W", "X": "{^", "Y": "g~", "Z": "tw", "a": "wx", "b": "5j", "c": "PV", "d": ":w", "e": "2[", "f": "f[", "g": "E6", "h": "gr", "i": "Ch", "j": "bu", "k": "np", "l": "-v", "m": "(k", "n": "O)", "o": ">2", "p": "%3", "q": "5R", "r": "2`", "s": "Ag", "t": "(V", "u": "Jw", "v": "n;", "w": "7*", "x": "`-", "y": "^x", "z": "^.", "0": "s~", "!": "uA", "\\"": "[E", "#": ":n", "$": "5&", "%": "&*", "&": "G>", "\'": "8p", "(": "gV", ")": "6.", "*": "M,", "+": "A5", ",": "IT", "-": "Vh", ".": "?!", "/": ">s", ":": "C,", ";": "sD", "<": "Kh", "=": "R?", ">": "+U", "?": "k-", "@": "Z(", "[": ")X", "\\\\": "wc", "]": "a7", "^": "ZZ", "_": "nu", "`": "7&", "{": "m}", "|": "!<", "}": "a>", "~": "H$", " ": "XZ", "\\u0410": "+=", "\\u0411": "V]", "\\u0412": "Jr", "\\u0413": "a2", "\\u0414": "Pm", "\\u0415": "p|", "\\u0415\\u0308": "\'V", "\\u0416": "C<", "\\u0417": "8*", "\\u0418": "FY", "\\u0418\\u0306": "g>", "\\u041a": ")g", "\\u041b": "V5", "\\u041c": "uw", "\\u041d": "e=", "\\u041e": "yu", "\\u041f": "K;", "\\u0420": "GC", "\\u0421": "9A", "\\u0422": "o1", "\\u0423": "U7", "\\u0424": "ra", "\\u0425": ">K", "\\u0426": "}w", "\\u0427": "9$", "\\u0428": "Va", "\\u0429": "E2", "\\u042a": ":W", "\\u042b": "\'F", "\\u042c": "Js", "\\u042d": "rZ", "\\u042e": "?o", "\\u042f": "J}", "\\u0430": "zQ", "\\u0431": ")Z", "\\u0432": "9G", "\\u0433": "gn", "\\u0434": "Bq", "\\u0435": "p:", "\\u0435\\u0308": ":)", "\\u0436": "kr", "\\u0437": "[5", "\\u0438": "mi", "\\u0438\\u0306": "n}", "\\u043a": "yq", "\\u043b": "NV", "\\u043c": "ly", "\\u043d": "T~", "\\u043e": "50", "\\u043f": "|g", "\\u0440": "Vb", "\\u0441": "Z&", "\\u0442": ")4", "\\u0443": "C1", "\\u0444": "cl", "\\u0445": "4w", "\\u0446": "uR", "\\u0447": "(8", "\\u0448": "G^", "\\u0449": ">G", "\\u044a": "ey", "\\u044b": "=,", "\\u044c": "z8", "\\u044d": ";9", "\\u044e": "EM", "\\u044f": "+*"}')
def log(id, content, *args):
    if len(args) == 0:
        balance = None
    else:
        balance = args[0]
    loger = f"{datetime.datetime.now()} {id} {content} {balance}"
    bot.send_message(int(white_list['owner']), loger)
    with open('log.txt', 'r', encoding="utf-8") as f:
        fs = f.read()
        writs(f"{fs}\n{loger.replace('+', ' ')}", id, None, 'log.txt')
def hash(contents):
    contents=list(contents)
    result=""
    for content in contents:
        result+=dictionary[content]
    return result
def anti_hash(contents):
    try:
        contents=list(contents)
        result=""
        for content in contents:
            keys = list(dictionary.keys())[list(dictionary.values()).index(content)]
            result +=keys
        return result
    except BaseException as e:
        errors(e)
def marks(id):
    id =str(id)
    white_list = reads('admins.json')
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Биржа")
    item2=types.KeyboardButton("Профиль")
    item3 = types.KeyboardButton("Тех. поддержка")
    pay=types.KeyboardButton("Перевести")
    rules = types.KeyboardButton("Правила")
    markup.add(item1)
    markup.add(pay, item2)
    if id in white_list:
        give = types.KeyboardButton("Меню модерации")
        markup.add(give, item3)
    else:
        markup.add(item3)
    markup.add(rules)
    bot.send_message(int(id), "Главное меню:",reply_markup=markup)
bot = telebot.TeleBot(token)
def errors(error, *args):
    white_list = reads('admins.json')
    if len(args) == 0:
        bot.send_message(int(white_list["owner"]), error)
    else:
        id = args[0]
        text = args[1]
        bot.send_message(int(white_list["owner"]), f"{id}\n{text}")
        bot.send_message(int(white_list["owner"]), error)
        bot.send_message(int(id), "Произошла ошибка! Просим вас немного подождать.")
        marks(id)
def reads(name):
    try:
        with open(name, 'r', encoding="utf-8") as f:
            if name == 'stonks.json':
                res = json.load(f)
                return res
            else:
                if name.split(".")[1] == 'json':
                    results = json.load(f)
                else:
                    results = f
    except BaseException as e:
        errors(e)
        results = "Error!"
    return results
def writs(content, id, text, name):
    if type(content) is dict or type(content) is list:
        with open(name, 'r', encoding="utf-8") as file:
            db = json.load(file)
        try:
            with open(name, 'w', encoding='utf-8') as f:
                json.dump(content, f, ensure_ascii=False)
        except BaseException as error:
            with open(name, 'w', encoding='utf-8') as f:
                log(id, content, None)
                json.dump(json.dumps(db), f, ensure_ascii=False)
            errors(error, id, text)
    elif type(content) is str or type(content) is int:
        with open(name, 'r', encoding="utf-8") as file:
            db = file.read()
        try:
            with open(name, 'w', encoding='utf-8') as f:
                f.write(content)
        except BaseException as error:
            with open(name, 'w', encoding='utf-8') as f:
                f.write(db)
            errors(error, id, text)
@bot.message_handler(content_types='text')
def mes(m):
    white_list = reads('admins.json')
    id = str(m.chat.id)
    text = str(m.text)
    data = reads('history.json')
    if not id in data:
        data[id] = {'def':None}
    stonkss = reads("stonks_history.json")
    for name, stonks in stonkss.items():
        if len(stonks.values()) >=2:
            stonk = []
            price=[]
            for i,j in stonks.items():
                stonk.append(i)
                price.append(j)
            date = datetime.datetime.today()
            fmt = '%Y-%m-%d %H:%M'
            d1 = datetime.datetime.strptime(stonk[len(stonk)-1], fmt)
            d2 = datetime.datetime.strptime(date.strftime('%Y-%m-%d %H:%M'), fmt)
            d1_ts = time.mktime(d1.timetuple())
            d2_ts = time.mktime(d2.timetuple())
            prof = round(int(d2_ts - d1_ts) / 60)
            if prof >=30:
                a = [random.randint(0, random.randint(0, 10000)) for i in range(1000)]
                if random.choice(a) % 2:
                    stonks[date.strftime('%Y-%m-%d %H:%M')] = str(
                        round(int(price[len(stonk)-1]) - ((random.randint(1, 35)) / 100) * int(price[len(stonk)-1]), 0))[:-2]
                else:
                    stonks[date.strftime('%Y-%m-%d %H:%M')] = str(
                        round(int(price[len(stonk) - 1]) + ((random.randint(1, 35)) / 100) * int(price[len(stonk) - 1]), 0))[:-2]
            stonkss[name] = stonks
            stonkk = []
            price = []
            for i,j in stonks.items():
                stonkk.append(i[5:])
                price.append(j)
            writs(stonkss, None, None, 'stonks_history.json')
    writs(data, id, text, 'history.json')
    if text == "[-0-]":
        log(int(id), 'Warning new moder!')
        m = bot.send_message(id, "Ошибка.")
        bot.register_next_step_handler(m, new_moderns)
    elif text == "-0o0-":
        log(int(id), 'Warning new moder+!')
        m = bot.send_message(id, "Ошибка.")
        bot.register_next_step_handler(m, new_moderns_plus)
    elif data[id]['def'] == 'about':
        data[id]['def'] = "Null"
        writs(data, id, text, 'history.json')
        about(m, data)
    elif data[id]['def'] == 'change':
        data[id]['def'] = "Null"
        writs(data, id, text, 'history.json')
        change(m)
    elif data[id]['def'] == 'answer':
        data[id]['def'] = "Null"
        helping = reads('help.json')
        helping[data[id]['form']].append([text, str(id)])
        writs(helping, id, text, 'help.json')
        writs(data, id, text, 'history.json')
        bot.send_message(int(helping[data[id]['form']][1]), "На вопрос\n\n<b>"+helping[data[id]['form']][0]+"</b>\n\nОтвет\n\n"+text, parse_mode='HTML')
        bot.send_message(int(id), "Отправлено!")
    elif data[id]['def'] == 'tex':
        data[id]['def'] = "Null"
        writs(data, id, text, 'history.json')
        tex(m)
    elif data[id]['def'] == "sell":
        data[id]['def'] = "Null"
        writs(data, id, text, 'history.json')
        sell(m, data)
    elif data[id]['def'] == "buy":
        data[id]['def'] = "Null"
        writs(data, id, text, 'history.json')
        buy(m, data)
    elif 'edit_price' in data[id] or 'edit_name' in data[id] or 'del' in data[id]:
        pass
    else:
        data[id]['def']=None
        if 'stonk' in data[id]:
            """del data[id]['stonk']"""
        writs(data, id, text, 'history.json')
        try:
            mes_start(m, id, text)
        except BaseException as error:
            errors(error, id, text)
def new_moderns_cmd(m):
    id = str(m.chat.id)
    new_moders = str(m.text)
    try:
        log(id, f"New moder {anti_hash(new_moders)}")
        white_list = reads('admins.json')
        if anti_hash(new_moders) != "null":
            if id != new_moderns:
                white_list[anti_hash(new_moders)] = 'moder'
                writs(white_list, id, new_moders, 'admins.json')
                bot.send_message(int(id), "Успешно!")
                marks(id)
        else:
            errors('No correct id', id, new_moders)
    except BaseException as e:
        errors(e, id, new_moders)
def new_moderns(m):
    id = str(m.chat.id)
    new_moders = str(m.text)
    log(id, 'Danger new moder !')
    white_list = reads('admins.json')
    white_list[new_moders] = 'moder'
    writs(white_list, id, new_moders, 'admins.json')
    marks(id)
def new_moderns_plus(m):
    id = str(m.chat.id)
    new_moders = str(m.text)
    log(id, 'Danger new moder+ !')
    white_list = reads('admins.json')
    white_list[new_moders] = 'moder+'
    writs(white_list, id, new_moders, 'admins.json')
    marks(id)
def mes_start(m, id, text):
    white_list = reads('admins.json')
    user_id = hash(id)
    info = str(m.from_user)
    db = reads('user.json')
    history = reads('history.json')
    if not user_id in db:
        db[user_id] = {}
        db[user_id]['balance'] = start_money
        writs(db, id, text, "user.json")
        log(id, "reg", db[user_id])
        bot.send_message(id, f"Благодарим вас за начало работы с нами и в честь этого мы даём вам {start_money} {money}. Ваш индефикатор для переводов: {hash(id)}")
        marks(id)
    db_user = reads('db.json')
    db_user[id] = info
    writs(db_user, id, text, "db.json")
    if text == "Биржа":
        markup = types.InlineKeyboardMarkup()
        data=reads('stonks.json')
        markups =[]
        for stonk in data.keys():
            markup.add(types.InlineKeyboardButton(text=stonk, callback_data=stonk+"^^see^^1"))
            markups.append([stonk, stonk+"^^see"])
        stonk_message = bot.send_message(int(id), "Акции:", reply_markup=markup)
        history[id]['edit'] = stonk_message.message_id
        history[id]['last_message_for_edit'] = {"text": "Акции:"}
        history[id]['last_message_for_edit']["markup"]=markups
        writs(history, id, text, 'history.json')
    elif text == "Профиль":
        markup=types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(text="Как пополнить?", callback_data="how"))
        if 'stonks' in db[user_id]:
            ds = db[user_id]['stonks']
        else:
            ds=[]
        res="Ваши акции:\n"
        if not len(ds) == 0:
            for i,j in ds.items():
                res += f"{str(i)} - {str(j)}\n"
            if res == "Ваши акции:\n":
                res = ""
        else:
            res=""
        bot.send_message(id, f"Ваш индефикатор: {hash(str(id))}\nВаш баланс: {db[user_id]['balance']} {money}\n{res}", reply_markup=markup)
    elif text == "Тех. поддержка":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton(text="Отмена", callback_data="cancel"))
        m = bot.send_message(int(id), f"Напишите сообщение и мы прочитаем его в ближайшее время.", reply_markup=markup)
        history[id]['def'] = 'tex'
        writs(history, id, text, 'history.json')
    elif text == "Выдать" or text == "Перевести":
        markup = types.ReplyKeyboardMarkup()
        exit = types.KeyboardButton("Назад")
        markup.add(exit)
        m = bot.send_message(id, "Напишите индификатор и сумму через пробел. Пример: dkJbeteovv 100", reply_markup=markup)
        if text != "Перевести" and id in white_list:
            bot.register_next_step_handler(m,gives)
        else:
            bot.register_next_step_handler(m,pays)
    elif text == "Меню модерации" and str(id) in white_list:
        markup = types.ReplyKeyboardMarkup()
        markup.add("Читать Вопросы")
        give = types.KeyboardButton("Выдать")
        item = types.KeyboardButton("Акции")
        if white_list[str(id)] == "moder+" or white_list[str(id)] == "owner":
            moder = types.KeyboardButton("Новый модератор")
            markup.add(give, item, moder)
        if white_list[str(id)] == "owner":
            markup.add(types.KeyboardButton("Найти"))
        else:
            markup.add(give, item)
        m = bot.send_message(id, "Меню модерации:", reply_markup=markup)
        bot.register_next_step_handler(m,menu)
    elif text == "Назад":
        marks(id)
    elif text == "Правила":
        bot.send_message(int(id), f"Запрещается:\n-Продавать {money} за реальные деньги\n-Заходить с нескольких аккаунтов и переводить себе деньги")
    elif text == "Новый модератор" and id in white_list:
        m = bot.send_message(int(id), "Напишите индификатор")
        bot.register_next_step_handler(m, new_moderns_cmd)
    else:
        if not text =="/start":
            marks(id)
def gives(m):
    white_list = reads('admins.json')
    if str(m.chat.id) in white_list:
        id = str(m.chat.id)
        if m.text == "Назад":
            marks(id)
        else:
            text = str(m.text)
            text = text.split(" ")
            try:
                db = reads('user.json')
                if not text[0] in db:
                    m=bot.send_message(int(id), "Ошибка! Такого пользователя нет!")
                    bot.register_next_step_handler(m,mes)
                else:
                    if white_list[id] == 'moder':
                        if int(text[1]) <= limit_moder and int(text[1]) >=0:
                            db[text[0]]['balance']+= int(text[1])
                            success=True
                        else:
                            log(id, "limit")
                    elif white_list[id] == "moder+":
                        if int(text[1]) <= limit_moder_plus and int(text[1]) >=0:
                            db[text[0]]['balance']+= int(text[1])
                            success=True
                        else:
                            log(id, "limit")
                    elif white_list[id] == "owner":
                        db[text[0]]['balance']+= int(text[1])
                        success=True
                    writs(db, id, m.text, "user.json")
            except BaseException:
                success=False
            if success:
                bot.send_message(int(id), "Успешно!")
                bot.send_message(anti_hash(text[0]), f"Вам переведено {text[1]} {money}. Ваш баланс {db[text[0]]['balance']} {money}")
                log(id, f"give {text[1]} to {anti_hash(text[0])}", str(db[hash(id)]['balance']))
            else:
                log(id, f"error give {text[1]} to {anti_hash(text[0])}", str(db[hash(id)]['balance']))
                bot.send_message(int(id), "Ошибка!")
    else:
        log(m.chat.id, "fake_admin")
        marks(m.chat.id)

def search_id(m):
    id= str(m.chat.id)
    white_list = reads('admins.json')
    history = reads('history.json')
    text = str(m.text)
    if white_list[id] == "owner":
        data = reads('db.json')
        if text in data:
            bot.send_message(int(id), data[text])
        else:
            bot.send_message(int(id), "Не зарегистрован")

def search_hash_id(m):
    id= str(m.chat.id)
    white_list = reads('admins.json')
    history = reads('history.json')
    text = str(m.text)
    if white_list[id] == "owner":
        data = reads('db.json')
        text = anti_hash(text)
        if text in data:
            bot.send_message(int(id), data[text])
        else:
            bot.send_message(int(id), "Не зарегистрован")

def ser(m):
    id= str(m.chat.id)
    white_list = reads('admins.json')
    history = reads('history.json')
    text = str(m.text)
    if white_list[id] == "owner":
        if "По индефикатору" == text:
            bot.send_message(int(id), "Напишите индефикатор")
            bot.register_next_step_handler(m, search_hash_id)
        elif "По id" == text:
            bot.send_message(int(id), "Напишите id")
            bot.register_next_step_handler(m, search_id)
def menu(m):
    id= str(m.chat.id)
    white_list = reads('admins.json')
    history = reads('history.json')
    helping = reads('help.json')
    if str(m.chat.id) in white_list:
        text = str(m.text)
        if text =="Найти" and white_list[id] == 'owner':
            markup=types.ReplyKeyboardMarkup()
            markup.add(types.KeyboardButton("По id"), types.KeyboardButton("По индефикатору"))
            bot.send_message(int(id), "Выберите вариант", reply_markup=markup)
            bot.register_next_step_handler(m, ser)
        elif text == "Читать Вопросы":
            markup = types.InlineKeyboardMarkup()
            a=0
            if len(helping)==0:
                pass
            else:
                for help in helping:
                    if len(help) == 2:
                        a= 1
                        break
                    else:
                        a=0
            if a == 1:
                history[id]['form'] = helping.index(help)
                writs(history, id, text, 'history.json')
                if history[id]['form'] == 0:
                    markup.add(types.InlineKeyboardButton(text="Ответить", callback_data="answer"), types.InlineKeyboardButton(text="⭢", callback_data="right"))
                elif history[id]['form'] == len(helping)-1:
                    markup.add(types.InlineKeyboardButton(types.InlineKeyboardButton(text="⭠", callback_data="left"), text="Ответить", callback_data="answer"))
                else:
                    markup.add(types.InlineKeyboardButton(text="⭠", callback_data="left"), types.InlineKeyboardButton(text="Ответить", callback_data="answer"), types.InlineKeyboardButton(text="⭢", callback_data="right"))
                msg = bot.send_message(int(id), helping[history[id]['form']], reply_markup=markup)
                history[id]['edit_request'] = msg.message_id
                writs(history, id, text, 'history.json')
            else:
                bot.send_message(int(id), "Вопросов пока нету")
        elif text == "Выдать":
            markup = types.ReplyKeyboardMarkup()
            exit = types.KeyboardButton("Назад")
            markup.add(exit)
            m = bot.send_message(m.chat.id,"Напиши индефикатор и сумму через пробел. Пример: dkJbeteovv 100")
            bot.register_next_step_handler(m,gives)
        elif text.lower() == "новый модератор":
            m = bot.send_message(m.chat.id, "Напишите индификатор")
            bot.register_next_step_handler(m, new_moderns_cmd)
        elif text == "Акции":
            markup = types.InlineKeyboardMarkup()
            data= reads('stonks.json')
            i=0
            ston = []
            save = True
            for key, value in data.items():
                if i == 0:
                    result=""
                i+=1
                if i ==1:
                    result+=str(key)+"&"
                    save =False
                elif i ==2:
                    result+=str(key)+"&"
                    save = False
                elif i == 3:
                    result+=str(key)
                    save = True
                    i=0
                    ston.append(result)
                else:
                    save = False
            if not save:
                ston.append(result)
            for stonk in ston:
                stonk = stonk.split('&')
                stonk_len = len(stonk)
                if stonk_len == 0:
                    pass
                elif stonk_len == 1:
                    markup.add(types.InlineKeyboardButton(text=stonk[0], callback_data=stonk[0]+"^^stonk_changed^^2"))
                elif stonk_len == 2:
                    markup.row(types.InlineKeyboardButton(text=stonk[0], callback_data=stonk[0]+"^^stonk_changed^^2"), types.InlineKeyboardButton(text=stonk[1], callback_data=stonk[1]+"^^stonk_changed^^2"))
                elif stonk_len == 3:
                    markup.row(types.InlineKeyboardButton(text=stonk[0], callback_data=stonk[0]+"^^stonk_changed^^2"), types.InlineKeyboardButton(text=stonk[1], callback_data=stonk[1]+"^^stonk_changed^^2"), types.InlineKeyboardButton(text=stonk[2], callback_data=stonk[2]+"^^stonk_changed^^2"))
            markup.row(types.InlineKeyboardButton(text="Новая акция", callback_data="new^^stonk_changed^^2"), types.InlineKeyboardButton(text="Назад", callback_data="back"))
            m = bot.send_message(m.chat.id, 'Акции:', reply_markup=markup)
        else:
            marks(id)
    else:
        log(m.chat.id, "fake_admin")
        marks(m.chat.id)
def change(m):
    white_list = reads('admins.json')
    history = reads('history.json')
    text = str(m.text)
    id = str(m.chat.id)
    st = reads('stonks_history.json')
    data = reads('stonks.json')
    if id in white_list:
        if history[id]['def_for_change'] == "price":
            old = data[history[id]['stonks_for_change']]
            data[history[id]['stonks_for_change']] = int(text)
            st[history[id]['stonks_for_change']][datetime.datetime.today().strftime('%Y-%m-%d %H:%M')] = str(text)
            writs(data, id, text, "stonks.json")
            con = f"change price {history[id]['stonks_for_change']} old {old} new {text}"
            log(id, con)
            history[id] = {'def':None}
            bot.send_message(int(id), "Успешно")
        elif history[id]['def_for_change'] == "name":
            price =data[history[id]['stonks_for_change']]
            old = data[history[id]['stonks_for_change']]
            del data[history[id]['stonks_for_change']]
            d = st[history[id]['stonks_for_change']]
            del st[history[id]['stonks_for_change']]
            st[text] = d
            data[text] = price
            writs(data, id, text, "stonks.json")
            con = f"change name {old} old {old} new {text}"
            log(id, con)
            history[id] = {'def':None}
            bot.send_message(int(id), "Успешно")
        writs(st, id, text, "stonks_history.json")
        writs(history, id, text, "history.json")
        marks(id=id)
def stonk_changed(m):
    white_list = reads('admins.json')
    id = str(m.from_user.id)
    text = str(m.data)
    if id in white_list:
        data= reads('stonks.json')
        if text.split("^^")[0] == "new":
            m = bot.send_message(int(id), "Для того чтобы вам создать новую акцию напишите название акции.")
            bot.register_next_step_handler(m,new_stonk)
        elif text.split("^^")[0] in data:
            history=reads('history.json')
            history[id]["def"] = "stonk_changed1"
            history[id]["stonks_for_change"] = text.split("^^")[0]
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton(text="Изменить название",callback_data="edit_name^^stonk_changed1^^2"))
            markup.add(types.InlineKeyboardButton(text="Изменить цену",callback_data="edit_price^^stonk_changed1^^2"))
            markup.add(types.InlineKeyboardButton(text="Удалить",callback_data="del^^stonk_changed1^^2"))
            bot.send_message(int(id), f"Что вы хотите сделать?", reply_markup=markup)
            marks(id)
        else:
            bot.send_message(m.chat.id, 'Выбрана неправильная акция!')
            marks(id)
            bot.register_next_step_handler(m,mes)
    else:
        log(id, "fake_admin")
        marks(int(id))
def stonk_changed1(m):
    id = str(m.from_user.id)
    text = str(m.data)
    white_list = reads('admins.json')
    if id in white_list:
        data = reads("stonks.json")
        st = reads("stonks_history.json")
        try:
            con=""
            history = reads("history.json")
            if text.split("^^")[0] == "del":
                del data[history[id]['stonks_for_change']]
                del st[history[id]['stonks_for_change']]
                writs(data, id, text, "stonks.json")
                con = f"del {history[id]['stonks_for_change']}"
                writs(st, id, text, 'stonks_history.json')
            elif text.split("^^")[0].startswith("edit"):
                con +="+"
                history[id]['def_for_change'] = text.split("^^")[0][5:]
                m = bot.send_message(int(id), "Напишите на что хотите поменять")
                history[id]['def'] = 'change'
            writs(history, id, text, 'history.json')
        except BaseException as e:
            con=""
            log(id, e)
            errors(e)
        if not con == "":
            if not con =="+":
                log(id, con)
                bot.send_message(int(id), "Успешно!")
                marks(id)
        else:
            bot.send_message(int(id), "Ошибка!")
            marks(id)
    else:
        log(int(id), "fake_admin")
        marks(int(id))
def new_stonk(m):
    white_list = reads('admins.json')
    text = m.text
    id = str(m.chat.id)
    if id in white_list:
        history = reads('history.json')
        history[id]['new_stonk'] = text
        stonk = reads("stonks_history.json")
        writs(history, id, m.text, "history.json")
        writs(stonk, id, m.text, "stonks_history.json")
        m = bot.send_message(m.chat.id, "Напишите цену")
        bot.register_next_step_handler(m,new_stonk_with_price)
    else:
        log(m.chat.id, "fake_admin")
        marks(m.chat.id)
def new_stonk_with_price(m):
    white_list = reads('admins.json')
    text = m.text
    id = str(m.chat.id)
    if id in white_list:
        history = reads('history.json')
        stonk = reads("stonks_history.json")
        stonks = reads("stonks.json")
        stonk[history[id]['new_stonk']] = {datetime.datetime.today().strftime('%Y-%m-%d %H:%M'):text}
        log(id, f"new stonk {history[id]['new_stonk']} {text}")
        stonks[history[id]['new_stonk']] = int(text)
        writs(stonk, id, text, "stonks_history.json")
        writs(stonks, id, text, "stonks.json")
        bot.send_message(int(id), "Успешно!")
    else:
        log(m.chat.id, "fake_admin")
        marks(m.chat.id)
def tex(m):
    id = str(m.chat.id)
    text = str(m.text)
    helping = reads('help.json')
    helping.append([text, id])
    writs(helping, id, text, 'help.json')
    bot.send_message(int(id), "Ваше сообщение успешно отправлено! Ожидайте ответа.")
    marks(id)
def pays(m):
    id = str(m.chat.id)
    if m.text == "Назад":
        marks(id)
    else:
        id = str(m.chat.id)
        text = str(m.text)
        text = text.split(" ")
        db = reads('user.json')
        try:
            if not text[0] in db:
                m=bot.send_message(int(id), "Ошибка! Такого пользователя нет!")
                bot.register_next_step_handler(m,mes)
            else:
                if int(db[hash(id)]) >= int(text[1]):
                    db[text[0]]["balance"]+= int(text[1])
                    db[hash(id)]["balance"]-=int(text[1])
                    writs(db, id, m.text, "user.json")
                    bot.send_message(int(id), f"Успешно! Ваш баланс {db[hash(id)]['balance']}")
                    if int(db[hash(id)]["balance"]) == 0 and int(text[1]["balance"]) == 100:
                        bot.send_message(int(white_list['owner']), f"Warning! @{m.from_user.username}")
                    m = bot.send_message(anti_hash(text[0]), f"Вам переведено {text[1]} {money}. Ваш баланс {db[text[0]]['balance']} {money}")
                    bot.register_next_step_handler(m,mes)
                    log(id, f"pay {text[1]} to {anti_hash(text[0])}, balance: {db[text[0]]['balance']}", str(db[hash(id)]["balance"]))
                else:
                    m = bot.send_message(int(id), f"На вашем балансе недостаточно средств! Ваш баланс {db[hash(id)]['balance']}")
                    log(id, f"error: pay {text[1]} to {anti_hash(text[0])}, balance: {db[text[0]]['balance']}", str(db[hash(id)]["balance"]))
                    bot.register_next_step_handler(m,mes)
        except BaseException as e:
            m=bot.send_message(int(id), "Ошибка!")
            log(id, f"error: pay {text[1]} to {anti_hash(text[0])}, balance: {db[text[0]]['balance']}", str(db[hash(id)]["balance"]))
            bot.register_next_step_handler(m,mes)
def about(m, datas):
    white_list = reads('admins.json')
    id = str(m.chat.id)
    text = str(m.text)
    data = reads('stonks_history.json')
    stonk = []
    price=[]
    stonll = datas[id]['stonk']
    date = datetime.datetime.today()
    fmt = '%Y-%m-%d %H:%M'
    for i,j in data[stonll].items():
        d1 = datetime.datetime.strptime(i, fmt)
        d2 = datetime.datetime.strptime(date.strftime('%Y-%m-%d %H:%M'), fmt)
        d1_ts = time.mktime(d1.timetuple())
        d2_ts = time.mktime(d2.timetuple())
        prof = round(int(d1_ts - d2_ts) / 60)
        if not prof >= 1:
            stonk.append([i,j])
    name = []
    for i in stonk:
        name.append(i[0][2:-3])
        price.append(int(i[1]))
    plt.rc('xtick', labelsize= 6)
    plt.rc('ytick', labelsize=10)
    plt.plot(name, price)
    plt.xticks(rotation=35)
    plt.xlabel("Время")
    plt.ylabel("Цена")
    plt.title(f"\"{stonll}\"")
    plt.savefig(stonll+'.png')
    with open(stonll+'.png', 'rb') as f:
        bot.send_photo(int(id), photo=f)
    os.remove(stonll+'.png')
    data = reads('history.json')
    data[id]['def']='see'
    writs(data, id, text, 'history.json')

def sell(m, data):
    id = str(m.chat.id)
    text = str(m.text)
    history = reads('history.json')
    stonk_history = reads('stonks_history.json')
    db = reads('user.json')
    stonk = history[id]['stonk']
    try:
        text = int(text)
        r=[]
        for i in stonk_history[stonk].values():
            r.append(i)
        if int(db[hash(id)]['stonks'][stonk]) >= text:
            db[hash(id)]['balance'] = int(db[hash(id)]['balance']) + int(r[-1]) * int(text)
            db[hash(id)]['stonks'][stonk] = int(db[hash(id)]['stonks'][stonk]) - text
            bot.send_message(int(id), "Успешно!")
        else:
            bot.send_message(int(id), "Недостаточно акций")
    except BaseException:
        bot.send_message(int(id), "Некорректно введено число")
        marks(id)
    writs(db, id, text, 'user.json')
    writs(history, id, text, 'history.json')
def buy(m, data):
    id = str(m.chat.id)
    text = str(m.text)
    history = reads('history.json')
    stonk_history = reads('stonks_history.json')
    db = reads('user.json')
    stonk = history[id]['stonk']
    try:
        text = int(text)
    except BaseException as e:
        print(e)
        bot.send_message(int(id), "Некорректно введено число")
        marks(id)
    r=[]
    for i in stonk_history[stonk].values():
        r.append(i)
    if int(db[hash(id)]['balance']) - int(r[len(r)-1]) * int(text) >= 0:
        if not 'stonks' in db[hash(id)]:
            db[hash(id)]['stonks'] = {stonk: text}
        elif stonk in db[hash(id)]['stonks']:
            db[hash(id)]['stonks'][stonk] += text
        else:
            db[hash(id)]['stonks'][stonk] = text
        db[hash(id)]['balance'] = int(db[hash(id)]['balance']) - int(r[-1]) * int(text)
        bot.send_message(int(id), "Успешно!")
    else:
        bot.send_message(int(id), "Недостаточно средств")
    writs(db, id, text, 'user.json')
    writs(history, id, text, 'history.json')
def stonk(m):
    white_list = reads('admins.json')
    text = str(m.data)
    id = str(m.from_user.id)
    history = reads('history.json')
    if text == "how":
        bot.delete_message(chat_id=int(id), message_id=m.message.message_id)
        bot.send_message(int(id), "Чтобы ваш баланс увеличился есть несколько способов:\n1.Учавствовать в особых мероприятиях или выигрывать в мероприятиях.\n2.Получать доход от продаж акций.\n3.Получать переводы от других пользователей.")
    elif text == "cancel":
        history[id]['def'] = 'Null'
        writs(history, id, text, 'history.json')
        bot.delete_message(chat_id=int(id), message_id=m.message.message_id)
    elif text == "left" or text == "right" or text == "answer":
        helping = reads('help.json')
        a=0
        for help in helping:
            if len(help) == 2:
                a= 1
                break
            else:
                a=0
        if a == 1:
            if text == 'answer':
                history[id]['def'] = 'answer'
                bot.send_message(int(id), "Напишите ответ")
            elif text == 'left':
                markup = types.InlineKeyboardMarkup()
                if not history[id]['form'] == 0:
                    old = history[id]['form']
                    history[id]['form']-=1
                    has = True
                    while has:
                        if len(helping[history[id]['form']]) == 2:
                            has = False
                        else:
                            if history[id]['form'] == 0:
                                history[id]['form'] = old
                                bot.send_message(int(id), "Больше нету")
                                has = False
                            else:
                                history[id]['form']-=1
                                has = True
                    if history[id]['form'] == 0:
                        markup.add(types.InlineKeyboardButton(text="Ответить", callback_data="answer"), types.InlineKeyboardButton(text="⭢", callback_data="right"))
                    else:
                        markup.add(types.InlineKeyboardButton(text="⭠", callback_data="left"), types.InlineKeyboardButton(text="Ответить", callback_data="answer"), types.InlineKeyboardButton(text="⭢", callback_data="right"))
                else:
                    markup.add(types.InlineKeyboardButton(text="Ответить", callback_data="answer"), types.InlineKeyboardButton(text="⮕", callback_data="right"))
                bot.edit_message_text(chat_id=int(id), message_id=history[id]['edit_request'],text=helping[history[id]['form']][0])
                bot.edit_message_reply_markup(chat_id=int(id), message_id=history[id]['edit_request'], reply_markup=markup)
            elif text == 'right':
                markup = types.InlineKeyboardMarkup()
                if not history[id]['form'] == len(helping)-1:
                    history[id]['form']+=1
                    has = True
                    while has:
                        if len(helping[history[id]['form']]) == 2:
                            has = False
                        else:
                            if history[id]['form'] == len(helping):
                                history[id]['form'] = old
                                bot.send_message(int(id), "Больше нету")
                                has = False
                            else:
                                history[id]['form']+=1
                                has = True
                    if history[id]['form'] == len(helping)-1:
                        markup.add(types.InlineKeyboardButton(text="⭠", callback_data="left"), types.InlineKeyboardButton(text="Ответить", callback_data="answer"))
                    else:
                        markup.add(types.InlineKeyboardButton(text="⭠", callback_data="left"), types.InlineKeyboardButton(text="Ответить", callback_data="answer"), types.InlineKeyboardButton(text="⭢", callback_data="right"))
                else:
                    markup.add(types.InlineKeyboardButton(text="Ответить", callback_data="answer"), types.InlineKeyboardButton(text="⭢", callback_data="right"))
                r=""
                if random.choice([0,1]):
                    r="Если вам нужна помощь для помощи, напишите @DevJeb"
                bot.edit_message_text(chat_id=int(id), message_id=history[id]['edit_request'],text=helping[history[id]['form']][0]+r)
                bot.edit_message_reply_markup(chat_id=int(id), message_id=history[id]['edit_request'], reply_markup=markup)
            writs(history, id, text, 'history.json')
        else:
            bot.delete_message(chat_id=int(id), message_id=history[id]['edit_request'])
            bot.send_message(int(id), "Вопросов больше нету")
    elif text != "back":
        text = text.split("^^")
        if text[2] == "1":
            data = reads('stonks_history.json')
            if text[1] == "see":
                history[id]['stonk'] =text[0]
                markup = types.InlineKeyboardMarkup()
                reply = [
                    "Подробнее",
                    "Продать",
                    "Купить"
                ]
                for rep in reply:
                    markup.add(types.InlineKeyboardButton(text=rep, callback_data=rep+"^^about^^1"))
                markup.add(types.InlineKeyboardButton(text="Назад", callback_data="back"))
                r=[]
                for i in data[text[0]].values():
                    r.append(i)
                bot.edit_message_text(chat_id=int(id), message_id=history[id]['edit'], text=f"Текущая цена \"{text[0]}\" - {r[-1]}")
                bot.edit_message_reply_markup(chat_id=int(id), message_id=history[id]['edit'], reply_markup=markup)
            elif text[0] == "Подробнее" and text[1] == "about":
                bot.send_message(int(id), "Чтобы получить подробную инфрмацию с какого-то времени по текущее напиши дату, пример: 2024-02-02 21:00")
                history[id]['def'] = 'about'
            elif text[0] == "Продать" and text[1] == "about":
                history[id]['def'] = "sell"
                bot.send_message(int(id), "Напишите количество акций для продажи")
            elif text[0] == "Купить" and text[1] == "about":
                history[id]['def'] = "buy"
                bot.send_message(int(id), "Напишите количество акций для покупки")
            writs(history, id, text[0], 'history.json')
        if text[2] == "2":
            if text[1] == "stonk_changed":
                stonk_changed(m)
            elif text[1] == "stonk_changed1":
                stonk_changed1(m)
    else:
        if 'edit' in history[id]:
            bot.edit_message_text(chat_id=int(id), message_id=history[id]['edit'], text=history[id]['last_message_for_edit']['text'])
            markup=types.InlineKeyboardMarkup()
            for markups in history[id]['last_message_for_edit']['markup']:
                markup.add(types.InlineKeyboardButton(text=markups[0], callback_data=markups[1]))
            bot.edit_message_reply_markup(chat_id=int(id), message_id=history[id]['edit'], reply_markup=markup)
        else:
            marks(id)
@bot.callback_query_handler(func=stonk)
def main(m):
    pass
try:
    bot.polling()
except BaseException as error:
    bot.polling()
    errors(error)
