from flask import Blueprint, render_template
from flask_login import login_required

score_view = Blueprint('score_view', __name__, template_folder='templates')


@score_view.route('/add_score', methods=['GET', 'POST'])
@login_required
def add_score():
    return render_template('add_score.html')


@score_view.route('/score_list', methods=['GET', 'POST'])
@login_required
def score_list():
    pass
