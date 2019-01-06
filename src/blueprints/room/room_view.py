from flask import Blueprint, render_template
from flask_login import login_required, current_user

from src.entities.room import Room

room_view = Blueprint('room_view', __name__, template_folder='templates')


@room_view.route('/room_list', methods=['GET', 'POST'])
def room_list():
    rooms = Room.query.all()
    user = current_user if current_user.is_authenticated else None
    return render_template('room_list.html', is_logged=current_user.is_authenticated,  user=user, rooms=rooms)
