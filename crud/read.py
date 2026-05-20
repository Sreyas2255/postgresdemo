import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import get_db_connection   

def get_user(user_id):
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT id, name FROM users WHERE id = %s"
            cursor.execute(query, (user_id,))
            user = cursor.fetchone()
            cursor.close()
            if user:
                print(f"user found: ID={user[0]}, Name={user[1]}")
            else:
                print("user not found")
        except Exception as e: 
            print(f"an error occurred: {e}")
        finally:
            cursor.close()
            conn.close()
get_user(1)            
