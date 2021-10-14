def future_value(pv, rate):
    fv = pv*(1 + rate/100)
    return fv
print(future_value(1000,10))