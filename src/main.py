# coding=utf-8

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_cors import CORS
from flask_login import LoginManager

from src.blueprints.room import room_view
from src.blueprints.score import score_view
from src.blueprints.user import user_view
from src.database import init_db, db_session
from src.entities.room import Room
from src.entities.user import User

app = Flask(__name__)
login = LoginManager(app)
login.login_view = 'user_view.login'
bootstrap = Bootstrap(app)
# dodac @login_required nad elementami wymagajacymi autoryzacji
# https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins       Introduction to Flask-Login

app.register_blueprint(user_view.user_view)
app.register_blueprint(score_view.score_view)
app.register_blueprint(room_view.room_view)
app.secret_key = b'akfsd(){;[/.32jide9q0IE@#$%^&*(/'

CORS(app)
init_db()


#
# u = User('ala', '123', 'Ala', 'alowksa')
# r = Room('ala', '123', 'Ala', 'alowksa')
# db_session.add(r)
# db_session.commit()


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/exams')
def get_exams():
    pass
    # # fetching from the database
    # session = Session()
    # exam_objects = session.query(Exam).all()
    #
    # # transforming into JSON-serializable objects
    # schema = ExamSchema(many=True)
    # exams = schema.dump(exam_objects)
    #
    # # serializing as JSON
    # session.close()
    # return jsonify(exams.data)


@app.route('/exams', methods=['POST'])
def add_exam():
    pass
    # # mount exam object
    # posted_exam = ExamSchema(only=('title', 'description'))\
    #     .load(request.get_json())
    #
    # exam = Exam(**posted_exam.data, created_by="HTTP post request")
    #
    # # persist exam
    # session = Session()
    # session.add(exam)
    # session.commit()
    #
    # # return created exam
    # new_exam = ExamSchema().dump(exam).data
    # session.close()
    # return jsonify(new_exam), 201
