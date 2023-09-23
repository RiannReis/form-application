from form import app
from flask import render_template, redirect, url_for, request, abort


@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if request.form['name'] == 'test' and request.form['email'] =='test@gmail.com':
            return redirect(url_for('success'))    
    return render_template('auth/index.html')
    


@app.route('/success')
def success():
    return render_template('results/success.html')