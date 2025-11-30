from flask import Flask, render_template, request, redirect, url_for # request function
from flask_sqlalchemy import SQLAlchemy

# Create Flask application instance
app = Flask(__name__, template_folder='templates')

# Connect to db, = is path
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///GibJohn.db'

# Initialise db
db = SQLAlchemy(app)

# OOP table
class User(db.Model):
    user_id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(100), nullable = False)
    user_email = db.Column(db.String(100), nullable = False, unique = True)
    user_password = db.Column(db.String(100), nullable = False)
    user_type = db.Column(db.String(100), nullable = False)
    user_dob = db.Column(db.String(100), nullable = False)

    def __repr__(self):
        return f'<User {self.user_name}>'

with app.app_context():
    db.create_all()

# Create Homepage route
@app.route('/')
def homepage():
    return render_template('index.html')

# Create a Hompage route for dark mode
@app.route('/dark')
def homepage_dark():
    return render_template('index-dark.html')

# Create Login page route
@app.route('/login')
def login_page():
    return render_template('login.html')

# Create a Login page route for dark mode
@app.route('/login/dark')
def login_page_dark():
    return render_template('login-dark.html')

# Create Signup page route
@app.route('/signup', methods = ['GET', 'POST'])
def signup_page():
    # Create link to db
    if request.method == 'POST':
        user_name = request.form['user_name']
        user_email = request.form['user_email']
        user_password = request.form['user_password']
        user_type = request.form['user_type']
        user_dob = request.form['user_dob']

        new_user = User(
            user_name = user_name,
            user_email = user_email,
            user_password = user_password,
            user_type = user_type,
            user_dob = user_dob
        )

        try:
            db.session.add(new_user)
            db.session.commit() # saves to db
            return redirect(url_for('login_page'))
        except Exception as e:
            return f'An error occured: {e}'
    return render_template('signup.html')

# Create a Signup page route for dark mode
@app.route('/signup/dark')
def signup_page_dark():
    return render_template('signup-dark.html')

# Create Rewards page route
@app.route('/rewards')
def rewards_page():
    return render_template('rewards.html')

# Create Rewards page route for dark mode
@app.route('/rewards/dark')
def rewards_page_dark():
    return render_template('rewards-dark.html')

# Create Resources page route
@app.route('/resources')
def resources_page():
    return render_template('resources.html')

# Create Resources page route for dark mode
@app.route('/resources/dark')
def resources_page_dark():
    return render_template('resources-dark.html')

if __name__ == '__main__':
    app.run(debug=True)