"""Classes for melon orders."""

from random import randint
from datetime import datetime


class AbstractMelonOrder:
    """An abstract base class that other Melon Orders inherit from"""

    # Attributes that will change in subclasses
    order_type = None
    tax = 0
    # passed_inspection = False

    def __init__(self, species, qty, country_code="US"):
        """Initialize melon order attributes"""

        self.species = species
        self.qty = qty
        self.shipped = False
        # self.country_code = country_code.upper()


    def get_base_price(self):
        """Return a randomized base price (5-9) including splurge pricing"""

        rand_price = randint(5, 9)

        # Add splurge pricing
        # Monday - Friday are 1-5 and mornings 8-11am
        weekdays = list(range(1, 6))
        # print(weekdays)
        day_of_week = datetime.now().strftime('%w')
        # print(day_of_week)
        mornings = list(range(8, 12))
        # print(mornings)
        hour = datetime.now().strftime('%H')
        # print(hour)

        if day_of_week in weekdays and hour in mornings:
            rand_price += 4

        return rand_price


    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price()
        # print(f"base: {base_price}")

        # Add updated pricing for Christmas melons
        if self.species == "Christmas":
            base_price *= 1.5

        total = (1 + self.tax) * self.qty * base_price

        # Update international order pricing
        if (self.order_type == "international" and
            self.qty < 10):

            total += 3    

        return total
    
    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = "domestic"
    tax = 0.08


    # def __init__(self, species, qty):
    #     """Initialize melon order attributes."""

    #     self.species = species
    #     self.qty = qty
    #     self.shipped = False
    #     self.order_type = "domestic"
    #     self.tax = 0.08

    # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = "international"
    tax = 0.17

    def __init__(self, species, qty, country_code):
        super().__init__(species, qty)

        self.country_code = country_code.upper()

    def get_country_code(self):
        """Return the country code."""

        return self.country_code

    # def __init__(self, species, qty, country_code):
    #     """Initialize melon order attributes."""

    #     self.species = species
    #     self.qty = qty
    #     self.country_code = country_code
    #     self.shipped = False
    #     self.order_type = "international"
    #     self.tax = 0.17

    # def get_total(self):
    #     """Calculate price, including tax."""

    #     base_price = 5
    #     total = (1 + self.tax) * self.qty * base_price

    #     return total

    # def mark_shipped(self):
    #     """Record the fact than an order has been shipped."""

    #     self.shipped = True

    # def get_country_code(self):
    #     """Return the country code."""

    #     return self.country_code


class GovernmentMelonOrder(AbstractMelonOrder):
    """Government tax-free melon order."""

    # Inspection boolean that is defaulted to False
    order_type = "government"
    tax = 0

    def __init__(self, species, qty, country_code="US"):
        super().__init__(species, qty, country_code)
        
        self.passed_inspection = False

    # @staticmethod
    def mark_inspection(self, passed):
        """Records whether the order passed inspection or not"""

        self.passed_inspection = passed

