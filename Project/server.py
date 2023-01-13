from flask import Flask, request, redirect, render_template

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # check if user exists and password is correct
    if check_user_credentials(username, password):
        return redirect('/dashboard')
    else:
        return redirect('/')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

def check_user_credentials(username, password):
    return username == 'admin' and password == 'password'

if __name__ == '__main__':
    app.run(debug=True)
