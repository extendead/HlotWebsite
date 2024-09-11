from secrets import token_urlsafe

from flask import Flask, render_template, request

from src.database import Database

app = Flask(__name__)
db = Database()


@app.route('/')
def main():
    """ Форма обратной связи """
    return render_template("index.html")


if __name__ == '__main__':
    app.secret_key = token_urlsafe(128)
    app.run(debug=True)
