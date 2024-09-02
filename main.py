from flask import Flask, render_template, request, redirect, url_for, jsonify
from cryptography.fernet import Fernet

app = Flask(__name__)

# Route to render the form
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle form submission
@app.route('/submit', methods=['POST'])
def submit_form():
    # Check if the request is JSON
    if request.is_json:
        data = request.get_json()
        username = data['username']
        email = data['email']
    else:
        # Fallback to form-data if JSON is not used
        username = request.form['username']
        email = request.form['email']

    # Save the data to a file
    with open('user_data.txt', 'a') as file:
        file.write(f'Username: {username}, Email: {email}\n')

    return redirect(url_for('view_data'))

# Route to view data
@app.route('/view_data')
def view_data():
    with open('user_data.txt', 'r') as file:
        data = file.read().splitlines()

    return render_template('view_data.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Encrypt data
encrypted_data = cipher_suite.encrypt(b"Sensitive data")

# Decrypt data
decrypted_data = cipher_suite.decrypt(encrypted_data)