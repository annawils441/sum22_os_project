from flask import Flask, render_template

# Create Flask application instance
app = Flask(__name__, template_folder='templates')

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
@app.route('/signup')
def signup_page():
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