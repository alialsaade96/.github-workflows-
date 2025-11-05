import requests

BASE_URL = "https://fakestoreapi.com"

def test_get_products_status_code():
    response = requests.get(f"{BASE_URL}/products")
    assert response.status_code == 200

def test_number_of_products():
    response = requests.get(f"{BASE_URL}/products")
    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 20  # API returnerar 20 produkter

def test_specific_product_fields():
    response = requests.get(f"{BASE_URL}/products/1")
    product = response.json()
    for field in ["title", "price", "category"]:
        assert field in product

def test_specific_product_data():
    response = requests.get(f"{BASE_URL}/products/1")
    product = response.json()
    assert product["id"] == 1
    assert isinstance(product["title"], str)
    assert isinstance(product["price"], float)
