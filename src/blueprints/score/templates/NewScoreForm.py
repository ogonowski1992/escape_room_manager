from datetime import datetime

from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField, DateField, IntegerField
from wtforms.validators import DataRequired, NumberRange


class NewScoreForm(FlaskForm):
    date = DateField('Data ucieczki', format='%d-%m-%Y', render_kw={"placeholder": "dd-mm-yyyy"},
                     default=datetime.now(), validators=[DataRequired()])
    room_id = SelectField('Pokój', validators=[DataRequired()])
    escape_time = IntegerField('Czas ucieczki [w minutach]', validators=[DataRequired(), NumberRange(min=1)])
    submit = SubmitField('Dodaj')
