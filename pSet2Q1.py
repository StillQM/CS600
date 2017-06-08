
# Calculation method definitions
def getMinMonthlyPay(balance, monthlyPaymentRate):
	return monthlyPaymentRate * balance

def getMonthlyUnpaidBalance(balance, minMonthlyPay):
	return balance - minMonthlyPay

def getUpdatedBalance(balance, monthlyInterest):
	return balance + (monthlyInterest * balance)


# Balance, Annual Interest, Monthly Payment Minimum
balance = 5000.00
annualInterestRate = .18
monthlyPaymentRate = .02

# Required Variables
monthlyInterest = annualInterestRate / 12
minMonthlyPay = getMinMonthlyPay(balance, monthlyPaymentRate)
monthlyUnpaidBalance = getMonthlyUnpaidBalance(balance, minMonthlyPay)
updatedBalance = getUpdatedBalance(monthlyUnpaidBalance, monthlyInterest)


# Test Prints 
# print(minMonthlyPay)
# print(monthlyUnpaidBalance)
# print(updatedBalance)

def getOneYearBalance(xBalance, xMonthlyInterest, xMonthlyPaymentRate):
	x = 0
	while x < 12:
		minMonthlyPay = getMinMonthlyPay(xBalance, xMonthlyPaymentRate)
		monthlyUnpaidBalance = getMonthlyUnpaidBalance(xBalance, minMonthlyPay)
		xBalance = getUpdatedBalance(monthlyUnpaidBalance, xMonthlyInterest)
		print("Month " + str(x + 1) + " has balance of: " + str(round(xBalance, 2))) 
		x += 1
	return xBalance


balance = round(getOneYearBalance(balance, monthlyInterest, monthlyPaymentRate), 2) 

print("Your remaining balance is: " + str(round(balance, 2)))