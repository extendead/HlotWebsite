from secrets import token_urlsafe

from flask import Flask, render_template, request, redirect, flash

from src.database import Database
from src.web.system.modules.check import Check
from src.web.system.modules.hasher import Hasher
from src.web.system.modules.login import UserLogin

app = Flask(__name__)
db = Database()
check = Check


@app.route('/', methods=['POST', 'GET'])
def main():
    """ Форма обратной связи """
    if request.method == "POST":
        name = request.form["name"]
        text = request.form["text"]
        phone = request.form["phone"]
        email = request.form["email"]
        social_media = "Telegram" if request.form.get("telegram") else "WhatsApp"

        if check.CheckPhone(phone):
            db.add_user(
                user_name=name,
                phone=phone,
                email=email,
                fb_text=text,
                social_media=social_media
            )

            return redirect('/#feedback')
        else:
            return "Неверный номер телефона!"
    else:
        return render_template("index.html")


@app.route('/admin-_-login', methods=['POST', 'GET'])
def admin_login():
    """ Админка """
    if request.method == "POST":
        login_ = request.form['login']
        password = request.form['password']
        check_data = check.CheckAdminLoginData(login=login_, password=password)
        if check_data:
            return redirect("/admin-_-panel")
        else:
            flash("Неверные данные для входа.")
            return redirect('/admin-_-login')
    return render_template("admin_login.html")


@app.route('/admin-_-panel')
def admin_panel():
    return render_template("admin.html")


if __name__ == '__main__':
    app.secret_key = token_urlsafe(128)
    app.run(debug=True)
