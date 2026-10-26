from products_service.app import app


def test_get_products():
    client = app.test_client()
    response = client.get("/products")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)
    assert len(response.get_json()) > 0


def test_get_product_by_id():
    client = app.test_client()
    response = client.get("/products/1")
    assert response.status_code == 200
    assert response.get_json()["id"] == 1


def test_missing_product():
    client = app.test_client()
    response = client.get("/products/999")
    assert response.status_code == 404
