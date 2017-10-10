import MySQLdb as mdb
import os

class Database:

    def __init__(self):
        self.con = con = mdb.connect(os.environ.get('MYSQL_HOST',
                'localhost'), os.environ.get('MYSQL_USER', 'root'),
                os.environ.get('MYSQL_PASSWORD', 'root'),
                os.environ.get('MYSQL_DB', 'mydb'))

    def create_table(self):
        CREATE_TABLE_QUERY = \
            'CREATE TABLE IF NOT EXISTS movies(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, name VARCHAR(40) NOT NULL, cover VARCHAR(150) NOT NULL)'
        cur = self.con.cursor()
        cur.execute(CREATE_TABLE_QUERY)

    def insert_movie(self, name, cover):
        cur = self.con.cursor()
        cur.execute('INSERT INTO movies(name, cover) VALUES(%s, %s)',
                    (name, cover))

    def fetch_one(self, name):
        cur = self.con.cursor()
        cur.execute("SELECT * FROM movies WHERE name LIKE %s", (name, ))
        return cur.fetchone()

    def fetch_movies(self):
        cur = self.con.cursor()
        cur.execute('SELECT * FROM movies')
        data = cur.fetchall()
        movies = []
        for entry in data:
            movie = {'id': entry[0], 'name': entry[1],
                     'cover': entry[2]}
            movies.append(movie)
        return movies

    def drop_table(self):
        DROP_TABLE_QUERY = 'DROP TABLE movies'
        cur = self.con.cursor()
        cur.execute(DROP_TABLE_QUERY)

    def close_conn(self):
        self.con.close()
