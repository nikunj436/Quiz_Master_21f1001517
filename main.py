from flask import Flask
from flask import render_template
from flask import request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login/', methods=['POST','GET'])
def login():
    return render_template('login.html')

if __name__ == "__main__":

    app.run(host="0.0.0.0",port= 5000, debug=True)
