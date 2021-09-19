from flask import render_template, url_for, flash, redirect, request
from tutoring_website import app, db, bcrypt
from tutoring_website.forms import RequestForm, RegisterForm, LoginForm
from tutoring_website.models import Request, Tutor, Student
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/admin", methods=['GET', 'POST'])
@login_required
def admin():
    if request.method == 'POST':
        if 'validate' in request.form:
            ids = request.form.get('selected_tutor')
            tutor_id, req_id = ids.split(', ')
            tutor = Tutor.query.get(tutor_id)
            req = Request.query.get(req_id)
            student = Student(email=req.email,
                              first_name=req.first_name, last_name=req.last_name)
            student.tutor = tutor
            db.session.delete(req)
            db.session.commit()

    requests = Request.query.all()

    return render_template('admin.html', requests=requests)


@app.route("/test", methods=['GET', 'POST'])
@login_required
def test():
    requests = Request.query.all()
    tutor = Tutor.query.get(int(current_user.id))
    pending_requests = []
    accepted_requests = []

    if request.method == 'POST':
        if 'select' in request.form:
            for req_id in request.form.getlist('selected_requests'):
                req = Request.query.get(int(req_id))
                tutor.requests.append(req)
                db.session.commit()
        elif 'delete' in request.form:
            for req_id in request.form.getlist('selected_requests'):
                req = Request.query.get(int(req_id))
                tutor.requests.remove(req)
                db.session.commit()

    for accept_requests in tutor.requests:
        accepted_requests.append(accept_requests)

    for pending_request in requests:
        if pending_request not in accepted_requests:
            pending_requests.append(pending_request)

    return render_template('test.html', pending_requests=pending_requests, accepted_requests=accepted_requests)


@app.route("/tutors", methods=['GET', 'POST'])
@login_required
def tutor_view():
    tutors = Tutor.query.all()
    selected_tutor = None

    if request.method == 'POST':
        # TODO(ajeej): Find way to prevent page refresh after POST method
        if 'selected_tutor' in request.form:
            tutor_id = request.form.get('selected_tutor')
            selected_tutor = Tutor.query.get(tutor_id)

    return render_template('tutors.html', tutors=tutors, selected_tutor=selected_tutor)


@ app.route("/", methods=['GET', 'POST'])
def request_tutor():
    form = RequestForm()
    if form.validate_on_submit():
        request = Request(email=form.email.data,
                          first_name=form.first_name.data,
                          last_name=form.last_name.data)
        db.session.add(request)
        db.session.commit()
        return redirect(url_for('test'))

    return render_template('request.html', form=form)


@ app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('test'))

    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        tutor = Tutor(first_name=form.first_name.data,
                      last_name=form.last_name.data,
                      email=form.email.data,
                      username=form.username.data,
                      password=hashed_password)
        if tutor.username == 'admin' and tutor.email == 'admin@gmail.com':
            tutor.is_admin = True
        db.session.add(tutor)
        db.session.commit()
        flash('Your account has been created! You\'re now able to log in', 'success')
        return redirect(url_for('login'))

    return render_template('register.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('test'))

    form = LoginForm()
    if form.validate_on_submit():
        tutor = Tutor.query.filter_by(email=form.email.data).first()
        if tutor and bcrypt.check_password_hash(tutor.password, form.password.data):
            login_user(tutor, remember=form.remember_me.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('test'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')

    return render_template('login.html', form=form)


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('request_tutor'))
