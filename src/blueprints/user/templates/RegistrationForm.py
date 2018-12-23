from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class RegistrationForm(FlaskForm):
    name = StringField('Imie')
    surname = StringField('Nazwisko')
    username = StringField('nazwa użytkownika', validators=[DataRequired()])
    password = PasswordField('hasło', validators=[DataRequired()])
    password2 = PasswordField('powtórz hasło', validators=[DataRequired()])
    submit = SubmitField('Rejestruj')
