from flask import Flask, render_template
import datetime
import random

app = Flask(__name__)

@app.route('/')
def home():
    status_list = ["SUCCESS", "RUNNING", "FAILED"]
    return render_template(
        'dashboard.html',
        status=random.choice(status_list),
        time=str(datetime.datetime.now())
    )
    
if __name__ == '__main__':
    app.run(port=5050)
