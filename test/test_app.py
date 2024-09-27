# test_app.py
import unittest
from fastapi.testclient import TestClient
from main import app
from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(DATABASE_URL)
SQLModel.metadata.create_all(engine)


class TestProductAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_create_product(self):
        response = self.client.post("/api/products", json={"sku": "12345", "name": "Test Product"})
        self.assertEqual(response.status_code, 200)
        response_data = response.json()
        self.assertIn("id", response_data)
        self.assertEqual(response_data["sku"], "12345")
        self.assertEqual(response_data["name"], "Test Product")

    def test_add_stock(self):
        response = self.client.patch("/api/inventories/product/1", json={"stock": 50})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Stock updated"})

    def test_create_order(self):
        response = self.client.post("/api/orders", json={"product_id": 1, "quantity": 10})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Order completed"})


if __name__ == "__main__":
    unittest.main()
