import psycopg2

def test_connection():
    try:
        conn = psycopg2.connect(
            database="assetmanagement",
            user="postgres",
            password="root2005417",
            host="localhost",
            port="5432"
        )
        print("Connection successful!")
        
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM USER")
        rows = cursor.fetchall()
        
        if len(rows) > 0:
            print("Data in the STUDENT1 table:")
            for row in rows:
                print(row)
        else:
            print("No data found in the STUDENT1 table.")
        
        cursor.close()
        conn.close()
    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")

test_connection()
