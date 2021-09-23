from tutoring_website import db, login_manager
from flask_login import UserMixin

tutor_request_association_table = db.Table('association',
                                           db.Column('tutor_id', db.ForeignKey(
                                               'tutor.id'), primary_key=True),
                                           db.Column('request_id', db.ForeignKey(
                                               'request.id'), primary_key=True)
                                           )


@login_manager.user_loader
def load_user(user_id):
    return Tutor.query.get(int(user_id))


class Tutor(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    profile_pic = db.Column(db.String(20), nullable=False,
                            default='default.jpg')
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    students = db.relationship("Student", backref="tutor", lazy=True)
    requests = db.relationship("Request",
                               secondary=tutor_request_association_table,
                               backref=db.backref('tutors', lazy='dynamic'))

    def __repr__(self):
        return f"Tutor('{self.username}', '{self.email}', '{self.first_name}', '{self.last_name}')"


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tutor_id = db.Column(db.Integer, db.ForeignKey('tutor.id'))
    email = db.Column(db.String(120), nullable=False)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)

    def __repr__(self):
        return f"Student('{self.email}', '{self.first_name}', '{self.last_name}')"


class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    first_name = db.Column(db.String(25), nullable=False)
    last_name = db.Column(db.String(25), nullable=False)
    date = db.Column(db.String(10), nullable=False)
    time = db.Column(db.String(5), nullable=False)

    def __repr__(self):
        return f"Request('{self.email}', '{self.first_name}', '{self.last_name}')"
