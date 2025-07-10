from sqlalchemy import create_engine, text
import os
# Setup engine once
db_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(
    db_connection_string,
    connect_args={"ssl":
                  {"ca": "ca.pem"}
                 }
)

# Function to load books
def load_books():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM books"))
        result_all = result.mappings().all()
        books = [dict(row) for row in result_all]
        return books

def add_email_to_email_list(email):
    with engine.connect() as conn:
        query = text("INSERT INTO email_list (email) VALUES (:Email)")
        conn.execute(query, {"Email": email})
        conn.commit()  # <-- This is needed


        