def calculate_order(price, cash_coupon, percent_coupon):
    SALES_TAX = .06
    total = price - cash_coupon
    total = total - (total * (percent_coupon / 100))
    total = total + (total * SALES_TAX)

    if (total < 10):
        shipping = 5.95
    elif (10 <= total < 30):
        shipping = 7.95
    elif (30 <= total < 50):
        shipping = 11.95
    else:
        shipping = 0

    total = total + shipping
    return round(total, 2)

