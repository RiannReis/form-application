from form import app, db
from flask import render_template, redirect, url_for, request

from form.model.registerforms import RegisterForm
from form.model.loginform import TokenAuth
from form.model.tables import Register

from form import helper

@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit:
            name = request.form.get('name')
            email = request.form.get('email')
            age = request.form.get('age')
            number = request.form.get('number')
            occupation = request.form.get('occupation')

            data = Register(name=name, email=email, occupation=occupation, age=age, number=number)

            db.session.add(data)
            db.session.commit()

            return redirect(url_for('success'))
    return render_template('auth/index.html', form=form)
    

@app.route('/success')
def success():
    return render_template('results/success.html')


@app.route('/auth', methods=['GET'])
def authenticate():
    return helper.auth()


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = TokenAuth()
    if request.method == 'POST':
        token = request.form.get('token')
        
        return redirect(url_for('data_table', token=token))
    return render_template('auth/login.html', form=form)


@app.route('/tableDB')
@helper.token_required
def data_table(data):

    participants = db.session.query(Register).all()

    return render_template('storage/table.html', participants=participants)


@app.route('/delete')
def clean_table():
    db.session.query(Register).delete()
    db.session.commit()
    return 'OK'