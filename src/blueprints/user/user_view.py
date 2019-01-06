from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import current_user, login_user, logout_user

from src.Utils import add_error
from src.blueprints.user.templates.LoginForm import LoginForm
from src.blueprints.user.templates.RegistrationForm import RegistrationForm
from src.dao import user_dao

user_view = Blueprint('user_view', __name__, template_folder='templates')


@user_view.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    # if current_user.is_authenticated:
    #     return redirect(url_for('user_view.index'))
    # if request.method == 'POST':
    #     if request.form['username'] is not None and request.form['password'] is not None:
    #         user = user_dao.login(request.form['username'], request.form['password'])
    #         if user is None:
    #             flash('Invalid username or password')
    #             return redirect(url_for('login'))
    #         login_user(user, remember=False)
    #         return redirect(url_for('user_view.index'))
    # return render_template('login.html', title='Sign In')
    if current_user.is_authenticated:
        return redirect(url_for('user_view.index'))
    if request.method == 'POST':
        if form.validate_on_submit():
            user = user_dao.login(form.username.data, form.password.data)
            if user is None:
                form.username.errors.append("Niepoprawna nazwa użytkownika i/lub hasło")
                return render_template('login.html', form=form)
            login_user(user, remember=False)
            return redirect(url_for('user_view.index'))
    return render_template('login.html', title='Sign In', form=form)


@user_view.route('/', methods=['GET', 'POST'])
@user_view.route('/index', methods=['GET', 'POST'])
def index():
    user = current_user if current_user.is_authenticated else None
    return render_template('index.html', is_logged=current_user.is_authenticated, user=user)

@user_view.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('user_view.login'))


@user_view.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if form.password.data != form.password2.data:
                add_error(form.password, 'Podane hasła różnia się od siebie.')
                return render_template('registration.html', form=form)
            elif user_dao.check_if_username_exist(form.username.data):
                add_error(form.username, 'Podana nazwa użytkownika jest już używana')
                return render_template('registration.html', form=form)
            else:
                user = user_dao.registration(form.username.data, form.password.data, form.name.data,
                                             form.surname.data)
                login_user(user, remember=False)
                return render_template('index.html', is_logged=current_user.is_authenticated)
    else:
        return render_template('registration.html', form=form)

