from flask import Blueprint
from flask_login import login_required

room_view = Blueprint('room_view', __name__, template_folder='templates')


@room_view.route('/room_list', methods=['GET', 'POST'])
@login_required
def room_list():
    pass
