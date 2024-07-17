"""
ProductDataAccess is the data access for product management
"""
from src.config.database import products_collection
from src.models.products import Product


class ProductDataAccess():
    """
    ProductDataAccess is responsible for getting all products and an product details
    """
    def get_products(self) -> list[Product]:
        """
        This function gets all the products
        """
        products = products_collection.find()
        return products

    def get_product_details(self, data: dict) -> Product:
        """
        This function gets one product from the db

        params:
            - data: contains filters to pass to the query
        """
        product = products_collection.find_one(data)
        return product
