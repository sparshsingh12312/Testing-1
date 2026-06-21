principal=float(input("enter th principal amount"))
rate=float(input("enter the rate of interest"))
time=float(input("enter the time duration"))
amount=principal*(1+rate/100)**time
print("amount is",round(amount))

ci=amount-principal
print("compound interest is",round(ci))