https://replit.com/@nour55/boilerplate-polygon-area-calculator#main.py
# This entrypoint file to be used in development. Start by reading README.md
import shape_calculator
from unittest import main


rect = shape_calculator.Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(2)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
sq.set_width(4)
print(sq)
print(sq.get_picture())
print(rect.get_amount_inside(sq))



# Run unit tests automatically
main(module='test_module', exit=False)
