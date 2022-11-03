from flask import Blueprint

from models import User
from models import db, session

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return f'<h1>Hello from home</h1>'


@views.route('/<name>/')
def show(name):
    user = session.query(User).filter_by(name=name).first()
    return f'<h1>{user.name} with role {user.role}. Created at {user.date}</h1>'


@views.route('/id/<user_id>/')
def by_id(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    return f'<h1>{user.name} with role {user.role}. Created at {user.date}</h1>'

@views.route('/update/<user_id>/<n>/<r>')
def update(user_id, n, r):
    user = session.query(User).filter_by(id=user_id).first()
    user.name = n
    user.role = r
    return f'<h1>{user.name} with role {user.role}</h1>'


@views.route('/<n>/<r>')
def create(n, r):
    user = User(name=n, role=r)
    session.add(user)
    session.commit()
    print(f'{user.id}\t{user.name}\t{user.role}\t{user.date}')
    return f'<h1>Added user {user.name} with role {user.role}</h1>'
