A simple real-world Flask application to demonstrate how to use blueprints and organize your application effectively. In this example, we will create an application that consists of a main module and two blueprints: one for user management and one for product management. This example includes routes for creating, reading, updating, and deleting users and products, simulating basic CRUD operations.

Here is the code for the Flask application:

```python
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
```

### Application Overview:

- **Users Blueprint (`/users`)**:
  - `GET /users/<int:user_id>`: Retrieve a specific user by ID.
  - `POST /users/`: Create a new user and return the created user's data.
  - `PUT /users/<int:user_id>`: Update an existing user's data by ID.
  - `DELETE /users/<int:user_id>`: Delete a user by ID.

- **Products Blueprint (`/products`)**:
  - `GET /products/<int:product_id>`: Retrieve a specific product by ID.
  - `POST /products/`: Create a new product and return the created product's data.
  - `PUT /products/<int:product_id>`: Update an existing product's data by ID.
  - `DELETE /products/<int:product_id>`: Delete a product by ID.

### Key Features:

- The application uses blueprints (`users_bp` and `products_bp`) to manage routes related to users and products, respectively. This helps keep the code organized and modular.
- The application uses in-memory dictionaries (`users` and `products`) to store user and product data for demonstration purposes. In a real application, you would typically use a database instead.
- Each blueprint is registered with a specific URL prefix (`/users` and `/products`), so routes for each blueprint are distinct and can be accessed separately.

To run the application, save the code in a file (e.g., `app.py`) and execute it using Python:

```shell
python app.py
```

The application will start and listen on `http://localhost:5000/`. You can use a tool like [Postman](https://www.postman.com/) or [curl](https://curl.se/) to interact with the application, making requests to the user and product routes for CRUD operations.
