from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask.ext.bcrypt import Bcrypt
import re
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector('login_register_db')
app.secret_key = 'maricIsTired'
NAME_REGEX = re.compile(r'^[a-zA-z]{2,}$')
EMAIL_REGEX = re.compile(r'^[a-za-z0-9\.\+_-]+@[a-za-z0-9\._-]+\.[a-za-z]*$')


@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/create_user', methods=['POST'])
def create():
	first_name = request.form['first_name']
	last_name = request.form['last_name']
	email = request.form['email']
	password = request.form['password']
	if password:
		pw_hash = bcrypt.generate_password_hash(password)
	error = False

	if not email or not first_name or not last_name or not password:
		flash('1 or more of the required fields have not been completed')
		error = True
	if not NAME_REGEX.match(first_name) or not NAME_REGEX.match(last_name):
		flash('Name fields must contain at least 2 characters and cannot contain any numbers or special characters')
		error = True
	if not EMAIL_REGEX.match(email) and email:
		flash('Invalid email')
		error = True
	if len(password) < 8:
		flash('Password field must contain at least 8 characters')
		error = True
	if password != request.form['confirm']:
		flash('Passwords must match')
		error = True
	if error == True:
		return redirect('/')
	
	insertInto = "INSERT INTO users (first_name, last_name, email, pw_hash, created_at) VALUES ('{}', '{}', '{}', '{}', NOW())"
	query = insertInto.format(first_name, last_name, email, pw_hash)
	mysql.run_mysql_query(query)
	return render_template('/success.html', youremail=email, first_name=first_name, last_name=last_name, page='register')

@app.route('/sign_in', methods=['POST'])
def sign_in():
	return render_template('/success.html', page='login')

app.run(debug=True)