import unittest
from directors import read_all, read_one
from movies import read_all, read_one

# connex_app.add_api("swagger.yml")
class TestDirectors(unittest.TestCase):
    '''
    Test director
    '''
    def test_read_all(self):
        self.assertIs(type(read_all()), list)

    def test_read_all_err(self):
        self.assertIsNot(type(read_all()), dict)
    

class TestMovies(unittest.TestCase):
    '''
    Test movie
    '''
    def test_read_all(self):
        self.assertIs(type(read_all()), list)

    def test_read_one(self):
        self.assertIs(type(read_one(director_id=7110, movie_id=48399)), dict),

if __name__ == '__main__':
    unittest.main()