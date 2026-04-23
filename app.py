from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

app = Flask(__name__)

def connect():
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )
    return conn

def select_users():
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def get_user_by_id(user_id):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    result = cursor.fetchone()
    cursor.close()
    conn.close()
    return result

def insert_user(name, email, balance):
    conn = connect()
    cursor = conn.cursor()
    query = "INSERT INTO users (name, email, balance) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, email, balance))
    conn.commit()
    cursor.close()
    conn.close()

def update_user(user_id, balance):
    conn = connect()
    cursor = conn.cursor()
    query = "UPDATE users SET balance = %s WHERE id = %s"
    cursor.execute(query, (balance, user_id))
    conn.commit()
    cursor.close()
    conn.close()

def deposit_user(user_id, amount):
    conn = connect()
    cursor = conn.cursor()
    query = "UPDATE users SET balance = balance + %s WHERE id = %s"
    cursor.execute(query, (amount, user_id))
    conn.commit()
    cursor.close()
    conn.close()

def withdraw_user(user_id, amount):
    conn = connect()
    cursor = conn.cursor()
    query = "UPDATE users SET balance = balance - %s WHERE id = %s"
    cursor.execute(query, (amount, user_id))
    conn.commit()
    cursor.close()
    conn.close()

def delete_user(user_id):
    conn = connect()
    cursor = conn.cursor()
    query = "DELETE FROM users WHERE id = %s"
    cursor.execute(query, (user_id,))
    conn.commit()
    cursor.close()
    conn.close()

@app.route('/')
def index():
    users = select_users()
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        balance = request.form['balance']
        insert_user(name, email, float(balance))
        return redirect(url_for('index'))
    return render_template('add_user.html')

@app.route('/update_balance/<int:user_id>', methods=['GET', 'POST'])
def update_balance(user_id):
    if request.method == 'POST':
        balance = request.form['balance']
        update_user(user_id, float(balance))
        return redirect(url_for('index'))
    return render_template('update_balance.html', user_id=user_id)

@app.route('/deposit/<int:user_id>', methods=['GET', 'POST'])
def deposit(user_id):
    if request.method == 'POST':
        amount = float(request.form['amount'])
        deposit_user(user_id, amount)
        return redirect(url_for('index'))
    user = get_user_by_id(user_id)
    return render_template('deposit.html', user=user)

@app.route('/withdraw/<int:user_id>', methods=['GET', 'POST'])
def withdraw(user_id):
    user = get_user_by_id(user_id)
    error = None
    if request.method == 'POST':
        amount = float(request.form['amount'])
        if amount <= 0:
            error = 'Amount must be greater than 0.'
        elif amount > float(user[3]):
            error = 'Insufficient balance for withdrawal.'
        else:
            withdraw_user(user_id, amount)
            return redirect(url_for('index'))
    return render_template('withdraw.html', user=user, error=error)

@app.route('/delete_user/<int:user_id>')
def delete_user_route(user_id):
    delete_user(user_id)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
