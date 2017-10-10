import unittest

from app import app
from database import Database

class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = Database()
        self.db.create_table()

    def tearDown(self):
        self.db.drop_table()
        self.db.close_conn()

    def test_create_movie(self):
        expectedName = 'Minions'
        expectedCover = 'https://image.tmdb.org/t/p/w185_and_h278_bestv2/q0R4crx2SehcEEQEkYObktdeFy.jpg'
        self.db.insert_movie(expectedName, expectedCover)
        result = self.db.fetch_one(expectedName)
        assert result[1] == expectedName
        assert result[2] == expectedCover

    def test_fetch_movies(self):
        movies = []
        movies.append({
            'id' : 1,
            'name' : 'Spider-Man: Homecoming',
            'cover' : 'https://image.tmdb.org/t/p/w185_and_h278_bestv2/c24sv2weTHPsmDa7jEMN0m2P3RT.jpg'
        })
        movies.append({
            'id' : 2,
            'name' : 'Wonder Woman',
            'cover' : 'https://image.tmdb.org/t/p/w185_and_h278_bestv2/imekS7f1OuHyUP2LAiTEM0zBzUz.jpg'
        })
        for movie in movies:
            self.db.insert_movie(movie['name'], movie['cover'])
        result = self.db.fetch_movies()
        assert result == movies

if __name__ == "__main__":
    unittest.main()
