from flask import Blueprint, request, session, render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required

from src.dao import user_dao

user_view = Blueprint('user_view', __name__, template_folder='templates')


@user_view.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('user_view.index'))
    if request.method == 'POST':
        if request.form['username'] is not None and request.form['password'] is not None:
            user = user_dao.login(request.form['username'], request.form['password'])
            if user is None:
                flash('Invalid username or password')
                return redirect(url_for('login'))
            login_user(user, remember=False)
            return redirect(url_for('user_view.index'))
    return render_template('login.html', title='Sign In')


@user_view.route('/', methods=['GET', 'POST'])
@user_view.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html', is_logged=current_user.is_authenticated)


@user_view.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('user_view.login'))


@user_view.route('/registration', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('home'))
    else:
        return render_template('registration.html')
