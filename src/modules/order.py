
from .discount import DiscountEngine

class OrderCalculator:
    def __init__(self, discount_engine: DiscountEngine):
        self.discount_engine = discount_engine

    def final_total(self, subtotal: float, tax_rate: float) -> float:
        disc = self.discount_engine.discount_for(subtotal)
        after_disc = subtotal * (1 - disc)
        tax = after_disc * tax_rate
        return round(after_disc + tax, 2)
