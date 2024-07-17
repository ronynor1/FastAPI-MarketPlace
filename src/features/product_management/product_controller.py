"""
ProductContoller is the controller for product management
"""
from bson import ObjectId
from src.features.product_management.product_service import ProductService
from src.schema.products_schema import product_serialize, products_list


class ProductContoller():
    """
    ProductContoller is responsible for getting all products and an product details
    """
    def __init__(self):
        self.product_service = ProductService()

    def get_products(self) -> list[dict]:
        """
        This function gets all the products
        """
        products = self.product_service.get_products()
        response = products_list(products)
        return response

    def get_product_details(self, product_id: ObjectId) -> dict:
        """
        This function gets product details by id

        params:
            - product_id: the chosen product
        """
        product = self.product_service.get_product_details(product_id)
        response = product_serialize(product)
        return response
