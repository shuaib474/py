from decimal import Decimal,ROUND_HALF_UP
def calc(v,n):
    fmt="0."+"0"*n
    result=Decimal(str(v)).quantize(Decimal(fmt),rounding=ROUND_HALF_UP)
    return result
print(calc(4.666667,4))