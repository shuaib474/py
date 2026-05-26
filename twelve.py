from decimal import Decimal,ROUND_HALF_UP
y=Decimal("8.87776765")
RESULT=y.quantize(Decimal("0.000"),rounding=ROUND_HALF_UP)
print(RESULT)
x=4.7653
print(round(y,3))
print(f"{x:2f}")
z=int(2.65432*100)/100
print(z)

