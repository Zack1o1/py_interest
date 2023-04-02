# calculator to calculate interest amount

def interest_amount(principal,month,rate):
    return principal*(month/12)*(rate/100)


principal = float(input("Enter a principal: "))
month = float(input("Enter a month: "))
rate = float(input("Enter an rate: "))

interest_amt =interest_amount(principal,month,rate)
print("Interest amount:", round(interest_amt,2))