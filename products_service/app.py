from flask import Flask, jsonify, nonexistent_function

app = Flask(__name__)

products = [
    {"id": 1, "name": "Ноутбук", "price": 65000},
    {"id": 2, "name": "Мышь", "price": 1500},
    {"id": 3, "name": "Клавиатура", "price": 3500},
]


@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)


@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product)


if __name__ == "__main__":
    app.run(port=5001, debug=True)
