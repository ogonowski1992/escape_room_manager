from src.entities.user import User


def login(username, password):
    user = User.query.filter(User.username == username and User.password == password).first()
    return user

