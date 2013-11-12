from firstapp import app

class TestFirstapp():

    def setup_method(self, method):
        self.app = app.test_client()

    # This test is overly simplistic but it does work
    def test_index(self):
        rv = self.app.get('/')

        assert 'Flask' in rv.data
