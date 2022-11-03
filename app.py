from os import path
from flask import Flask

from models import create_db_app
from models import DB_NAME
from views import views

app = Flask(__name__)
app.config['SECRET_KEY'] = 'h4sski'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'


def main():

    app.register_blueprint(views, url_prefix='/')

    create_db_app()

    app.run(debug=True)


if __name__ == '__main__':
    main()
