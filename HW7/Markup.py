class Markup:

    def __init__(self, product_type, number_of_product):
        self.product_type = product_type
        self.number_of_product = number_of_product

    def calculate_markup(self, product_type, number_of_product):

        if product_type == "1":
            product_type = {"upper_cost": 20, "lower_cost": 10, "lower_count": 10}
        elif product_type == "2":
            product_type = {"upper_cost": 20, "lower_cost": 15, "lower_count": 10}
        elif product_type == "3":
            product_type = {"upper_cost": 15, "lower_cost": 10, "lower_count": 5}
        elif product_type == "4":
            product_type = {"upper_cost": 30, "lower_cost": 10, "lower_count": 20}

        if number_of_product >= product_type["lower_count"]:
            return product_type["lower_cost"]
        elif 1 <= number_of_product < product_type["lower_count"]:
            m = (product_type["upper_cost"] - product_type["lower_cost"]) / (1 - product_type["lower_count"])
            markup = m * number_of_product - m + product_type["upper_cost"]
            return markup
        else:
            print('You have not purchased any products')
