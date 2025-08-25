from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

products = [
    {"id": 1, "name": "Phone", "price": 500, "color": "Black", "likes": 0},
    {"id": 2, "name": "Laptop", "price": 1200, "color": "Silver", "likes": 0}
]

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)

@app.route("/products/<int:id>", methods=["GET"])
def get_product(id):
    product = next((p for p in products if p["id"] == id), None)
    return jsonify(product)

@app.route("/products", methods=["POST"])
def add_product():
    data = request.json
    data["id"] = len(products) + 1
    data["likes"] = 0
    products.append(data)
    return jsonify(data)

@app.route("/products/<int:id>", methods=["PUT"])
def edit_product(id):
    data = request.json
    for i, p in enumerate(products):
        if p["id"] == id:
            products[i].update(data)
            return jsonify(products[i])
    return jsonify({"error": "Product not found"}), 404

@app.route("/products/<int:id>", methods=["DELETE"])
def delete_product(id):
    global products
    products = [p for p in products if p["id"] != id]
    return jsonify({"message": "Deleted"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
