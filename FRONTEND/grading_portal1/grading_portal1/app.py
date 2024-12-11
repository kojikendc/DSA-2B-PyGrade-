from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "your_secret_key"

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'  # Ensure MySQL listens on all IPs or update to specific server IP
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Jayben26@'
app.config['MYSQL_DB'] = 'grades'

# Initialize MySQL
mysql = MySQL(app)

# Utility function to check credentials
def check_credentials(username, password):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT role FROM users WHERE username = %s AND password = %s", (username, password))
    result = cursor.fetchone()  # Fetch the result (should be a tuple)
    cursor.close()
    if result:
        return result[0]  # Return role (admin or student)
    return None

@app.route('/')
def login():
    """Render the login page."""
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login_user():
    """Handle user login."""
    username = request.form['username']
    password = request.form['password']
    
    # Validate credentials
    role = check_credentials(username, password)
    if role:
        session['username'] = username
        session['role'] = role
        return redirect(url_for('admin_dashboard' if role == 'admin' else 'student_dashboard'))
    
    return render_template('login.html', error_message="Invalid username or password")

@app.route('/admin_dashboard')
def admin_dashboard():
    """Admin dashboard."""
    if 'username' not in session or session.get('role') != 'admin':
        flash("Unauthorized access. Please log in.", 'error')
        return redirect(url_for('login'))
    return render_template('admin_dashboard.html', username=session['username'])

@app.route('/student_dashboard')
def student_dashboard():
    """Student dashboard."""
    if 'username' not in session or session.get('role') != 'student':
        flash("Unauthorized access. Please log in.", 'error')
        return redirect(url_for('login'))
    return render_template('student_dashboard.html', username=session['username'])

@app.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    """Handle forgotten password."""
    if request.method == 'POST':
        email = request.form['email']
        
        # Query the database for the user by email
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT username FROM users WHERE email = %s", [email])
        user = cursor.fetchone()

        if user:
            flash(f"Recovery instructions have been sent to {email}.", 'success')
            # Logic to send an email would go here
        else:
            flash("Email not found. Please try again.", 'error')
        
        cursor.close()
        return redirect(url_for('forgot_password'))
    
    return render_template('forgot_password.html')

@app.route('/logout', methods=['POST'])
def logout():
    """Handle user logout."""
    session.clear()
    flash("You have been logged out.", 'info')
    return redirect(url_for('login'))

if __name__ == '__main__':
    # Host the Flask app on all available interfaces and set a port (e.g., 5000)
    app.run(host='0.0.0.0', port=5000, debug=True)

