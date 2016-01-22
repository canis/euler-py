import decimal as d

d.getcontext().prec = 50
frcts = {i: str(d.Decimal(1) / d.Decimal(i))[2:-1] for i in range (2, 1000)}

for i in frcts:
    
