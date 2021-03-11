import mysql.connector

# Database config
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="security_analyzer_db"
)


# Helpers
def fetch_all(query):
    query_cursor = database.cursor()
    query_cursor.execute(query)
    items = query_cursor.fetchall()
    return items


def fetch_one(query):
    query_cursor = database.cursor()
    query_cursor.execute(query)
    item = query_cursor.fetchone()
    return item


def commit_query(query):
    query_cursor = database.cursor()
    query_cursor.execute(query)
    database.commit()
