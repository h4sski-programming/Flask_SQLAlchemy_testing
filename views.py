from flask import Blueprint

from models import User, Activity
from models import session, db, engine

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


@views.route('/activity/add/<user_id>/<distance>')
def create_activity(user_id, distance):
    activity = Activity(user_id=user_id, distance=distance)
    session.add(activity)
    session.commit()
    s = f'<h1>Added activity</h1><p>{activity.user_id}</br>{activity.distance}</p>'
    return s


@views.route('/activity/show/<activity_id>')
def show_activity(activity_id):
    activity = session.query(Activity).filter_by(id=activity_id).first()
    s = f'<h1>Showing activity</h1><p>Activity ID = {activity.id}<br/>\
        User id = {activity.user_id}<br/>Distance = {activity.distance}</p>'
    return s


@views.route('/activity/show_all/<user_id>')
def show_activity_all(user_id):
    user = session.query(User).filter_by(id=user_id).first()
    activity = session.query(Activity).filter_by(user_id=user.id).all()
    s = f'<h1>Showing all activities of user {user.name}</h1>'
    for a in activity:
        s = s + f'<p>{a.id} | {a.distance}</p>'
    return s


@views.route('/activity/show_all_user/<user_id>')
def show_activity_all_from_user(user_id):
    # user = User.query.filter_by(id=user_id).first()   ''' Not working '''
    # user = session.query(User).filter_by(id=user_id).first()

    user = session.query(User).all()
    print(type(user))
    s = ''
    for r in user:
        t = f'<p>{r.id} | {r.name} | {r.role} | {r.date}</p>'
        s = s + t
    # s = f'<h1>Showing all activities of user {user.name}</h1>'
    # for a in user.activity:
    #     s = s + f'<p>{a.id} | {a.distance}</p>'
    return s
