from flask import Flask, render_template, request, redirect, session
import datetime
import random

app = Flask(__name__)
app.secret_key = "devops_secret_key"

# Dummy login credentials
USERNAME = "admin"
PASSWORD = "admin"

# Login Route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']

        if user == USERNAME and pwd == PASSWORD:
            session['user'] = user
            return redirect('/dashboard')
        else:
            return render_template('login.html', error="Invalid Credentials")

    return render_template('login.html')


# Dashboard Route
@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/')

    # Simulate pipeline status
    status = "SUCCESS"

    # Simulate pipeline metrics
    build_time = str(datetime.datetime.now())
    pipeline_data = [random.randint(5, 15), random.randint(3, 10), random.randint(4, 12)]

    return render_template(
        'dashboard.html',
        status=status,
        time=build_time,
        data=pipeline_data
    )


# Logout Route
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/')


# Run App
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)
