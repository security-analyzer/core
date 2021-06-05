import json
import mysql.connector

# Database config
database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="security_analyzer_db"
)


# Database utils
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


# Shared utils
def dict_to_json(dictionary):
    return json.dumps(dictionary, indent = 4)


def json_to_dict(json_object):
    return json.loads(json_object)


def contains_one_of(word, terms):
    for term in terms:
        if word in term:
            return True
    return False
