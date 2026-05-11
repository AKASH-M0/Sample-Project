from flask import Flask, render_template, request, redirect, session
import datetime
import random

app = Flask(_name_)
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
            return render_template(
                'login.html',
                error="Invalid Credentials"
            )

    return render_template('login.html')


# Dashboard Route
@app.route('/dashboard')
def dashboard():

    # Check login session
    if 'user' not in session:
        return redirect('/')

    # Simulate pipeline status
    status = "SUCCESS"

    # Simulate build statistics
    total_builds = 50
    successful_builds = 49

    # Calculate failed builds
    failed_builds = total_builds - successful_builds

    # Calculate success rate
    success_rate = round(
        (successful_builds / total_builds) * 100,
        2
    )

    # Current build time
    build_time = str(datetime.datetime.now())

    # Simulate pipeline stage execution times
    pipeline_data = [
        random.randint(5, 15),   # Build time
        random.randint(3, 10),   # Test time
        random.randint(4, 12)    # Deploy time
    ]

    return render_template(
        'dashboard.html',
        status=status,
        time=build_time,
        data=pipeline_data,
        success_rate=success_rate,
        total_builds=total_builds,
        successful_builds=successful_builds,
        failed_builds=failed_builds
    )


# Logout Route
@app.route('/logout')
def logout():

    session.pop('user', None)
    return redirect('/')


# Run App
if _name_ == '_main_':
    app.run(
        host='0.0.0.0',
        port=5050,
        debug=True
    )
