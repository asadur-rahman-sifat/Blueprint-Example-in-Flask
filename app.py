from flask import Flask, request, jsonify, Blueprint

# Create the main Flask application
app = Flask(__name__)

# In-memory storage for users and products
users = {}
products = {}

# Create a blueprint for user-related routes
users_bp = Blueprint('users', __name__)


@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@users_bp.route('/', methods=['POST'])
def create_user():
    user_id = len(users) + 1
    user_data = request.get_json()
    users[user_id] = user_data
    return jsonify({"id": user_id, **user_data}), 201


@users_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id in users:
        user_data = request.get_json()
        users[user_id].update(user_data)
        return jsonify(users[user_id])
    else:
        return jsonify({"error": "User not found"}), 404


@users_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted"}), 200
    else:
        return jsonify({"error": "User not found"}), 404


# Create a blueprint for product-related routes
products_bp = Blueprint('products', __name__)


@products_bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = products.get(product_id)
    if product:
        return jsonify(product)
    else:
        return jsonify({"error": "Product not found"}), 404


@products_bp.route('/', methods=['POST'])
def create_product():
    product_id = len(products) + 1
    product_data = request.get_json()
    products[product_id] = product_data
    return jsonify({"id": product_id, **product_data}), 201


@products_bp.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    if product_id in products:
        product_data = request.get_json()
        products[product_id].update(product_data)
        return jsonify(products[product_id])
    else:
        return jsonify({"error": "Product not found"}), 404


@products_bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    if product_id in products:
        del products[product_id]
        return jsonify({"message": "Product deleted"}), 200
    else:
        return jsonify({"error": "Product not found"}), 404


# Register the blueprints with URL prefixes
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(products_bp, url_prefix='/products')

if __name__ == '__main__':
    app.run(port=5000)
from flask import Flask, request, jsonify, Blueprint

# Create the main Flask application
app = Flask(__name__)

# In-memory storage for users and products
users = {}
products = {}

# Create a blueprint for user-related routes
users_bp = Blueprint('users', __name__)


@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@users_bp.route('/', methods=['POST'])
def create_user():
    user_id = len(users) + 1
    user_data = request.get_json()
    users[user_id] = user_data
    return jsonify({"id": user_id, **user_data}), 201


@users_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id in users:
        user_data = request.get_json()
        users[user_id].update(user_data)
        return jsonify(users[user_id])
    else:
        return jsonify({"error": "User not found"}), 404


@users_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted"}), 200
    else:
        return jsonify({"error": "User not found"}), 404


# Create a blueprint for product-related routes
products_bp = Blueprint('products', __name__)


@products_bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = products.get(product_id)
    if product:
        return jsonify(product)
    else:
        return jsonify({"error": "Product not found"}), 404


@products_bp.route('/', methods=['POST'])
def create_product():
    product_id = len(products) + 1
    product_data = request.get_json()
    products[product_id] = product_data
    return jsonify({"id": product_id, **product_data}), 201


@products_bp.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    if product_id in products:
        product_data = request.get_json()
        products[product_id].update(product_data)
        return jsonify(products[product_id])
    else:
        return jsonify({"error": "Product not found"}), 404


@products_bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    if product_id in products:
        del products[product_id]
        return jsonify({"message": "Product deleted"}), 200
    else:
        return jsonify({"error": "Product not found"}), 404


# Register the blueprints with URL prefixes
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(products_bp, url_prefix='/products')

if __name__ == '__main__':
    app.run(port=5000)
from flask import Flask, request, jsonify, Blueprint

# Create the main Flask application
app = Flask(__name__)

# In-memory storage for users and products
users = {}
products = {}

# Create a blueprint for user-related routes
users_bp = Blueprint('users', __name__)


@users_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@users_bp.route('/', methods=['POST'])
def create_user():
    user_id = len(users) + 1
    user_data = request.get_json()
    users[user_id] = user_data
    return jsonify({"id": user_id, **user_data}), 201


@users_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id in users:
        user_data = request.get_json()
        users[user_id].update(user_data)
        return jsonify(users[user_id])
    else:
        return jsonify({"error": "User not found"}), 404


@users_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        return jsonify({"message": "User deleted"}), 200
    else:
        return jsonify({"error": "User not found"}), 404


# Create a blueprint for product-related routes
products_bp = Blueprint('products', __name__)


@products_bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = products.get(product_id)
    if product:
        return jsonify(product)
    else:
        return jsonify({"error": "Product not found"}), 404


@products_bp.route('/', methods=['POST'])
def create_product():
    product_id = len(products) + 1
    product_data = request.get_json()
    products[product_id] = product_data
    return jsonify({"id": product_id, **product_data}), 201


@products_bp.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    if product_id in products:
        product_data = request.get_json()
        products[product_id].update(product_data)
        return jsonify(products[product_id])
    else:
        return jsonify({"error": "Product not found"}), 404


@products_bp.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    if product_id in products:
        del products[product_id]
        return jsonify({"message": "Product deleted"}), 200
    else:
        return jsonify({"error": "Product not found"}), 404


# Register the blueprints with URL prefixes
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(products_bp, url_prefix='/products')

if __name__ == '__main__':
    app.run(port=5000)
