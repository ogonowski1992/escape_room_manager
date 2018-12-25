from datetime import datetime

from flask import Blueprint, render_template, request, url_for, redirect
from flask_login import login_required, current_user
from sqlalchemy import desc

from src.Utils import add_error
from src.blueprints.score.templates.NewScoreForm import NewScoreForm
from src.database import db_session
from src.entities.room import Room
from src.entities.user import User
from src.entities.visited_rooms import VisitedRooms

score_view = Blueprint('score_view', __name__, template_folder='templates')


@score_view.route('/add_score', methods=['GET', 'POST'])
@login_required
def add_score():
    form = NewScoreForm()
    rooms = Room.query.all()
    form.room_id.choices = [(str(r.id), r.room_name) for r in rooms]
    if request.method == 'POST':
        if form.validate_on_submit():
            visited_room = VisitedRooms(form.room_id.data, current_user.id, form.date.data, form.escape_time.data)
            db_session.add(visited_room)
            db_session.commit()
            return redirect(url_for('score_view.score_list'))
        else:
            if 'date' in form.errors:
                add_error(form.date, 'Zły format daty.')
            elif 'escape_time' in form.errors:
                add_error(form.escape_time, 'Zły format czasu ucieczki.')
    return render_template('add_score.html', is_logged=current_user.is_authenticated, form=form)


@score_view.route('/score_list', methods=['GET', 'POST'])
@login_required
def score_list():
    # userList = users.query.join(friendships, users.id == friendships.user_id).add_columns(users.userId, users.name,
    #                                                                                       users.email, friends.userId,
    #                                                                                       friendId).filter(
    #     users.id == friendships.friend_id).filter(friendships.user_id == userID).paginate(page, 1, False)
    ranking = VisitedRooms.query.join(Room).join(User).add_columns(Room.room_name, VisitedRooms.escape_time, User.name,
                                                                   User.surname).order_by(VisitedRooms.room_id.desc(),
                                                                                          VisitedRooms.escape_time.asc()).all()

    return render_template('score_list.html', is_logged=current_user.is_authenticated, ranking=ranking)
