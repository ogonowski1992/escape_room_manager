from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class RegistrationForm(FlaskForm):
    name = StringField('Imię')
    surname = StringField('Nazwisko')
    username = StringField('Nazwa użytkownika', validators=[DataRequired()])
    password = PasswordField('Hasło', validators=[DataRequired()])
    password2 = PasswordField('Powtórz hasło', validators=[DataRequired()])
    submit = SubmitField('Rejestruj')
