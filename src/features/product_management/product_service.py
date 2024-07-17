"""
ProductService is the service for product management
"""
from bson import ObjectId
from src.features.product_management.exceptions import InvalidProduct
from src.features.product_management.product_data_access import ProductDataAccess
from src.models.products import Product


class ProductService():
    """
    ProductService is responsible for getting all products and an product details
    """
    def __init__(self):
        self.product_data_access = ProductDataAccess()

    def get_products(self) -> list[Product]:
        """
        This function gets all the products
        """
        products = self.product_data_access.get_products()
        return products

    def get_product_details(self, product_id: ObjectId) -> Product:
        """
        This function gets one product

        params:
            - product_id: The id of the chosen product
        """
        data = {"_id": product_id}
        product = self.product_data_access.get_product_details(data)
        if not product:
            raise InvalidProduct()
        return product
