from flask import Flask, jsonify

app = Flask(__name__)

customers = [
    {"id": 1, "name": "Анна"},
    {"id": 2, "name": "Илья"},
]


@app.route("/customers", methods=["GET"])
def get_customers():
    return jsonify(customers)


if __name__ == "__main__":
    app.run(port=5002, debug=True)
