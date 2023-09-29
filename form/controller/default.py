from form import app, db
from flask import render_template, redirect, url_for, request

from form.model.registerforms import RegisterForm
from form.model.tables import Register


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


@app.route('/login')
def login():
    return render_template('auth/login.html')


@app.route('/tableDB')
def data_table():

    participants = db.session.query(Register).all()

    return render_template('storage/table.html', participants=participants)
