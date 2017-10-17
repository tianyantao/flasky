#coding:utf-8
from flask import Flask
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('apply_test_dev.html')


if __name__ == '__main__':
    app.run(debug=True)