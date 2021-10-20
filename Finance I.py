def fv_annual(pv, r, n):
    factor = (1 + r/100)**n
    fv = pv*factor
    return round(fv, 2)


print(fv_annual(1000, 20, 10))


def pv_annual(fv, r, n):
    factor = (1 + r/100)**n
    pv = fv/factor
    return round(pv, 2)


print(pv_annual(500, 20, 10))


def fv_annuity(pmt, r, n):
    factor = (1 + r/100)**n
    fv = pmt*((factor - 1)/(r/100))
    return round(fv, 2)


print(fv_annuity(500, 6, 5))


def pv_annuity(pmt, r, n):
    factor = (1 + r/100)**n
    pv = pmt*((1 - 1/factor)/(r/100))
    return round(pv, 2)


print(pv_annuity(1000, 5, 10))


def annuity_pmt(fv, r, n):
    factor = (1 + r/100)**n
    pmt = fv/((factor - 1)/(r/100))
    return round(pmt, 2)


print(annuity_pmt(6000, 15, 4))


def fv_annuity_due(pmt, r, n):
    factor = (1 + r/100)**n
    fv = pmt*(((factor - 1)/(r/100))*(1 + r/100))
    return round(fv, 2)


print(fv_annuity_due(500, 6, 5))


def pv_annuity_due(pmt, r, n):
    factor = (1 + r/100)**n
    pv = pmt*(((1 - 1/factor)/(r/100))*(1 + r/100))
    return round(pv, 2)


print(pv_annuity_due(500, 6, 5))


def amortized_loan(pv, r, n):
    factor = (1 + r/100)**n
    pmt = pv/((1 - 1/factor)/(r/100))
    return round(pmt, 2)


print(amortized_loan(6000, 15, 4))


def fv_nonannual(pv, r, n, m):
    factor = (1 + r/(100*m))**(m*n)
    fv = pv*factor
    return round(fv, 2)


print(fv_nonannual(100, 12, 5, 4))


def monthly_mortgage(pv, r, n, m):
    factor = (1 + r/(100*m))**(m*n)
    pmt = pv/((1 - 1/factor)/(r/(100*m)))
    return round(pmt, 2)


print(monthly_mortgage(100000, 8, 25, 12))


def perpetuity(pp, r):
    pv = pp/(r/100)
    return round(pv, 2)


print(perpetuity(500, 8))







################################################################################# Class I
def fv_simple(pv, r, n):
    fv = pv*(1 + (r/100)*n)
    return round(fv,2)

print("The answer is",fv_simple(1000,5,5))


def pv_simple(fv, r, n):
    pv = fv/(1 + (r/100)*n)
    return round(pv,2)

print("The answer is",pv_simple(1250.0,5,5))


def fv_annual(pv, r, n):
    factor = (1 + r/100)**n
    fv = pv*factor
    return round(fv, 2)


print("The answer is",fv_annual(12000, 3.75, 3))


def pv_annual(fv, r, n):
    factor = (1 + r/100)**n
    pv = fv/factor
    return round(pv, 2)


print("The answer is",pv_annual(500, 20, 10))



def fv_nonannual(pv, r, n, m):
    factor = (1 + r/(100*m))**(m*n)
    fv = pv*factor
    return round(fv, 2)


print("The answer is",fv_nonannual(12000, 3.75, 3, 4))



def pv_nonannual(fv, r, n, m):
    factor = (1 + r/(100*m))**(m*n)
    pv = fv/factor
    return round(pv, 2)


print("The answer is",pv_nonannual(180.61, 12, 5, 4))



def fv_continuous_compounding(pv, r, n):
    rate = (r/100)*n
    return round(pv*math.exp(rate),2)



print("The answer is",fv_continuous_compounding(12000,3.75,3))


def pv_continuous_compounding(fv, r, n):
    rate = (r/100)*n
    return round(fv/math.exp(rate),2)



print("The answer is",pv_continuous_compounding(13428.87,3.75,3))
