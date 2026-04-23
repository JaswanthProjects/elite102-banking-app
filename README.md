# Banking App

A simple Flask web application for basic banking operations with MySQL database integration. Manage user accounts, deposit, withdraw, and track balances all from a web interface.

## Features

- ✅ View all users and their current balances
- ✅ Create new user accounts
- ✅ Deposit money to accounts
- ✅ Withdraw money from accounts (with balance validation)
- ✅ Update account balances directly
- ✅ Delete user accounts
- ✅ Unit tests for all database operations

## Prerequisites

- Python 3.6+
- MySQL Server 5.7+
- pip

## Installation & Setup

### 1. Clone or Download the Project
```bash
cd elite102project
```

### 2. Install MySQL Server
- Download from https://dev.mysql.com/downloads/mysql/
- Install and start the MySQL service

### 3. Create the Database
Open a terminal and run:
```bash
mysql -u root -p < schema.sql
```
Enter your MySQL root password when prompted. This creates the `elite102` database and `users`/`transactions` tables.

### 4. Configure Database Credentials
Edit `config.py` and update your MySQL credentials:
```python
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = 'your_mysql_password'  # Update this
DB_NAME = 'elite102'
```

### 5. Install Python Dependencies
```bash
pip install -r requirements.txt
```

This installs Flask and mysql-connector-python.

## Running the Application

```bash
python app.py
```

Open your browser and navigate to:
```
http://localhost:5000
```

You should see the Banking App homepage with a list of users (if any exist).

## Using the App

### Add a New User
1. Click "Add New User"
2. Enter name, email, and starting balance
3. Click "Add User"

### Deposit Money
1. Click "Deposit" next to a user
2. Enter the deposit amount
3. Click "Deposit" - the account balance will increase

### Withdraw Money
1. Click "Withdraw" next to a user
2. Enter the withdrawal amount
3. If balance is sufficient, click "Withdraw" - the account balance will decrease
4. If withdrawal exceeds balance, an error message appears

### Set Balance Directly
1. Click "Set Balance" next to a user
2. Enter the new balance
3. Click "Update Balance"

### Delete a User
1. Click "Delete" next to a user
2. Confirm the deletion

## Testing

Run the unit tests to verify all database operations:
```bash
python test_app.py
```

Tests include:
- Database connection
- SELECT queries
- INSERT operations
- Deposit and withdrawal operations

## Project Structure

```
elite102project/
├── app.py                 # Flask web application with all routes
├── config.py              # Database connection configuration
├── schema.sql             # MySQL database schema (users & transactions tables)
├── requirements.txt       # Python dependencies
├── test_app.py            # Unit tests for database operations
├── README.md              # This file
└── templates/             # HTML templates
    ├── index.html         # Dashboard showing all users
    ├── add_user.html      # Form to add new user
    ├── deposit.html       # Form for deposit operations
    ├── withdraw.html      # Form for withdrawal operations
    └── update_balance.html # Form to set balance directly
```

## Database Schema

### Users Table
```sql
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    balance DECIMAL(10, 2)
);
```

### Transactions Table
```sql
CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    amount DECIMAL(10, 2),
    type VARCHAR(20),
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

## Checking Database Data

### Via MySQL Workbench
- Connect to your MySQL server
- Select the `elite102` database
- Right-click on `users` table → "Select Rows"

### Via Command Line
```bash
mysql -u root -p
USE elite102;
SELECT * FROM users;
SELECT * FROM transactions;
EXIT;
```

### Via Flask App
- Open http://localhost:5000 to view all users and balances in real-time

## Troubleshooting

**Error: "Access denied for user 'root'@'localhost'"**
- Update the password in `config.py` to match your MySQL root password

**Error: "database elite102 doesn't exist"**
- Run `mysql -u root -p < schema.sql` to create the database

**Port 5000 already in use**
- Edit `app.py` and change `app.run(debug=True)` to `app.run(debug=True, port=5001)`

## Technologies Used

- **Backend**: Python, Flask
- **Database**: MySQL
- **Frontend**: HTML, CSS (inline styling)
- **Testing**: Python unittest

## License

This project is open source and available under the MIT License.