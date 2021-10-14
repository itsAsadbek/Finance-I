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

