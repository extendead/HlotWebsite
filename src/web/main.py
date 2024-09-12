from secrets import token_urlsafe

from flask import Flask, render_template, request, redirect, flash, url_for
from flask_login import LoginManager, login_user, login_required

from src.database import Database
from src.web.system.modules.check import Check
from src.web.system.modules.login import UserLogin

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "admin_login"
db = Database()
check = Check


# def redirect_dest(fallback):
#     dest = request.args.get('next')
#     try:
#         dest_url = url_for(dest)
#     except:
#         return redirect(fallback)
#     return redirect(dest_url)


# @login_manager.user_loader
# def load_user(admin_id):
#     print("load_user")
#     return UserLogin().fromDB(admin_id=admin_id, database=db)

@login_manager.user_loader
def load_user(user_login):
    print(user_login)
    return UserLogin().fromDB(user_login, db)


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
        # user = db.select_login_data(login_)[0]
        ul = UserLogin()
        if check_data:   # user and :
            # user_login = ul.create(user)
            # load_user(user_login)
            login_user(UserLogin().create(login_))
            print(ul.get_id())
            return redirect(f"/admin-_-panel/{ul.get_id()}")      # redirect_dest(url_for(f"admin_panel"))
        else:
            flash("Неверные данные для входа.")
            return redirect('/admin-_-login')
    return render_template("admin_login.html")


@app.route('/admin-_-panel/<admin_id>', methods=['POST', 'GET'])
@login_required
def admin_panel(admin_id):
    ul = UserLogin()
    flash("Done!")
    return render_template("admin.html")


# @login_manager.unauthorized_handler
# def unauthorized():
#     flash("You have to be logged in to access this page.")
#     return redirect(url_for('admin_login', next=request.endpoint))


if __name__ == '__main__':
    app.secret_key = token_urlsafe(128)
    app.run(debug=True)
