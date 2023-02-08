import os
from flask import Flask
import mysql.connector
import uuid
import os
import json

class DBManager:
    def __init__(self):
        db_type = os.environ.get('DB_TYPE')
        password_file = os.environ.get('MY_SQL_PASSWORD_FILE','/run/secrets/db-password')
        pf = open(password_file, 'r')
        password = None

        if db_type == 'rds':
            credentials = json.load(pf)
            password = credentials["password"]
        else:
            password = pf.read()

        database = os.environ.get('MY_SQL_DATABASE','example')
        host = os.environ.get('MY_SQL_HOST',"db")
        user = os.environ.get('MY_SQL_USER',"root")
        self.connection = mysql.connector.connect(
            user=user, 
            password=password,
            host=host, # name of the mysql service as set in the docker-compose file
            database=database,
            auth_plugin='mysql_native_password'
        )
        pf.close()
        self.cursor = self.connection.cursor()
    
    def populate_db(self):

        self.cursor.execute('DROP TABLE IF EXISTS blog')
        self.cursor.execute('CREATE TABLE blog (id INT NOT NULL AUTO_INCREMENT PRIMARY KEY, title VARCHAR(256))')
        self.cursor.execute("insert into blog values(NULL,'initial load')")
        
        self.connection.commit()

    def insert_records(self,id,name):
        data = (id,str(name))
        query = (
                "INSERT INTO blog(id,title)"
                "VALUES (%s, %s)"
                )
        self.cursor.execute(query,data)
        self.connection.commit()
    
    def query_titles(self):
        self.cursor.execute('SELECT title FROM blog')
        rec = []
        for c in self.cursor:
            rec.append(c[0])
        return rec


server = Flask(__name__)
conn = None

@server.route('/')
def listName():
    global conn
    if not conn:
        conn = DBManager()
        conn.populate_db()
        #conn.insert_records()
    rec = conn.query_titles()

    response = ''
    for c in rec:
        response = response  + '<div>   ' + c + '</div>'
    return response

@server.route('/add/<id>/<name>')
def addName(id,name):
    global conn
    if not conn:
        conn = DBManager(password_file='/run/secrets/db-password')
    conn.insert_records(id,name)
    rec = conn.query_titles()

    response = ''
    for c in rec:
        response = response  + '<div>   ' + c + '</div>'
    return response

if __name__ == '__main__':
    server.run()
