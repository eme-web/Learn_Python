#functions
def CalculatePay():
    sales = get_sales()

    advanced_pay = get_advanced_pay()

    comm_rate = get_comm_rate(sales)

    pay = sales * comm_rate - advanced_pay

def get_sales():
    monthly_sales = float(input("Enter your monthly sales: "))
    return monthly_sales


def get_advanced_pay():
    advanced = float(input("Advanced pay: "))
    return advanced


def get_comm_rate():
    if sales < 10000:
        rate =  0.10
    elif sales >= 10000 and sales <= 14999:
        rate = 0.12
    elif sales >= 15000 and sales <= 17999:
        rate = 0.14
    elif sales >= 18000 and sales <= 21999:
        rate = 0.16
    else:
        rate =  0.18

    return rate

CalculatePay()


