from flask import Blueprint, render_template
from flask_login import login_required, current_user

from src.entities.room import Room

room_view = Blueprint('room_view', __name__, template_folder='templates')


@room_view.route('/room_list', methods=['GET', 'POST'])
@login_required
def room_list():
    rooms = Room.query.all()
    return render_template('room_list.html', is_logged=current_user.is_authenticated, rooms=rooms)
