from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('dashboard.html',
                           status="SUCCESS",
                           time=str(datetime.datetime.now()))

if __name__ == '__main__':
    app.run(port=5050)
