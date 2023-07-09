from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def login(username, password):
    """
    Checks if the username and password match a credential in the credentials.csv file.

    Args:
        username: The username to check.
        password: The password to check.

    Returns:
        True if the username and password match, False otherwise.
    """
    with open('credentials.csv', 'r') as f:
        credentials = [line.strip().split(',') for line in f]
        for credential in credentials:
            if credential[0] == username and credential[1] == password:
                return True
    return False

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/', methods=['POST'])
def login_post():
    username = request.form['username']
    password = request.form['password']
    if login(username, password):
        session['username'] = username  # Store the username in the session
        return redirect('/settings')
    else:
        error_message = 'Invalid username or password'
        return render_template('login.html', error_message=error_message)

@app.route('/settings')
def settings_page():
    if 'username' in session:
        username = session['username']  # Retrieve the username from the session
        return render_template('settings.html', username=username)
    else:
        return redirect('/')

if __name__ == '__main__':
    app.run()
