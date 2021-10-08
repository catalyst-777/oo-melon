"""Classes for melon orders."""
import random

class AbstractMelonOrder():
    """An abstract base class that other Melon Orders inherit from."""
    def __init__(self, species, qty):
        self.species= species
        self.qty = qty
        self.shipped = False
       
    def get_base_price(self):
        base_price = random.randint(5,9)
        return base_price

    def get_total(self):
        """Calculate price, including tax."""

        base_price = self.get_base_price(self)
        total = 0

        if self.qty < 10 and self.order_type== "international":
            total += 3
            
        if self.species=="Christmas melon":
            base_price = base_price * 1.5

        total = (1 + self.tax) * self.qty * base_price
        
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
    #     super().__init__(species, qty)
    
     


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        self.country_code = country_code
    
  
    order_type = "international"
    tax = 0.17


    def get_country_code(self):
        """Return the country code."""

        return self.country_code

class GovernmentMelonOrder(AbstractMelonOrder):
    """A US government melon order with no tax and an extra inspection."""
    def __init__(self, species, qty):
            """Initialize melon order attributes."""
            super().__init__(species, qty)
            self.passed_inspection = False
   
    tax = 0

    def mark_inspection(self,passed):
        if passed == True:
            self.passed_inspection = True
        
        
        


