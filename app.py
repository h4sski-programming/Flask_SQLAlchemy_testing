from os import path
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey, create_engine
from sqlalchemy.orm import relationship

import models
from models import db, User, DB_NAME
from views import views

# import models
# from models import DB_NAME, create_db_app, db, User, Activity

app = Flask(__name__)

app.config['SECRET_KEY'] = 'h4sski'
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
# db = SQLAlchemy(app)
# db.init_app(app)


def main():

    app.register_blueprint(views, url_prefix='/')

    if not path.exists(f'/{DB_NAME}'):
        models.create_db_app(app)

    app.run(debug=True)


if __name__ == '__main__':
    main()
