# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def home():
    # Your prediction logic goes here
    # return jsonify({'result': 'prediction_result'})
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True)
