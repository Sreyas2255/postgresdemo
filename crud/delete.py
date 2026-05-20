import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import get_db_connection   


def delete_user(user_id):
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "DELETE FROM users WHERE id = %s"
            cursor.execute(query, (user_id,))
            conn.commit()
            cursor.close()
            print(f"user with ID {user_id} deleted successfully")
        except Exception as e: 
            print(f"an error occurred: {e}")
        finally:
            conn.close()
delete_user(1)            