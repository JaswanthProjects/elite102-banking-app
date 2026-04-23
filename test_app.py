import unittest
from app import connect, select_users, insert_user, update_user, delete_user, get_user_by_id, deposit_user, withdraw_user

class TestBankingApp(unittest.TestCase):

    def test_database_connection(self):
        """Test if we can connect to the database"""
        conn = connect()
        self.assertIsNotNone(conn)
        conn.close()

    def test_select_users(self):
        """Test selecting users from database"""
        users = select_users()
        self.assertIsInstance(users, list)

    def test_insert_user(self):
        """Test inserting a user"""
        # Insert a test user
        insert_user("Test User", "test@example.com", 500.00)

        # Check if user was inserted
        users = select_users()
        test_user = next((user for user in users if user[1] == "Test User"), None)
        self.assertIsNotNone(test_user)

        # Clean up - delete the test user
        if test_user:
            delete_user(test_user[0])

    def test_deposit_withdraw(self):
        """Test deposit and withdrawal operations"""
        insert_user("Test Bank", "bank@example.com", 100.00)
        users = select_users()
        test_user = next((user for user in users if user[1] == "Test Bank"), None)
        self.assertIsNotNone(test_user)

        user_id = test_user[0]
        deposit_user(user_id, 50.00)
        user_after_deposit = get_user_by_id(user_id)
        self.assertEqual(float(user_after_deposit[3]), 150.00)

        withdraw_user(user_id, 25.00)
        user_after_withdraw = get_user_by_id(user_id)
        self.assertEqual(float(user_after_withdraw[3]), 125.00)

        delete_user(user_id)

if __name__ == '__main__':
    unittest.main()