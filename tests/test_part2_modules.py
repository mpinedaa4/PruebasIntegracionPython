
from modules.discount import DiscountEngine
from modules.order import OrderCalculator

def test_order_calculator_uses_discount_engine():
    de = DiscountEngine()
    calc = OrderCalculator(de)

    assert calc.final_total(210.0, 0.19) == 212.41
    assert calc.final_total(120.0, 0.19) == 128.52
    assert calc.final_total(60.0, 0.19) == 67.83
    assert calc.final_total(40.0, 0.19) == 47.6

    """
    Explica por qué esta es una prueba de integración (y no solo unitaria).

    Porque el cálculo del total depende del descuento. El descuento está en
    un módulo y el cálculo del total está en otro módulo. Como hay una 
    dependencia de módulos, necesitamos hacer una prueba de integración y no
    solo una unitaria.
    """