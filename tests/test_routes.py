import unittest
from app.routes import app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_trades(self):
        response = self.app.get("/trades")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Fetching trades...", response.data.decode())

if __name__ == "__main__":
    unittest.main()
