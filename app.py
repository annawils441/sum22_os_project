from flask import Flask, render_template

# Create Flask application instance
app = Flask(__name__, template_folder='templates')

# Create Homepage route
@app.route('/')
def homepage():
    return render_template('index.html')

# Create Login page route
@app.route('/login')
def login_page():
    return render_template('login.html')

# Create Signup page route
@app.route('/signup')
def signup_page():
    return render_template('signup.html')

# Create Rewards page route
@app.route('/rewards')
def rewards_page():
    return render_template('rewards.html')

# Create Resources page route
@app.route('/resources')
def resources_page():
    return render_template('resources.html')

if __name__ == '__main__':
    app.run(debug=True)