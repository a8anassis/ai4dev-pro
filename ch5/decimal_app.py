"""Υπολογισμός με χρήση της κλάσης Decimal σε Python."""


from decimal import Decimal
from decimal import ROUND_HALF_UP


price = Decimal("19.99")
tax_rate = Decimal("0.24")

vat = price * tax_rate
total_price = price + vat

# Στρογγυλοποίηση με χρήση της κλάσης Decimal
rounded_vat = vat.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)

print(f"Τιμή: {price}, ΦΠΑ: {rounded_vat}, Σύνολο: {total_price}")
