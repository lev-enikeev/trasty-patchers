import sqlite3

sqlite_connection = sqlite3.connect("bd.db")
cursor = sqlite_connection.cursor()

def create_user(username, seller):
    query = f"""INSERT INTO users (user_name, seller) VALUES ('{username}', {seller});"""
    cursor.execute(query)
    sqlite_connection.commit()

def get_games_list():
    query = 'SELECT description FROM games'
    values = cursor.execute(query).fetchall()
    return [i[0] for i in values]
