"""Bill"""
 
def main():
    """Bill"""
    subtotal = float(input())
    if subtotal*0.1 <= 50:
        service = subtotal + 50
    elif subtotal*0.1 >= 1000:
        service = subtotal + 1000
    else:
        service = subtotal + (subtotal*0.1)
 
 
    vat = service + (service*0.07)
    print('%.2f'% (round(vat, 2)))
 
main()