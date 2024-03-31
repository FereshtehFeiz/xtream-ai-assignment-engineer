# app.py
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/model', methods = ['GET','POST'])
def model():
    return "Method used:%s" % request.method

@app.route('/')
def home():
    return render_template("base.html")

@app.route('/cloud')
def cloud():
    return render_template("Architecture.html")


if __name__ == '__main__':
    app.run()
