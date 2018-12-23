from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('nazwa użytkownika', validators=[DataRequired()])
    password = PasswordField('hasło', validators=[DataRequired()])
    submit = SubmitField('Zaloguj')
