def add_vat(price,vat_rate):
    return price *(100 + vat_rate)

order = [100,200,300,400,500]
for item in order:
    final_price = add_vat(item,5)
    print(final_price)