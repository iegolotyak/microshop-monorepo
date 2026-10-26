from flask import Flask, jsonify

app = Flask(__name__)

orders = [
    {"id": 1, "customer_id": 1, "product_id": 2, "quantity": 1},
]


@app.route("/orders", methods=["GET"])
def get_orders():
    return jsonify(orders)


if __name__ == "__main__":
    app.run(port=5003, debug=True)
