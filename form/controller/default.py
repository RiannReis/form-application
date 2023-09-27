from form import app
from flask import render_template, redirect, url_for, request

from form.model.registerforms import RegisterForm


@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit:
            print(form.name.data)
            print(form.email.data)
            print(form.phone_number.data)
            print(form.age.data)
            print(form.occupation.data)
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
    return render_template('storage/table.html')
