def convert_currency(euro, conversion):
    if conversion == "uk":
        print(euro / 1.25)
    elif conversion == "usd":
        print(euro / 0.95)
    elif conversion == "yen":
        print(euro / 0.46)
    else:
        print("currency not supported")

x = 0
while x == 0:
    amount = input("how much money are you willing to convert: ")
    currency = input("in which currency are you willing to convert?(uk/usd/yen): ")
    convert_currency(float(amount), currency)
    y = 0
    while y == 0: 
        back_exit = input("would you like to make another conversion?(yes/no): ")
        if back_exit == "no" or "NO":
            y = 1
            x = 1
        elif back_exit == "yes" or "YES":
            y = 1
        else:
            print("would you like to make another conversion?(yes/no)")
    
