
1. Clone the repository:
2. 
   git clone https://github.com/yourusername/ecommerce-store.git

Create a virtual environment:


python -m venv venv
Activate the virtual environment:

On macOS and Linux:
source venv/bin/activate

On Windows:
venv\Scripts\activate

Install project dependencies:
pip install -r requirements.txt


Apply database migrations:
python manage.py migrate

Start the development server:
python manage.py runserver


Project full details :  

Model 1: Product
Create a Django model for the product with the following fields:

Name
Category
Size or Weight
Size options: '2xl', 'xl', etc.
Weight options: '500g', '1kg', etc.
Image
The Size or Weight field should dynamically switch between size and weight options based on the category of the product. 
You should implement this logic in your model.

Model 2: Cart
Create a Django model for the shopping cart with the necessary fields to keep track of items in the cart. 
You can decide on the specific fields required, but common fields include:

User
Product
Quantity

Create These APIs

- Add a New Product
Method: POST
Description: This endpoint allows users to add a new product to the e-commerce store.

- Get Product Details
Method: GET
Description: Retrieve details of a specific product by providing its ID.

- Add Product to Cart

Method: POST
Description: Add a product to the user's shopping cart
