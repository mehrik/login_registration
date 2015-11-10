from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector('login_register_db')

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/create_user', methods=['POST'])
def create():
	return render_template('/success.html')

app.run(debug=True)